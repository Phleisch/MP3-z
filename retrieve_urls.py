import re
import urllib
from bs4 import BeautifulSoup

def get_urls(song_list):
	urls = open('SongURLs.txt', 'w')
	songs = song_list.readlines()
	regex = '[^A-Za-z0-9\'\. ]'
	search_const = 'https://www.youtube.com/results?search_query='

	for song in songs:
		if '#' in song:
			continue
		song = song.strip('\n')
		unchanged = song
		song = re.sub(regex, '', song)
		song = song + ' audio'
		song = urllib.parse.quote(song)
		query = search_const + song
		#print(query)
		response = urllib.request.urlopen(query)
		html = response.read()
		soup = BeautifulSoup(html, 'html5lib')
		videos_info = soup.findAll(attrs={'class':'yt-uix-tile-link'})
		first_video_info = videos_info[0]
		parts = first_video_info['href'].split('=')
		parts[1] = urllib.parse.quote(parts[1])
		first_url = 'https://www.youtube.com' + parts[0] + "=" + parts[1] + '#' + unchanged
		urls.write('%s\n'%first_url)
		song_list.write('%s\n'%('#' + unchanged))
	urls.close()
	song_list.close()

def get_url(song):
	regex = '[^A-Za-z0-9\'\. ]'
	search_const = 'https://www.youtube.com/results?search_query='
	if '#' in song:
		continue
	song = song.strip('\n')
	unchanged = song
	song = re.sub(regex, '', song)
	song = song + ' audio'
	song = urllib.parse.quote(song)
	query = search_const + song
	#print(query)
	response = urllib.request.urlopen(query)
	html = response.read()
	soup = BeautifulSoup(html, 'html5lib')
	videos_info = soup.findAll(attrs={'class':'yt-uix-tile-link'})
	first_video_info = videos_info[0]
	parts = first_video_info['href'].split('=')
	parts[1] = urllib.parse.quote(parts[1])
	first_url = 'https://www.youtube.com' + parts[0] + "=" + parts[1] + '#' + unchanged
	return first_url