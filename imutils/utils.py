def printrgb(im, x, y):
    (b, g, r) = im[y, x]
    print("Pixel at ({x}, {y}) - Red: {r}, Green: {g}, Blue: {b}".format(x=x, y=y, r=r, g=g, b=b))

