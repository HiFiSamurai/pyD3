import os,sys
from mutagen.mp3 import MP3,HeaderNotFoundError
from mutagen.id3 import TPE2
try:
	path=sys.argv[1]
	print path
except IndexError:
	print "Usage: artistRectifier.py <dir to scan>"
	sys.exit()

counter = 0
for dirname, dirnames, filenames in os.walk(path):	
	for filename in filenames:
		if (".mp3" in filename):
			try:
				audio = MP3(os.path.join(dirname,filename))
				artist = audio["TPE1"].text
				try:
					albumArtist = audio["TPE2"]
				except KeyError:	
					# song has no album artist assigned, use the artist value
					audio.tags.add(TPE2(3,artist))
					audio.tags.save()
					counter+=1
			except KeyError:
				print "No Artist Name: " + filename
			except HeaderNotFoundError:
				print "MPEG Error: " + filename
print "Updated " + str(counter) + " Tracks"
