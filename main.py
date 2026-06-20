import os
# सभी स्क्रिप्ट्स को इम्पोर्ट कर रहे हैं
from scripts.trends import fetch_trending_topics
from scripts.story import generate_horror_story
from scripts.voice import generate_voiceover
from scripts.image import generate_horror_images
from scripts.video import create_shorts_video
from scripts.seo import generate_video_seo
from scripts.upload import upload_to_youtube
from scripts.analytics import check_video_performance

def main():
    print("==============================================")
    print("   HORROR AI AUTOMATION: PROCESS STARTED     ")
    print("==============================================")
    
    # Step 1: Trending Topic Search
    print("\n[1/8] Searching trending horror topics...")
    topics = fetch_trending_topics()
    current_topic = topics[0] # सबसे पहला ट्रेंडिंग टॉपिक चुन रहे हैं
    
    # Step 2: Story Generation
    print("\n[2/8] Generating AI Horror Story...")
    story_text = generate_horror_story(current_topic)
    
    # Step 3: Voice Generation
    print("\n[3/8] Generating AI Voiceover...")
    audio_path = generate_voiceover(story_text)
    
    # Step 4: Image Generation
    print("\n[4/8] Generating Cinematic Horror Images...")
    images_list = generate_horror_images(story_text)
    
    # Step 5: Video Creation
    print("\n[5/8] Editing & Creating Shorts Video...")
    video_path = create_shorts_video(audio_path, images_list)
    
    # Step 6: SEO Optimization
    print("\n[6/8] Generating SEO Title, Description & Tags...")
    seo_metadata = generate_video_seo(current_topic)
    
    # Step 7: YouTube Upload
    print("\n[7/8] Uploading Short to YouTube...")
    upload_success = upload_to_youtube(video_path, seo_metadata)
    
    # Step 8: Analytics & Logs
    if upload_success:
        print("\n[8/8] Checking Analytics & Saving Logs...")
        stats = check_video_performance()

    print("\n==============================================")
    print("   HORROR AI AUTOMATION: ALL STEPS LINKED!    ")
    print("==============================================")

if __name__ == "__main__":
    main()
