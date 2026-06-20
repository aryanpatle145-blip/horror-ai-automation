import os
import smtplib
from email.message import EmailMessage

def send_video_to_email():
    # 1. अपनी ईमेल डिटेल्स यहाँ सेट करें
    sender_email = "Patlearyan179@gmail.com"
    # ध्यान दें: इसके लिए आपको अपने Google Account में जाकर 'App Password' जनरेट करना होगा
    sender_password = os.environ.get("EMAIL_APP_PASSWORD", "YOUR_APP_PASSWORD") 
    receiver_email = "Patlearyan179@gmail.com"
    
    # 2. वीडियो फ़ाइल का नाम (जो आपकी स्क्रिप्ट बनाती है)
    video_filename = "output.mp4" 

    if not os.path.exists(video_filename):
        print(f"Error: {video_filename} फ़ाइल नहीं मिली!")
        return

    print("ईमेल तैयार की जा रही है...")
    msg = EmailMessage()
    msg['Subject'] = 'आपकी नई हॉरर एनिमेटेड वीडियो तैयार है! 🎬'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content("भाई, आपकी एनिमेटेड वीडियो बनकर तैयार हो चुकी है। फ़ाइल नीचे अटैच कर दी गई है।")

    # वीडियो फ़ाइल को ईमेल में अटैच करना
    with open(video_filename, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='video', subtype='mp4', filename=file_name)

    # 3. Gmail के सर्वर का उपयोग करके मेल भेजना
    try:
        print("Gmail सर्वर से कनेक्ट हो रहा है...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            print("लॉगिन सफल! ईमेल भेजी जा रही है...")
            smtp.send_message(msg)
            print("बधाई हो भाई! वीडियो सफलतापूर्वक ईमेल पर भेज दी गई है। ✅")
    except Exception as e:
        print(f"ईमेल भेजने में एरर आया: {e}")

if __name__ == "__main__":
    # यहाँ पर आपकी पुरानी वीडियो बनाने वाली स्क्रिप्ट का कोड रहेगा
    # उदाहरण के लिए: generate_video()
    
    # वीडियो बनने के बाद यह फंक्शन उसे मेल कर देगा
    send_video_to_email()
