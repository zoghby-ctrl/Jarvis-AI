import ollama
import speech_recognition as sr
from AppOpener import open as app_open
import edge_tts
import asyncio
import pygame
import os

# --- CONFIGURATION ---
MODEL_NAME = "llama3"
VOICE_NAME = "en-GB-RyanNeural" # British Male (Jarvis-ish style)
# Other options: "en-US-ChristopherNeural" (Male), "en-US-AriaNeural" (Female)

recognizer = sr.Recognizer()

# Initialize Sound Player
pygame.mixer.init()

async def speak(text):
    """The Good Voice (Edge TTS)"""
    print(f"\n[JARVIS]: {text}")
    
    # Save audio to a temp file
    output_file = "voice.mp3"
    communicate = edge_tts.Communicate(text, VOICE_NAME)
    await communicate.save(output_file)
    
    # Play it
    try:
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Audio Error: {e}")
    
    # Clean up
    pygame.mixer.music.unload()
    if os.path.exists(output_file):
        os.remove(output_file)

def listen():
    """The Ears"""
    with sr.Microphone() as source:
        print("\n[LISTENING]...", end="\r")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("[THINKING]...             ", end="\r")
            command = recognizer.recognize_google(audio)
            print(f"[YOU]: {command}")
            return command.lower()
        except:
            return ""

async def process_command(command):
    # 1. Open Apps
    if command.startswith("open "):
        app_name = command.replace("open ", "").strip()
        await speak(f"Opening {app_name}...")
        try:
            app_open(app_name, match_closest=True, throw_error=True) 
        except:
            await speak(f"I couldn't find {app_name}")
        return

    # 2. Chat with Llama (WITH PERSONALITY)
    if command:
        print("[PROCESSING]...", end="\r")
        
        system_prompt = (
            "You are Jarvis. You are helpful, precise, and slightly sarcastic. "
            "You can hear and speak. Keep answers short (1-2 sentences)."
        )

        response = ollama.chat(model=MODEL_NAME, messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': command}
        ])
        
        reply = response['message']['content']
        await speak(reply)

async def main():
    print("--- JARVIS V2 (Neural Voice) ---")
    await speak("Systems online. Ready.")
    
    while True:
        try:
            # We can't await listen() because it blocks, 
            # so we run it normally.
            command = listen()
            
            if command:
                if "exit" in command or "quit" in command:
                    await speak("Goodbye, sir.")
                    break
                await process_command(command)
                
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    asyncio.run(main())