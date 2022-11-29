from PIL import Image
import sys, os
print("Welcome to Joseph's Photo Editor!")
photo = input("Please enter the file path of the photo you would like to edit:")
pic = Image.open(photo)
file = input("Would you like to change the file type to jpg?(y/n)")
if file == "y":
    for pic in sys.argv[1:]:
        f, e = os.path.splitext(pic)
        pic = f + ".jpg"
        if pic != pic:
            try:
                with Image.open(pic) as pic:
                    pic.save(pic)
            except OSError:
                print("cannot convert", pic)
crop = input("Would you like to crop?(y/n)")
if crop == "y":
    box = input("Input the new coordinates of your photo:(100 100 300 300)")
    box = box.split()
    box = (int(box[0]), int(box[1]), int(box[2]), int(box[3]))
    pic = pic.crop(box)
    pic.show()
recolour = input("Would you like to recolour?(y/n)")
if recolour == "y":
    colour = input("Input the new recolour of the photo:(blue, green, red, gray)")
    r, g, b = pic.split()
    if colour == "blue":
        pic = Image.merge("RGB", (b, g, r))
    if colour == "green":
        pic = Image.merge("RGB", (b, r, g))
    if colour == "red":
        pic = Image.merge("RGB", (r, b, g))
    if colour == "gray":
        pic = pic.convert("L")
    pic.show()
    #  colour = colour.split()r = int(colour[0])g = int(colour[1])b = int(colour[2])pic.show()
rotate = input("Would you like to rotate?(y/n)")
if rotate == "y":
    degrees = input("Please input how many degrees you would like to rotate your photo counter-clockwise:")
    pic = pic.rotate(int(degrees))
    pic.show()
exposure = input("Would you like to change the exposure on your photo?(y/n)")
if exposure == "y":
    high = input("Would you like high exposure or low?(h/l)")
    if high == "h":
        pic = pic.point(lambda i: i * 3)
    if high == "l":
        pic = pic.point(lambda i: i * 0.2)
    pic.show()