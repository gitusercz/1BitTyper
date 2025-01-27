import pygame
import os
import pyttsx3


def play_wav(file_name):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Define the path to the WAV file
    wav_file_path = os.path.join('resources', file_name)

    # Check if the file exists
    if not os.path.isfile(wav_file_path):
        print(f"File '{file_name}' not found in the 'resources' folder.")
        return

    # Load the WAV file
    pygame.mixer.music.load(wav_file_path)

    # Play the WAV file
    pygame.mixer.music.play()

    # Keep the script running long enough to hear the audio
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
if __name__ == "__main__":
    play_wav('your_audio_file.wav')  # Replace with the name of your WAV file

# Function to read the config file
def read_config():
    config = {}
    try:
        with open("config.txt", "r") as file:
            for line in file:
                if '=' in line:
                    name, value = line.strip().split("=")
                    config[name.strip()] = value.strip()
    except FileNotFoundError:
        print("Config file not found. Using default settings.")
    return config

# Function to get config value by name
def get_config_value(config, name, default=None, value_type=str):
    return value_type(config.get(name, default))


import pyttsx3


def read_out_loud_with_voice(text, voice_name_contains):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Get the available voices
    voices = engine.getProperty('voices')

    # Find a voice containing the specified name
    selected_voice = None
    for voice in voices:
        if voice_name_contains.lower() in voice.name.lower():
            selected_voice = voice
            break

    # If the voice is found, set it
    if selected_voice:
        engine.setProperty('voice', selected_voice.id)
        print(f"Using voice: {selected_voice.name}")
    else:
        print(f"Voice containing '{voice_name_contains}' not found. Using default voice.")

    # Set other properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()
