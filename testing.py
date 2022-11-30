from PIL import Image

im = Image.open("fire.jpg")
R, G, B = 0, 1, 2
source = im.split()
out = source[R].point(lambda i: i < 140 and 180)
out.show()
