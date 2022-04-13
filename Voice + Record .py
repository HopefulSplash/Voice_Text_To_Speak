import speech_recognition as sr
import pyttsx3 as tts
import pyaudio as p
from pynput.keyboard import HotKey, Key, KeyCode, Listener

r = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty('voices')


def change_voice(engine, language, gender):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    change_voice(engine, "en_GB", "VoiceGenderMale")

    # get audio from the microphone
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    # recognize speech using google
    try:
        test = r.recognize_google(audio)
        print("You said " + test)
    except sr.UnknownValueError:
        print(" could not understand audio")
    except sr.RequestError as e:
        print(" error; {0}".format(e))

    speak(test)
    print(test)
