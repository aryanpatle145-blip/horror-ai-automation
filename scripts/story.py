import os
from google import genai

def generate_horror_story(topic):
    print(f"Connecting to Gemini AI to generate story for: '{topic}'...")
    
    # GitHub Secrets से सुरक्षित रूप से API की को उठाना
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Error: GEMINI_API_KEY missing in environments!")
    
    # जेमिनी क्लाइंट को चालू करना
    client = genai.Client(api_key=api_key)
    
    # AI के लिए एक दमदार और खौफनाक प्रॉम्प्ट
    prompt = f"""
    You are a professional horror content writer for a famous YouTube channel.
    Write a terrifying, thrilling, and suspenseful horror story in HINDI based on the topic: '{topic}'.
    
    Rules for the story:
    1. Keep it extremely engaging, creepy, and fast-paced (perfect for 2D animation).
    2. Write the main content in Hindi (Devanagari script).
    3. Include a shocking twist at the end.
    4. Duration should be medium (around 200-300 words).
    """
    
    # जेमिनी मॉडल से कहानी लिखवाना
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    story_text = response.text
    print("🔥 Story generated successfully by Gemini AI!")
    return story_text

if __name__ == "__main__":
    # टेस्ट करने के लिए सैंपल टॉपिक
    sample = "Haunted Room 307"
    story = generate_horror_story(sample)
    print("\n--- Generated Story ---\n")
    print(story)
