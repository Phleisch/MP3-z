import pafy

input_file = open("SongURLs.txt")
urls = input_file.readlines()
for url in urls:
	url = url.strip()
	video = pafy.new(url)
	best_audio = video.getbestaudio()
	current_file = best_audio.download("\songs")