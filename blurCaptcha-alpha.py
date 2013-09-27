#author anirudh duggal anirudhduggal@gmail.com & prajwalpanchmahalkar@gmail.com
import random
import Tkinter
from Tkinter import *
from PIL import Image, ImageTk, ImageChops, ImageOps, ImageColor, ImageDraw, ImageFont, ImageFilter
from os import urandom
from itertools import islice, imap, repeat
import string
from random import choice
#to randomize
imageAngle=20
fontSize=0
x1=0
y1=0

def rand_string(length=5):
        chars = set(string.ascii_uppercase + string.digits +string.ascii_lowercase)
        char_gen = (c for c in imap(urandom, repeat(1)) if c in chars)
        return ''.join(islice(char_gen, None, length))

def randomizeComponents():
	global imageAngle, fontSize
	imageAngle = random.randint(0,1)
	fontSize = random.randint(20, 66)

#to randomize the coordinates of various shapes
def randomizeCoordinates():
        global x1,y1,filenaemsavc
        x1 = random.randint(50,100)
        y1 = random.randint(30,90)
        filenaemsavc = rand_string(3)
        

def makeImage(inputString,backgroundColor,fontSize):
        fontlist= ["Verdana.ttf","Corbel.ttf","Terminal.ttf"]
        #change the font size to int
        fontpath="C:\\Windows\\Fonts\\"+random.choice(fontlist)
        fontSize = int(fontSize)	
        font = ImageFont.truetype(fontpath,fontSize)
        fontImage = Image.new("RGBA",(200,113),backgroundColor)
        drawObject = ImageDraw.Draw(fontImage)
        colorlist=["#FF0000","#0000A0","#000000","#008000"]
        textcolor=random.choice(colorlist)
        drawObject.text((40,40),inputString,textcolor,font=font)
        

        for i in range(0,100):
                x1 = random.randint(0,200)
                y1 = random.randint(0,113)
                x2 = random.randint(0,200)
                y2 = random.randint(0,200)
                startAngle= random.randint(0,360)
                endAngle = random.randint(0,360)
                color= ('#16DA51','#341ED7','#C91616')
                
                drawObject.chord((x1,y1,x2,y2),0,255,fill=None,outline=choice(color))
                drawObject.arc((x1,y1,x2,y2),startAngle,endAngle,fill=choice(color))
        fontImage = fontImage.rotate(imageAngle)
        #commented line to remove blurring of whole image
        fontImage =fontImage.filter(ImageFilter.BLUR)
        fontImage.save(filenaemsavc+".jpg","JPEG")
        #open image and convert to byte format
        im = Image.open(filenaemsavc+'.jpg')
        root = Tkinter.Tk()
        tkimage = ImageTk.PhotoImage(im)
        Tkinter.Label(root, image=tkimage).pack(side=TOP,padx=10,pady=10)
        Entry(root, width=20).pack(side=TOP,padx=10,pady=10)
        Button(root, text='submit').pack(padx=10)
        root.mainloop()
randomizeComponents()
randomizeCoordinates()
makeImage(rand_string(),"#FFFFFF",fontSize)
