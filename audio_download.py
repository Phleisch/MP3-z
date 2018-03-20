import re
import pafy

def download_audio(urls):
	regex = '[ ]'
	input_file = urls
	urls = input_file.readlines()
	for url in urls:
		url = url.strip()
		parts = url.split("#")
		print("\nCurrently downloading %s..."%parts[1])
		video = pafy.new(parts[0])
		best_audio = video.getbestaudio()
		title = parts[1].title()
		title = re.sub(regex, '', title)
		file_save = "songs/" + title + ".mp3"
		current_file = best_audio.download(file_save)