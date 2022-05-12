import sys
import os

ES_EBOOK = 0
ES_AUDIO = 1
ES_IMAGE = 2
ES_VIDEO = 3
ES_EXECUTABLE = 4

FILE_TYPE_MAP = {
    ES_EBOOK: ['pdf'],
    ES_AUDIO: ['mp3', 'ogg', 'wav', 'mpeg'],
    ES_IMAGE: ['png', 'jpeg', 'bmp', 'jpg', 'ico', 'gif'],
    ES_VIDEO: ['mp4', 'avi', 'm4', 'webm'],
    ES_EXECUTABLE: ['exe', 'bat', 'msi'],
}
if sys.platform == 'linux':
    FILE_TYPE_MAP[ES_EXECUTABLE] = ['run', 'sh']

FOLDER_TYPE_MAP = {
    ES_EBOOK: 'Ebooks',
    ES_AUDIO: 'Audios',
    ES_IMAGE: 'Images',
    ES_VIDEO: 'Videos',
    ES_EXECUTABLE: 'Programs',
}


def audio_thread(msg) -> None:
    code_ = f"""
import time
import pyttsx3
audio_engine = pyttsx3.init()
audio_engine.setProperty('rate', 170)
audio_engine.say('{msg}')
audio_engine.runAndWait()
            """
    curr_dir = os.path.abspath(__file__)
    curr_dir = f'{os.path.sep}'.join(curr_dir.split(os.path.sep)[0:-1])
    temp_file_path = os.path.join(curr_dir, 'temp.py')
    temp_file = open('temp.py', 'w')
    temp_file.write(code_)
    temp_file.close()
    import subprocess
    command = f'{sys.executable} {temp_file_path}' if sys.platform == 'win32' else f'python3 {temp_file_path}'
    res = subprocess.run(command, stdout=sys.stdout, stdin=sys.stdin)


