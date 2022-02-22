from PIL import Image, ImageDraw, ImageFont

header_text = "Why NOT BOTH!"
background_image = './images/hungry_man_background.jpg'
image_1 = './images/chicken-legs.png'
image_2 = './images/burger.png'
image_3 = './images/chicken-wings.png'

# Open the background image and rest of images to be synthesis.
background = Image.open(background_image)
img1 = Image.open(image_1)
img2 = Image.open(image_2)
img3 = Image.open(image_3)

# Perform images synthesis into background image.
background.paste(img1, (10,0), mask = img1)
background.paste(img2, (350,350), mask = img2)
background.paste(img3, (700,0), mask = img3)

# Save the image after images synthesis.
background.save('./output_images/output.png',"PNG")

# Add header text to the image.
output_image = Image.open("./output_images/output.png")
output_image_editable = ImageDraw.Draw(output_image)
# Define the font type and size.
font = ImageFont.truetype(r'./font/arial.ttf', 80)
# Define the position of the header text, header text, header text color, and the font type and size.
output_image_editable.text((220, 580), header_text, (0, 0, 0), font=font)
# Save the final image after adding header text.
output_image.save('./output_images/output_final.png')

# Display the synthesis image.
#output_image.show()

# Close all images after synthesis.
background.close()
img1.close()
img2.close()
img3.close()
output_image.close()

