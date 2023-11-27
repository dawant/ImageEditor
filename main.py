from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'images'
pathOut = 'edited'

print("Welcome to the image editor using Pillow library!")
print("What would you like to do with your photos located in " +path + "?" )
print(" ")
print("1.Sharpen")
print("2. Blur")
print("3. Contour")
print("4. Detail")
print("5. Emboss")

input = int(input("Type a number: "))
numbers = range(6)

if input == 1:
    for name in os.listdir(path):
        img = Image.open(f"{path}/{name}")

        edit = img.filter(ImageFilter.SHARPEN)

        edit.save(f"{pathOut}/{name}_edited.jpg")
        print("Sharpen has been applied to the pictures in " +path +".")

elif input == 2:
    for name in os.listdir(path):
        img = Image.open(f"{path}/{name}")

        edit = img.filter(ImageFilter.BLUR)

        edit.save(f"{pathOut}/{name}_edited.jpg")
        print("Blur has been applied to the pictures in " +path +".")

elif input == 3:
    for name in os.listdir(path):
        img = Image.open(f"{path}/{name}")

        edit = img.filter(ImageFilter.CONTOUR)

        edit.save(f"{pathOut}/{name}_edited.jpg")
        print("Contour has been applied to the pictures in " + path + ".")

elif input == 4:
    for name in os.listdir(path):
        img = Image.open(f"{path}/{name}")

        edit = img.filter(ImageFilter.CONTOUR)

        edit.save(f"{pathOut}/{name}_edited.jpg")
        print("Detail has been applied to the pictures in " + path + ".")

elif input == 5:
    for name in os.listdir(path):
        img = Image.open(f"{path}/{name}")

        edit = img.filter(ImageFilter.CONTOUR)

        edit.save(f"{pathOut}/{name}_edited.jpg")
        print("Emboss has been applied to the pictures in " + path + ".")

if input not in numbers:
    print("Choose a number from 1 to 5.")














