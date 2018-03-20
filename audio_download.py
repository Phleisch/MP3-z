import pafy

url = "https://www.youtube.com/watch?v=gE68v9QotNA" #Audio for Soulja Boy - Crank That
video = pafy.new(url)
audiostreams = video.audiostreams
audiostreams[0].download()