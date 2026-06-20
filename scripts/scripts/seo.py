import os

def generate_video_seo(topic):
    print(f"Generating SEO metadata for topic: '{topic}'...")
    
    # अभी के लिए हम एक बेस्ट वायरल SEO टेम्पलेट रख रहे हैं, बाद में इसे AI से पूरी तरह डायनामिक बनाएंगे
    seo_data = {
        "title": f"The Dark Secret of {topic} 😱 #shorts #horror",
        "description": f"This creepy horror story about {topic} will give you goosebumps. Watch till the end if you dare!\n\n#horrorshorts #apnastoryhindi #creepypasta #backrooms",
        "tags": ["horror stories", "shorts", "scary stories in hindi", topic, "apna story hindi", "viral shorts"]
    }
    
    print("SEO Metadata generated successfully!")
    print(f"Suggested Title: {seo_data['title']}")
    return seo_data

if __name__ == "__main__":
    sample_topic = "The Backrooms Mystery Hidden Level"
    seo = generate_video_seo(sample_topic)
