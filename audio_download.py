import pafy

url = "https://www.youtube.com/watch?v=gE68v9QotNA" #Audio for Soulja Boy - Crank That
video = pafy.new(url)
best_audio = video.getbestaudio()
current_file = best_audio.download("CurrentSong.mp3")