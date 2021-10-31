def avgImgColor(path):
    from PIL import Image
    import matplotlib.pyplot as plt
    r,g,b = 0, 0, 0

    img = Image.open(path)
    img = img.convert("RGB")
    pixels = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r += pixels[x,y][0]/255
            g += pixels[x,y][1]/255
            b += pixels[x,y][2]/255
    
    r /= img.size[0] * img.size[1]
    g /= img.size[0] * img.size[1]
    b /= img.size[0] * img.size[1]

    return (r, g, b)

