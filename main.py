import speech_recognition as sr
import pyttsx3

# Initialise the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return None

# Main loop
while True:
    # Listen for user input
    command = listen()

    # If command is not recognized, continue to listen
    if command is None:
      continue

    # Set reminder
    if "remind me" in command:
        speak("What are the task you want to add to the to-do list?")
        tasks = []
        while True:
            task = listen()
            if "stop" in task:
                break
            tasks.append(task)
        speak("Here's your to-do list:")
        for i, task in enumerate(tasks):
            speak(f"{i+1}. {task}")

    # Search the web
    elif "search for" in command:
        query = command.replace("search for", "")
        speak(f"Here are the search results for {query}.")
        # Code to search the web goes here

    # Quit the program
    elif "quit" in command:
        speak("Goodbye!")
        break

    # If command is not recognized, continue to listen
    else:
        speak("I'm sorry, I didn't understand. Please try again.")


