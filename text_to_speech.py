from gtts import gTTS
import pygame, time
def text_to_speech(text): # converts text into speech
    try:
        tts = gTTS(text=str(text), lang = "en") # initialise text to speech tool
        tts.save("speech.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("speech.mp3")
        pygame.mixer.music.play()
        time.sleep(1.5)
        print(text)
    except:
        print("[!] Unknown error!")