import os
from audio_download import download_audio
from retrieve_urls import get_urls

song_input = open('SongList.txt', 'r+')
print('Retrieving URLs...')
get_urls(song_input)
url_list = open('SongURLs.txt')
print('Initializing audio downloads...')
download_audio(url_list)
print('\nDone!')
song_input.close()
url_list.close()
os.remove('SongURLs.txt')