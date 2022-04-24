#! /usr/bin/python3
from track import *
from utils import *

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'progress_hooks': [my_hook],
    'outtmpl' : 'music/%(title)s.%(ext)s',
    'external_downloader_args': ['-loglevel', 'panic']
}
