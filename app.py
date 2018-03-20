from audio_download import download_audio
from retrieve_urls import get_urls

song_input = open("SongList.txt")
print("Retrieving URLs...")
get_urls(song_input)
url_list = open("SongURLs.txt")
print("Initializing audio downloads...")
download_audio(url_list)
print("Done!")