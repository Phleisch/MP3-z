import re
import string
import pafy

def title_except(s, exceptions):
    word_list = re.split(' ', s)       # re.split behaves as expected
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        final.append(word if word in exceptions else word.capitalize())
    return " ".join(final)

def download_audio(url):
	articles = ['a', 'an', 'of', 'the', 'is']
	url = url.strip('\n')
	parts = url.split('#')
	print('\nCurrently downloading %s...'%parts[1])
	video = pafy.new(parts[0])
	best_audio = video.getbestaudio()
	title = title_except(parts[1], articles)
	file_save = 'songs/' + title + '.mp3'
	current_file = best_audio.download(file_save)