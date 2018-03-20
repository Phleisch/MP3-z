import re
import urllib
from bs4 import BeautifulSoup

input_file = open("SongList.txt")
urls = open("SongURLs.txt", "w")
songs = input_file.readlines()
regex = '[^A-Za-z0-9 ]'
search_const = "https://www.youtube.com/results?search_query="

for song in songs:
	song = song.strip("\n")
	song = re.sub(regex, '', song)
	song = song + " audio"
	song = urllib.parse.quote(song)
	query = search_const + song
	#print(query)
	response = urllib.request.urlopen(query)
	html = response.read()
	soup = BeautifulSoup(html, "html5lib")
	videos_info = soup.findAll(attrs={'class':'yt-uix-tile-link'})
	first_video_info = videos_info[0]
	first_url = 'https://www.youtube.com' + first_video_info['href']
	urls.write('%s\n'%first_url)
urls.close()
input_file.close()