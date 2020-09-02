#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime
import qrcode

image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)

os.system("Create ID Card")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# starting position of the message
print('\n\nAll Fields are Mandatory')
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')

(x, y) = (50, 50)
message = raw_input('Enter company name : ')
company = message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)

# add a unique id number
(x, y) = (600, 75)
idno = random.randint(10000000, 90000000)
message = str('ID ' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 250)
message = raw_input('Enter Your Full Name: ')
name = message
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 350)
message = raw_input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)
(x, y) = (250, 350)
message = raw_input('Enter Your Age: ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 450)
message = raw_input('Enter Your Date Of Birth: ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 550)
message = raw_input('Enter Your Blood Group: ')
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 650)
message = raw_input('Enter Your Mobile Number: ')
temp = message
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 750)
message = raw_input('Enter Your Address: ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

image.save(str(name) + '.png')

img = qrcode.make(str(company) + str(idno))  # this info. is added in QR code
img.save(str(idno) + '.bmp')

til = Image.open(name + '.png')
im = Image.open(str(idno) + '.bmp')
til.paste(im, (600, 350))
til.save(name + '.png')

print(('\n\n\nYour ID Card created in file ' + name + '.png'))
eval(raw_input('\n\nPress any key to close...'))
