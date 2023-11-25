from gtts import gTTS
import os
import subprocess


def play_mp3(file_path):
    subprocess.run(['mpg123', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def tts(text, language):
    speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
    speech.save("tts.mp3")
    mp3_file_path = "tts.mp3"
    play_mp3(mp3_file_path)
    os.remove("tts.mp3")
