import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# 1. गिटहब सीक्रेट से यूट्यूब की चाबी लोड करना
client_secret_json = os.environ.get("YOUTUBE_CLIENT_SECRET")
if not client_secret_json:
    raise ValueError("Error: YOUTUBE_CLIENT_SECRET missing in GitHub Secrets!")

client_config = json.loads(client_secret_json)

# इन दोनों स्कोप्स से वीडियो अपलोड और चैनल सिलेक्ट करने की अनुमति मिलती है
SCOPES = [
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube.readonly'
]

def get_youtube_client():
    creds = None
    # अगर पहले से लॉगइन टोकन सेव है, तो उसे लोड करो
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # अगर पहली बार चला रहे हैं, तो ऑथेंटिकेशन लिंक जनरेट करो
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
        # गिटहब एक्शन्स (कंसोल) के लिए लोकल सर्वर बंद करके लिंक मोड ऑन करेंगे
        auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
        
        print("\n" + "="*60)
        print("🔴 IMPORTANT: YOUTUBE LINK REQUIRED!")
        print("Please open this URL in your browser to log in:")
        print(auth_url)
        print("="*60 + "\n")
        
        # जब आप ब्राउज़र में अलाउ करके कोड लाएंगे, उसे यहाँ डालना होगा
        code = input("Enter the authorization code here: ").strip()
        flow.fetch_token(code=code)
        creds = flow.credentials
        
        # भविष्य के लिए टोकन सेव कर लो
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    return build('youtube', 'v3', credentials=creds)

def upload_video_to_youtube(youtube, video_path, title, description):
    print(f"Uploading {video_path} to YouTube...")
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['shorts', 'horror', 'backrooms', 'apnastoryhindi'],
            'categoryId': '24' # Entertainment category
        },
        'status': {
            'privacyStatus': 'public', # सीधे पब्लिक होगा
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
    print("[1/3] Generating story, voiceover and video...")
    video_file = "final_horror_short.mp4"
    
    # टेस्टिंग के लिए एक खाली वीडियो फाइल बना देते हैं अगर न हो
    if not os.path.exists(video_file):
        with open(video_file, "wb") as f:
            f.write(b"dummy video data")
            
    title = "The Dark Secret of The Backrooms Mystery Hidden Level 🚨 #shorts #horror"
    description = "Explore the deepest secrets of the Backrooms hidden level. Animated horror story by Apna Story Hindi."
    
    print("[2/3] Connecting to YouTube API...")
    youtube_client = get_youtube_client()
    
    print("[3/3] Commencing upload...")
    upload_video_to_youtube(youtube_client, video_file, title, description)
