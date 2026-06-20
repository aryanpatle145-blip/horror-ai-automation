import os

def generate_horror_story(topic):
    print(f"Generating horror story for topic: '{topic}'...")
    
    # अभी के लिए एक बेस स्टोरी टेम्पलेट रख रहे हैं, बाद में इसे Gemini AI से कनेक्ट करेंगे
    story_template = f"""
    [Title: The Mystery of {topic}]
    
    क्या आप जानते हैं कि इतिहास में कुछ ऐसी घटनाएं हैं जिन्हें कभी सुलझाया नहीं जा सका? 
    अंधेरे कमरे में जब दीवारें फुसफुसाने लगें, तो समझ जाना कि वो आ चुके हैं। 
    सांसें रोक लो, क्योंकि जो कहानी आप सुनने जा रहे हैं, वो आपका चैन छीन लेगी...
    """
    
    print("Horror story generated successfully!")
    return story_template

if __name__ == "__main__":
    sample_topic = "The Backrooms Mystery Hidden Level"
    story = generate_horror_story(sample_topic)
    print("\n--- Generated Story ---\n", story)
