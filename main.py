import os
import json
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# गिटहब सीक्रेट से चाबी लोड करना
client_secret_json = os.environ.get("YOUTUBE_CLIENT_SECRET")
if not client_secret_json:
    raise ValueError("Error: YOUTUBE_CLIENT_SECRET missing in GitHub Secrets!")

client_config = json.loads(client_secret_json)

SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube.readonly'
]

def get_youtube_client():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        # यहाँ हम स्पष्ट रूप से redirect_uri को localhost पर सेट कर रहे हैं ताकि Error 400 न आए
        flow = InstalledAppFlow.from_client_config(
            client_config, 
            scopes=SCOPES,
            redirect_uri='http://localhost:8080/'
        )
        
        auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
        
        print("\n" + "="*60)
        print("🔴 IMPORTANT: CLICK THIS LINK TO LINK YOUR CHANNEL")
        print(auth_url)
        print("="*60 + "\n")
        
        # चूँकि यह गिटहब पर ऑटो-रुक नहीं सकता, हम क्रेडेंशियल्स को सीधे बाईपास करने के लिए 
        # एक और सीक्रेट चेक करेंगे, अगर वो न हो तो एरर मैसेज देंगे।
        auth_code_secret = os.environ.get("YOUTUBE_AUTH_CODE")
        if auth_code_secret:
            flow.fetch_token(code=auth_code_secret)
            creds = flow.credentials
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        else:
            print("💡 Step 1: Open the link above in your browser.")
            print("💡 Step 2: Choose your 'Apna Story Hindi' channel & Allow permissions.")
            print("💡 Step 3: Copy the 'code' parameter from the address bar (URL) after it redirects to localhost.")
            print("💡 Step 4: Add it to GitHub Secrets with the name: YOUTUBE_AUTH_CODE")
            raise RuntimeError("Authentication pending. Please follow the steps above and run again!")
            
    return build('youtube', 'v3', credentials=creds)

def upload_video_to_youtube(youtube, video_path, title, description):
    print(f"Uploading {video_path} to YouTube...")
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['shorts', 'horror', 'backrooms', 'apnastoryhindi'],
            'categoryId': '24'
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False
        }
    }
    
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimeType='video/mp4')
    request = youtube.videos().insert(part=','.join(body.keys()), body=body, media_body=media)
    
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")
            
    print(f"✅ VIDEO UPLOADED SUCCESSFULLY! Video ID: {response.get('id')}")

if __name__ == "__main__":
    video_file = "final_horror_short.mp4"
    if not os.path.exists(video_file):
        with open(video_file, "wb") as f:
            f.write(b"dummy video data")
            
    title = "The Dark Secret of The Backrooms Mystery Hidden Level 🚨 #shorts #horror"
    description = "Animated horror story by Apna Story Hindi."
    
    youtube_client = get_youtube_client()
    upload_video_to_youtube(youtube_client, video_file, title, description)
