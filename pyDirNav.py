import os
counter = 0
#for dirname, dirnames, filenames in os.walk("/storage/Music/iTunes Music/"):
for dirname, dirnames, filenames in os.walk("/home/maynard/source/pyD3/"):
	for filename in filenames:
		if (".m4a" in filename):
			print  os.path.join(dirname,filename)
			counter += 1

print "Found " + str(counter) + " Tracks"
