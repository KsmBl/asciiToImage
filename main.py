#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys
import os

def helpText():
	return """
	pipe some stdin into this program and it outputs an image.
	Example:
	$ cat ./asciiCat | ./main.py

	-o	defines output file and type
		Example:
			$cat ./asciiCat | ./main.py -o "catImage.jpg"

	-s	defines font size / resolution. Higher fontsize results in a higher res image
		Example:
			$cat ./asciiCat | ./main.py -s 34

	-fc	defines font color. Use color words or hexcodes
		Example:
			$cat ./asciiCat | ./main.py -fc "#f0a54a"

	-bc	defines background color. Use color words or hexcodes
		Example:
			$cat ./asciiCat | ./main.py -bc "#000000"

	-h / --help
		shows this help page
	"""

args = sys.argv

outputFile="output.png"
fontSize = 14
fontColor = "white"
backgroundColor = "black"

for i in range(len(args)):
	if args[i] == "-o" and i+1 < len(args):
		outputFile = args[i + 1]
	elif args[i] == "-s" and i+1 < len(args):
		fontSize = int(args[i + 1])
	elif args[i] == "-fc" and i+1 < len(args):
		fontColor = str(args[i + 1])
	elif args[i] == "-bc" and i+1 < len(args):
		backgroundColor = str(args[i + 1])
	elif args[i] == "--help" or args[i] == "-h":
		print(helpText())
		sys.exit(1)

asciiInput = sys.stdin.read()

lines = asciiInput.splitlines()

fontPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Anonymous.ttf")
font = ImageFont.truetype(fontPath, fontSize)

charWidth = font.getlength("A")
ascent, descent = font.getmetrics()
lineHeight = (ascent + descent)

imgWidth = int(charWidth * max(len(line) for line in lines))
imgHeight = lineHeight * len(lines)

image = Image.new("RGB", (imgWidth, imgHeight), color=backgroundColor)
draw = ImageDraw.Draw(image)

for i, line in enumerate(lines):
	draw.text((0, i * lineHeight), line, fill=fontColor, font=font)

image.save(outputFile)
print(f"saved as {outputFile}")
