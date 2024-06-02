from PIL import Image

image = Image.open('Images\ipad_ss_5.JPG')

new_image = image.resize((28,28))
new_image.save('ipad_ss_5_resized.png')

new_image.show()