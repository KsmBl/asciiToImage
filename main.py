#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys
import os

args = sys.argv

outputFile="output.png"
fontSize = 14

for i in range(len(args)):
	if args[i] == "-o" and i+1 < len(args):
		outputFile = args[i + 1]
	elif args[i] == "-s" and i+1 < len(args):
		fontSize = int(args[i + 1])

asciiInput = sys.stdin.read()

lines = asciiInput.splitlines()

fontPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Anonymous.ttf")
font = ImageFont.truetype(fontPath, fontSize)

char_width = font.getlength("A")
ascent, descent = font.getmetrics()
lineHeight = (ascent + descent)

imgWidth = int(char_width * max(len(line) for line in lines))
imgHeight = lineHeight * len(lines)

image = Image.new("RGB", (imgWidth, imgHeight), color="black")
draw = ImageDraw.Draw(image)

for i, line in enumerate(lines):
	draw.text((0, i * lineHeight), line, fill="white", font=font)

image.save(outputFile)
print(f"saved as {outputFile}")
