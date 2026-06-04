# import datetime
# import json
# import os
# import sys
# import webbrowser

# try:
#     import pyttsx3
#     import requests
#     import speech_recognition as sr
# except ImportError:
#     print("Required libraries are missing. Install with: pip install pyttsx3 SpeechRecognition requests")
#     sys.exit(1)

# engine = pyttsx3.init()
# engine.setProperty("rate", 155)
# engine.setProperty("volume", 1.0)

# recognizer = sr.Recognizer()


# def speak(text: str) -> None:
#     """Speak text out loud and print it to the console."""
#     print(f"Assistant: {text}")
#     engine.say(text)
#     engine.runAndWait()


# def listen_from_microphone(timeout: int = 6) -> str:
#     """Listen for a voice command from the microphone."""
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=0.8)
#         speak("Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=timeout)
#             return recognizer.recognize_google(audio)
#         except sr.WaitTimeoutError:
#             return ""
#         except sr.UnknownValueError:
#             return ""
#         except sr.RequestError:
#             speak("I could not reach the speech recognition service.")
#             return ""


# def get_command(use_voice: bool = True) -> str:
#     """Get a command from the user via voice or typed text."""
#     if use_voice:
#         command = listen_from_microphone()
#         if command:
#             print(f"You said: {command}")
#             return command.lower()
#         speak("I did not understand that. Please type your command.")
#     return input("Type your command: ").strip().lower()


# def get_current_time() -> str:
#     return datetime.datetime.now().strftime("%I:%M %p")


# def get_current_date() -> str:
#     return datetime.datetime.now().strftime("%A, %B %d, %Y")


# def search_web(query: str) -> None:
#     url = f"https://www.google.com/search?q={webbrowser.quote(query)}"
#     webbrowser.open(url)
#     speak(f"I searched the web for {query}.")


# def send_simple_email() -> None:
#     speak("To send email, I need your configured SMTP settings and permission.")
#     speak("This feature is not enabled by default in this demo.")


# def simple_weather_summary() -> None:
#     speak("I can provide a basic weather summary for a fixed location.")
#     city = "New York"
#     api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={webbrowser.quote(city)}&count=1"
#     try:
#         resp = requests.get(api_url, timeout=8)
#         resp.raise_for_status()
#         data = resp.json()
#         if data.get("results"):
#             location = data["results"][0]
#             lat = location["latitude"]
#             lon = location["longitude"]
#             weather_url = (
#                 f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
#             )
#             weather_resp = requests.get(weather_url, timeout=8)
#             weather_resp.raise_for_status()
#             weather_data = weather_resp.json().get("current_weather", {})
#             if weather_data:
#                 temp = weather_data.get("temperature")
#                 condition = weather_data.get("weathercode")
#                 speak(f"Current temperature in {city} is {temp} degrees Celsius.")
#                 return
#         speak("I could not get weather for the example location.")
#     except requests.RequestException:
#         speak("There was a network problem while fetching weather data.")


# def process_command(command: str, use_voice: bool) -> bool:
#     """Process the user's command and return False when the assistant should stop."""
#     if not command:
#         speak("Please say a command or type one.")
#         return True

#     if any(token in command for token in ["exit", "quit", "stop", "bye"]):
#         speak("Goodbye. Have a nice day.")
#         return False

#     if any(token in command for token in ["hello", "hi", "hey"]):
#         speak("Hello! I am your voice assistant. How can I help you today?")
#         return True

#     if "time" in command:
#         speak(f"The current time is {get_current_time()}.")
#         return True

#     if "date" in command:
#         speak(f"Today is {get_current_date()}.")
#         return True

#     if "search" in command or "google" in command or "look up" in command:
#         query = command.replace("search", "").replace("google", "").replace("look up", "").strip()
#         if not query:
#             speak("What would you like me to search for?")
#             query = get_command(use_voice)
#         if query:
#             search_web(query)
#         return True

#     if "weather" in command:
#         simple_weather_summary()
#         return True

#     if "email" in command or "send email" in command:
#         send_simple_email()
#         return True

#     if "how are you" in command or "how is it going" in command:
#         speak("I am good, thank you. I am ready to help you.")
#         return True

#     if "reminder" in command:
#         speak("I can remind you of something during this session.")
#         reminder = command.replace("reminder", "").strip()
#         if not reminder:
#             speak("What should I remind you about?")
#             reminder = get_command(use_voice)
#         if reminder:
#             speak(f"Reminder set: {reminder}. I will repeat it when you ask.")
#             with open("reminder.txt", "w", encoding="utf-8") as file:
#                 json.dump({"reminder": reminder}, file)
#         return True

#     if "what is my reminder" in command or "show reminder" in command or "read reminder" in command:
#         if os.path.exists("reminder.txt"):
#             with open("reminder.txt", "r", encoding="utf-8") as file:
#                 data = json.load(file)
#             speak(f"Your reminder is: {data.get('reminder')}")
#         else:
#             speak("You have no reminders saved yet.")
#         return True

#     if "help" in command or "options" in command:
#         speak(
#             "I can tell you the time or date, search the web, give a weather example, set a reminder, and respond to greeting commands."
#         )
#         return True

#     speak("I am sorry, I did not understand that command. Say help to see some options.")
#     return True


# def main() -> None:
#     speak("Hello! I am your voice assistant.")
#     use_voice = True

#     try:
#         with sr.Microphone() as source:
#             pass
#     except (OSError, sr.RequestError):
#         speak("I could not access the microphone. Switching to text input mode.")
#         use_voice = False

#     if use_voice:
#         speak("Say a command anytime, or type it if you prefer.")
#     else:
#         speak("Type your commands below.")

#     while True:
#         command = get_command(use_voice)
#         if not process_command(command, use_voice):
#             break


# if __name__ == "__main__":
#     main()
