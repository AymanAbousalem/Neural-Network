from PIL import Image

image = Image.open('Neural-Network\ipadwritten4.png')

new_image = image.resize((24,24))
new_image.save('ipadwritten4_resized.png')

new_image.show()