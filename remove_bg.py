from PIL import Image

image = Image.open("e.NOVA Aero-transparent.png")
image = image.convert("RGBA")
pixels = image.getdata()
background_colors = [(255, 255, 255, 255), (0, 0, 0, 255)]

new_pixels = []
for pixel in pixels:
    if pixel in background_colors:
        new_pixels.append((0, 0, 0, 0))
    else:
        new_pixels.append(pixel)

image.putdata(new_pixels)
image.save("eNOVA_removed_background.png", "PNG")
