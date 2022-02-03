import speech_recognition as sr
import pygame
def speech_to_text(): # converts speech to text
    recognizer = sr.Recognizer() # initialise speech recognition tool
    heard = False
    while heard == False: # in order to get an input from the user.
        with sr.Microphone() as source:
            recognizer.pause_thresh = 1.5
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            pygame.mixer.music.load("siri.mp3")
            pygame.mixer.music.play()
            print("Speak..")
            audio = recognizer.listen(source)
        try:
            pygame.mixer.music.load("finished.mp3")
            pygame.mixer.music.play()
            text = recognizer.recognize_google(audio) # changes audio object into string
            print("You said: %s" % text)
            heard = True
          # loop back to continue to listen for speech
        except sr.UnknownValueError:
            print("Unknown error!")
    return text