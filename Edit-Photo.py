from PIL import Image
import sys, os

print("Welcome to Joseph's Photo Editor!")
photo = input("Please enter the file path of the photo you would like to edit:")
pic = Image.open(photo)
while True:
    print("--Main Menu--")
    menu = input(
        "Please input the edit you would like to make. Convert file to jpg(j), crop(c), recolour(r), rotate(d), resize(s), pixels(p), or exposure(e).")
    if menu == "j":
        for pic in sys.argv[1:]:
            f, e = os.path.splitext(pic)
            pic = f + ".jpg"
            if pic != pic:
                try:
                    with Image.open(pic) as pic:
                        pic.save(pic)
                except OSError:
                    print("cannot convert", pic)
    elif menu == "c":
        box = input("Input the new coordinates of your photo:(100 100 300 300)")
        box = box.split()
        box = (int(box[0]), int(box[1]), int(box[2]), int(box[3]))
        pic = pic.crop(box)
    elif menu == "r":
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
        #  colour = colour.split()r = int(colour[0])g = int(colour[1])b = int(colour[2])pic.show()
    elif menu == "d":
        degrees = input("Please input how many degrees you would like to rotate your photo counter-clockwise:")
        pic = pic.rotate(int(degrees))
    elif menu == "e":
        high = input("Would you like high exposure or low?(h/l)")
        if high == "h":
            pic = pic.point(lambda i: i * 3)
        if high == "l":
            pic = pic.point(lambda i: i * 0.2)
    elif menu == "s":
        size = input("Input the new size(100 100):")
        size = size.split()
        pic = pic.resize((int(size[0]), int(size[1])))
    elif menu == "p":
        pixel = input("Input the ratio of pixels you want to black(2):")
        double = int(input("Select the number of pixels you want the ratio to make black(5):"))
        pixels = pic.load()
        for i in range(0, pic.size[0], int(pixel)):  # for every pixel:
            for j in range(0, pic.size[1], int(pixel)):
                for k in range(0, double):
                    if i + double > pic.size[0]:
                        continue
                    pixels[i + k, j] = (0, 0, 0)
    else:
        break
    pic.show()
