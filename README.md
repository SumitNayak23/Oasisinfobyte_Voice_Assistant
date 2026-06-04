# Voice Assistant

A simple Python voice assistant for beginners. It can respond to greetings, tell the current time or date, search the web, provide a basic weather example, and save reminders.

## Features

- Voice command recognition using `speech_recognition`
- Text-to-speech responses with `pyttsx3`
- Time and date replies
- Web search support
- Basic weather summary example
- Simple reminder storage and retrieval
- Fallback to typed commands when the microphone is unavailable

## Requirements

- Python 3.8+ recommended
- `pyttsx3`
- `SpeechRecognition`
- `requests`
- A working microphone for voice input (optional)

## Installation

1. Open a terminal in the project folder.
2. Install the required packages:

```bash
pip install pyttsx3 SpeechRecognition requests
```

3. On Windows, you may also need the `pyaudio` package for microphone input:

```bash
pip install pyaudio
```

If `pyaudio` installation fails, use the appropriate wheel for your Python version from `https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio`.

## Usage

Run the assistant with:

```bash
python "voice assistant.py"
```

The assistant will try to use the microphone first. If the microphone cannot be accessed, it will ask you to type commands instead.

### Example commands

- `Hello`
- `What time is it?`
- `What is the date?`
- `Search for Python tutorials`
- `Weather`
- `Set reminder to buy milk`
- `Show reminder`
- `Exit`

## Notes

- The weather feature uses a public free API example and may only work for the default location in the script.
- Email sending is shown as a placeholder and requires additional SMTP configuration for real use.

## License

This project is provided as-is for learning and experimentation.
