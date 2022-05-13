import os
import time
import datetime
import threading
from constants import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DirectoryWatcher(FileSystemEventHandler):

    def __init__(self, watch_dir):
        super().__init__()
        self.watch_dir = os.path.abspath(watch_dir)
        self.observer = Observer()
        self.file_folder_maps = {}
        self.log_file = open(f'{os.path.join(os.path.split(os.path.abspath(__file__))[0], "logfile.txt")}', 'a')

        # if the specified directory to watch doe not exists already, then create it
        if not os.path.exists(watch_dir):
            print(f'{watch_dir} does not exists...')
            os.mkdir(watch_dir)
            print(f'created {watch_dir}...')
        else:
            pass

    def on_deleted(self, event):
        # print(f'type = {event.event_type} \t\tpath = {event.src_path}')
        pass

    def on_created(self, event):
        # print(f'type = {event.event_type} \t\tpath = {event.src_path}')
        if os.path.isdir(event.src_path):
            return None
        else:
            file_ext = event.src_path.split('.')[-1]
            # print(f'{file_ext} file added to {self.watch_dir}')

        # initially we assume the created file does not map to any of the known file extensions
        matched = False

        for file_category, file_extensions in FILE_TYPE_MAP.items():
            if file_ext in file_extensions:
                matched = True
                folder_to_place = os.path.join(self.watch_dir, FOLDER_TYPE_MAP.get(file_category))
                break
                # print(f'.{file_ext} files belongs in {folder_to_place}')
        # if the created file does not map to any of the extensions defined in FILE_TYPE_MAP
        if matched is False:
            print(f'unknown file type .{file_ext}')
            return
        if not os.path.exists(folder_to_place):
            os.mkdir(folder_to_place)
            # print(f'created {folder_to_place} for storing .{file_ext} files')

        path_delimeter = os.path.sep

        new_file_name = os.path.join(folder_to_place, event.src_path.split(path_delimeter)[-1])

        # if the file already exists in the target folder, don't attempt to move...
        if os.path.exists(new_file_name):
            audio_thread(f'duplicate already in the {FOLDER_TYPE_MAP.get(file_category)} folder')
            return None
            # if the text to speech module is not installed, don't use the speech function
        try:
            import pyttsx3

        except ModuleNotFoundError:
            print('pyttsx3 not installed, try running \'pip install pyttsx3\'')

        self.log_file.write(f'Action: {event.event_type}\t\tPath: {event.src_path} \t\tDest Folder: {folder_to_place}')
        self.log_file.close()
        os.rename(event.src_path, new_file_name)
        os.listdir(folder_to_place)
        os.listdir(self.watch_dir)
        message = f'file moved to the {FOLDER_TYPE_MAP.get(file_category)} folder'
        audio_thread(message)

    @classmethod
    def start(cls, handler):
        handler.observer.schedule(handler, handler.watch_dir, recursive=False)
        handler.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            handler.observer.stop()

        handler.observer.join()
