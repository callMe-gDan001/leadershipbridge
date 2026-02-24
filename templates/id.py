from PIL import Image, ImageDraw, ImageFont


def create_id_card_image(output_filename='id_card.png'):
	width, height = 1050, 600

	img = Image.new('RGB', (width, height), color=(255, 255, 255))

	# draw border

	draw = ImageDraw.Draw(img)
	draw.rectangle([(30, 30), (width-30, height-30)], outline="black", width=3)

	# Add title(using default font; for custom, load ttf file with ImageFont.truetype)



create_id_card_image()