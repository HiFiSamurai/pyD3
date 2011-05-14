import id3reader

# Construct a reader from a file or filename.
id3r = id3reader.Reader('/home/maynard/source/testSong.mp3')

# Ask the reader for ID3 values:
print "Artist: " + id3r.getValue('TP1')

# Can't write to tags...ARGHH!
#if (id3r.getValue('TP2') is None):
#	id3r.setValue('TP2',id3r.getValue('TP1'))

print "Album Artist: " + id3r.getValue('TP2')
