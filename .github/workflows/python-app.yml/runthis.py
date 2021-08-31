import sys 
from PIL import Image
import os

print("Enter Your Path : ...")
a = input("> ")
width = input("Type Your Height Size : ")
height = input("Type Your Height Size : ")

print("Open Your Path...")

os.system("ascii_image.txt")

#################################
image_path = sys.argv[0]
img = Image.open(a)#open jpg file 
width, height = img.size
aspect_ratio = height/width/2
new_width = width
new_height = height
img = img.resize((new_width,int(new_height)))
img = img.convert('L')
pixels = img.getdata()
chars = ["~","!","@","#","$","%","^","&","*","(",")","-","+","=","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","<",">",",",".","?","/","_","1","2","3","4","5","6","7","8","9","0"]
new_pixels = [chars[pixel//25] for pixel in pixels]

new_pixels = ''.join(new_pixels)
new_pixels_count= len(new_pixels)
ascii_image = [new_pixels[index:index+new_width] for index in range(0,new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
with open("ascii_image.txt",'w') as f:
       f.write(ascii_image)

print(ascii_image)
