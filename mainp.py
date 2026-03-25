import speech_recognition as sr
import pyttsx3 as tts
import webbrowser as web
import time
import music_lib
r = sr.Recognizer()
def speak(text):
    engine = tts.init()
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.5)

def process_command(c):
    print(f"Processing: '{c}'")
    if "youtube" in c.lower():
        speak("Opening YouTube")
        web.open("https://youtube.com")
    elif "google" in c.lower():
        speak("Opening Google")
        web.open("https://google.com")
    elif "github" in c.lower():
        speak("Opening GitHub")
        web.open("https://github.com")
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = music_lib.songs[song]
        speak(f"playing {song}")
        web.open(link)
    else:
        speak("Sorry, I didn't understand that command.")
if __name__ == "__main__":
    speak("Initializing Rahul's agent")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print("You said:", word)

            if word.lower() == "alexa":
                speak("Alexa is activated. How can I help you sir?")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                process_command(command)

        except sr.WaitTimeoutError:
            print("You didn't speak in time")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except KeyboardInterrupt:
            speak("An error occured!")
            print("Agent stopped")
            break
        except Exception as e:
            print("Error:", e)