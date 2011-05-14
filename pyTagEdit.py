from mutagen.mp3 import MP3
from mutagen.id3 import TPE2
from mutagen.easyid3 import EasyID3

# need to modify to take in command line args, or work on entire folders
audio = MP3('/home/maynard/source/pyD3/testSong.mp3')

artist = audio["TPE1"].text

try:
	print audio["TPE2"]
except KeyError:	# song has no album artist assigned, so use the artist value
	print "BAD"
	audio.tags.add(TPE2(3,artist))
	audio.tags.save()

