import os
import random
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = 'c'
openai.api_key = api_key

def get_comparable_items():
    topics = [ "car", "movie", "book", "technology", "sport", "vacation destination",
        "music genre", "restaurant", "video game", "smartphone", "programming language", "TV show",
        "software tool", "historical figure", "animal", "brand", "computer", "fitness routine",
        "fashion trend", "coffee", "tea", "sports team", "celebrity", "website",
        "social media platform", "financial investment", "city", "holiday", "gadget", "fitness tracker",
        "car model", "smartwatch", "online course", "mobile app", "exercise equipment", "gaming console",
        "diet plan", "podcast", "educational institution", "vacation activity", "real estate property",
        "art style", "music album", "book genre", "home appliance", "movie genre", "TV series", "board game",
        "digital camera", "smart home device", "travel destination", "personal finance app", "budgeting tool",
        "language learning app", "e-commerce platform", "writing style", "architectural style", "career field",
        "type of cuisine", "virtual reality game", "movie director", "music artist", "charity organization",
        "personal development book", "fitness app", "online learning platform", "health supplement", "workout routine",
        "social cause", "investment strategy", "crypto currency", "automobile brand", "streaming service",
        "dating app", "television network", "cultural festival", "book author", "type of therapy", "healthcare provider",
        "business model", "shopping mall", "skincare product", "gourmet food", "home decor style", "personal assistant app",
        "subscription box", "creative hobby", "outdoor gear", "online gaming platform", "fashion accessory",
        "energy drink", "board sport", "sustainable product", "office furniture", "sustainable brand", "fashion designer",
        "luxury brand", "online fitness class", "nutritional plan", "audio book", "mystery novel", "science fiction movie",
        "financial product", "luxury vacation", "unique experience", "high-end gadget", "ethical fashion brand",
        "eco-friendly product", "tech startup", "cloud service", "robotics", "smart home system", "AI application",
        "web design tool", "virtual event", "startup founder", "innovation hub", "business conference", "wearable tech",
        "electric vehicle", "digital payment service", "financial tech", "enterprise software", "3D printing", "urban farming",
        "sustainable energy", "remote work tool", "career mentor", "public speaking course", "online community",
        "work-life balance tool", "personal safety app", "meal kit service", "renewable resource", "travel app",
        "adventure sport", "non-profit organization", "cultural exchange program", "language exchange app", "tech gadget",
        "artificial intelligence tool", "freelancing platform", "business incubator", "crowdfunding platform",
        "virtual assistant", "smart kitchen appliance", "digital marketing tool", "financial advisor", "mobile payment solution",
        "public transportation app", "digital art", "e-book", "sustainable fashion", "impact investment", "personal finance tool",
        "online tutoring service", "telehealth service", "mental health app", "entrepreneurship course", "gaming headset",
        "solar power system", "home renovation", "online marketplace", "subscription service", "virtual reality headset",
        "augmented reality app", "cryptocurrency exchange", "investment app", "digital wallet", "innovative startup",
        "online course platform", "smart home security", "interactive website", "cloud storage solution", "data analytics tool",
        "home automation", "AI-driven product", "tech review site", "sustainable packaging", "career coaching", "cybersecurity tool",
        "personal development course", "digital asset management", "internet of things device", "startup accelerator",
        "renewable energy source", "ethical tech company", "online health resource", "luxury lifestyle brand", "crowdsourced content",
        "tech gadget review", "social impact startup", "digital productivity tool", "online job board", "robotic process automation",
        "home energy management", "biodegradable product", "remote team collaboration tool", "smart garden", "virtual networking event",
        "wellness app", "digital education platform", "AI-powered tool", "tech-focused podcast", "online financial service",
        "virtual conference", "augmented reality game", "digital learning tool", "sustainable transportation", "tech entrepreneurship",
        "smart city technology", "personal finance blog", "investment platform", "virtual coworking space", "tech innovation award",
        "digital art platform", "ethical investment fund", "online fitness tracker", "robotic technology", "cloud-based service",
        "tech entrepreneur", "innovative tech product", "business analytics tool" ]  # The list of topics

    topic = random.choice(topics)
    
    # Construct the prompt
    question = f"Given the topic '{topic}', give me a list of 15 items to compare so people can poll on them."
    
    # Make the API request using openai library
    try:
        
        response = openai.Completion.create(
            model="babbage-002",  # Corrected model name
            prompt=question,
            max_tokens=200
        )
        # Handle the response
        choices = response.get('choices', [])
        if choices:
            response_text = choices[0].get('text', '').strip()
            return response_text
        else:
            return "No choices returned in the response."
    
    except Exception as e:
        return f"Error occurred: {e}"
