def avgImgColor(path, accuracy):
    from PIL import Image
    if accuracy > 100:
        print("Accuracy set to above 100%, defaulting to 100%!")
        accuracy = 100
    elif accuracy <=0:
        print("Accuracy set to 0% or smaller, defaulting to 1%!")
        accuracy = 1

    r,g,b = 0, 0, 0

    img = Image.open(path)
    img = img.convert("RGB")
    width = int(img.size[0] * (accuracy / 100))
    height = int(img.size[1] * (accuracy / 100))
    width, height = img.size
    img.thumbnail((width, height), Image.ANTIALIAS)
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r += pixels[x,y][0]/255
            g += pixels[x,y][1]/255
            b += pixels[x,y][2]/255
    
    r /= width * height
    g /= width * height
    b /= width * height

    return (r, g, b)


