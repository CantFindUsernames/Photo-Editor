from PIL import Image
img = Image.open("horse.jpg")
pixels = img.load() # create the pixel map

for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        for k in range(0, 100):
            if pixels[i, j] == (0, 255, k):
                # change to black if not red
                pixels[i, j] = (0, 0, 255)
img.show()