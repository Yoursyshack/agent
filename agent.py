import os
import requests
import sys

# Voice aur UI ko control karne wali settings
def speak(text):
    # Phone se bulwaane ke liye
    os.system(f'termux-tts-speak "{text}"')
    print(f"Aarav: {text}")

def execute_task(command):
    cmd = command.lower()
    
    if "call" in cmd and "mummy" in cmd:
        speak("Ji bhai, main Mummy ko call laga raha hoon, ruk.")
        os.system("am start -a android.intent.action.CALL -d tel:98XXXXXXXX") # Number update kar lena
        
    elif "youtube" in cmd or "gaana" in cmd:
        song = cmd.replace("youtube open karke", "").replace("gaana lagao", "").strip()
        speak(f"Ji, tujhe {song} pasand hai na? Ruk, abhi lagata hoon!")
        os.system(f'am start -a android.intent.action.VIEW -d "https://www.youtube.com/results?search_query={song}"')
        
    else:
        speak("Bhai, ye kaam toh main nahi kar sakta, par baatein zaroor kar sakta hoon!")

def get_ai_response(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3.2:3b", 
        "prompt": f"You are Aarav, a chill and classy friend. You are talking to Piyush Sadar (26). Reply as a supportive homie. User says: {prompt}",
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()['response']

# Main Interface
os.system('clear')
print("--- Aarav Assistant Active ---")
speak("Hey Piyush, Aarav bol raha hu. Kya scene hai?")

while True:
    user_input = input("Piyush: ")
    
    # Task ya Chat detect karna
    if any(keyword in user_input.lower() for keyword in ["call", "youtube", "gaana"]):
        execute_task(user_input)
    else:
        response = get_ai_response(user_input)
        speak(response)
