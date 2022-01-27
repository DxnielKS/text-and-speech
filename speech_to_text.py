import speech_recognition as sr
def speechToText(): # converts speech to text
    global n
    r = sr.Recognizer() // initialise speech recognition tool
    heard = False
    while heard == False: # in order to get an input from the user.
        with sr.Microphone() as source:
            r.pause_thresh = 1.5
            r.adjust_for_ambient_noise(source, duration = 1)
            pygame.mixer.music.load("siri.mp3")
            pygame.mixer.music.play()
            print("Speak..")
            audio = r.listen(source)
        try:
            pygame.mixer.music.load("finished.mp3")
            pygame.mixer.music.play()
            text = r.recognize_google(audio) # changes audio object into string
            print ("You said: %s" % text)
            heard = True
          # loop back to continue to listen for speech
        except sr.UnknownValueError:
            textToSpeech("I didn't quite get that!")
    # chatbox2 = chatbox(text)
    # chatbox2.draw(n)
    # n = n + 1
    # pygame.display.update()
    return text