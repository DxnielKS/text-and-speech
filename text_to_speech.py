from gtts import gTTS
def textToSpeech(text): # converts text into speech
    global n
    print ("Avis said: %s" % text)
    chatbox1 = chatbox(text)
    chatbox1.draw(n)
    n = n + 1
    pygame.display.update()
    try:
        tts = gTTS(text=str(text), lang = "en")
        tts.save("speech.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("speech.mp3")
        pygame.mixer.music.play()
        time.sleep(1.5)
    except:
        print("[!] Not able to connect to text to speech services!")