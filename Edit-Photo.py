from PIL import Image
import PIL
print("Welcome to Joseph's Photo Editor!")
photo = input("Please enter the file path of the photo you would like to edit:")
pic = Image.open(photo)
print("This is the photo you've selected.")
crop = input("Would you like to crop?(y/n)")
if crop == "y":
    box = input("Input the new coordinates of your photo:(200 100 200 300)")
    box = box.split()
    box = (int(box[0]), int(box[1]), int(box[2]), int(box[3]))
    pic = pic.crop(box)
    pic.show()
recolour = input("Would you like to recolour?(y/n)")
if recolour == "y":
    colour = input("Input the new R G B of the photo:(10 200 90)")
    colour = colour.split()
    r = int(colour[0])
    g = int(colour[1])
    b = int(colour[2])
    pic = Image.merge("RGB", (r, g, b))
    pic.show()
