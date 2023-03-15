from pytube import YouTube
from sys import argv
link = argv[1]
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Author: ", yt.author)
print("Duration: ", float(yt.length / 60))
print("Description: ", yt.description)
print("Publish_date: ", yt.publish_date)
# yd = yt.streams.get_highest_resolution()
# yd.download('/Users/MY PC/Music/pytube/downloaded')


