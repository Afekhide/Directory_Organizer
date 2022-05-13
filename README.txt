====================================================================
|                                                                  |
|                                                                  |
|                           DirOrganizer                                                                 |
|                                                                  |
|                                                                  |
====================================================================

ABOUT
======
directory_organizer is a simple and handy tool that help your organize your folders for easy searching.
It works by watching a user specified directory, and when a file gets added to that directory, it determines
the file category (based on the file extension) and then puts that file into its appropriate folder.
For example, say you want to `watch` your Desktop folder, assuming it's hypothetical path is 'C:\Users\Randy\Desktop'
then adding a .jpg file to your the Desktop directory would be categorized as an Image file and as such would get added to
Desktop/Images.

FILE_CATEGORIES
==================

# IMAGES
['png', 'jpeg', 'bmp', 'jpg', 'ico', 'gif', 'tiff']

#EBOOKS
['pdf', 'epub', 'cbz', 'cbr', 'djvu', 'mobi', 'azw', 'tpz', 'lrs', 'jwpub', 'lit', 'ebk']

#AUDIOS
[.wma, .mp3, .wav, .ogg]

#VIDEOS
['mp4', 'avi', 'mpeg', 'webm', 'mov', 'flv', 'm4p', 'm4v', 'mpg', 'mpe', '.swf']

#WINDOWS EXECUTABLES
[.exe. .bat, .msi]                           => Executables #For Windows

#LINUX EXECUTABLES
[.sh, .run]                                  => Executables #For Linux


SETUP
======
1. cd to project root directory
2. For Windows, run `pip install -r requirements.txt`
   For Linux, run   `pip3 install -r requirements.txt`


USAGE
=======

1. Open your terminal / command prompt
2. cd into the project root folder, example `cd /path/to/main/project/directory_organizer`
3. For Linux users, run `python3 app.py /path/to/watch/folder`
   For Windows users, run `python app.py /path/to/watch/folder`
   Where '/path/to/watch/folder' represents the full path to the folder you want to



