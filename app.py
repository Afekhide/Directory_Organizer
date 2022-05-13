import subprocess
import sys
import os
from dirWatcher import DirectoryWatcher

if len(sys.argv) < 2:
    print(f'Requires 2 arguments, found {len(sys.argv)}')
    usage = f'Sample Usage:\t{sys.executable} {__file__} {"path/to/folder/to/watch".replace("/", os.path.sep)}'
    print(usage)
    sys.exit(0)
watch_dir = sys.argv[1]
eventHandler = DirectoryWatcher(watch_dir=watch_dir)

if __name__ == '__main__':

    # os.chdir(os.path.split(os.path.abspath(__file__)))
    if sys.platform == 'linux':
        command = f'pip3 install -r requirements.txt'
    elif sys.platform == 'win32':
        command = f'pip install -r requirements.txt'
    else:
        print('For now this program is only developed for Linux and Windows machines...')
        exit(0)

    print(f'watching {watch_dir}....')
    DirectoryWatcher.start(eventHandler)

