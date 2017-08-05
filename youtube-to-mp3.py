from __future__ import unicode_literals
import youtube_dl
import urllib.request
from bs4 import BeautifulSoup
import time

playlist_file = "your-playlist.txt"

with open(playlist_file) as file:
    songs = file.readlines()
songs = [x.strip() for x in songs]

for song in songs:
    textToSearch = song
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")

    print("Youtube Song URL for %s is:", query)
    print('https://www.youtube.com' + soup.find(attrs={'class': 'yt-uix-tile-link'})['href'])
    youtube_song_url = 'https://www.youtube.com' + soup.find(attrs={'class': 'yt-uix-tile-link'})['href']

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    print("Downloading %s ....", query)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_song_url])
    time.sleep(5)