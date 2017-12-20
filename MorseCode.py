from PIL import Image

white = (255,255,255)
black = (0,0,0)
countwhite = 0
countblack = 0

#=================================
# number of frame between 2 words
SPACE = 5
# number of frame to know . and _
# if number <= DOTANDDASH: .
# if number > DOTANDDASH: _
DOTANDDASH = 10
#=================================

for x in xrange(48,22384):
	img = Image.open("Output/scene" + str(x) + ".jpg")
	r,g,b = img.getpixel((20,20))
	if (r,g,b)== black: #black
		countblack = countblack + 1
		if countwhite >= SPACE:
			print "/",
		# if countwhite != 0:
		# 	print "[%d]" % countwhite,
		countwhite = 0
	else: #white
		countwhite = countwhite + 1
		if countblack != 0:
			if countblack <= DOTANDDASH:
				print ".",
				# print "- %d" % countblack,
			if countblack > DOTANDDASH:
				print "-",
				# print "_ %d" % countblack,
		countblack = 0
	img.close()