import os
from google import genai

# The SDK automatically detects the "GEMINI_API_KEY" environment variable.
# No need to manually pass it if it is correctly set in your environment.
client = genai.Client() 

def get_response(prompt):                                                
    response = client.models.generate_content(                           
        model="gemini-2.5-flash",                                        
        contents=prompt                                                  
    )
    return response.text
