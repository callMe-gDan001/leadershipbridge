from PIL import Image, ImageDraw, ImageFront
from django.conf import settings
import os



def generate_id_card(member):
	base = Image.open(os.path.join(settings.BASE_DIR, 'templates/id_template.png')).convert('RGB')
	font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts/arial.ttf'), 24)
	draw.text((200, 50), member.full_name, fill='black', font=font)
	draw.text((200, 100), member.membership_id, fill='black', font=font)
	draw.text((200, 50), member.full_name, fill='black', font=font)
	photo = Image.open(member.photo.path).resize((120, 120))
	base.paste(photo (50, 50))

	path = os.path.join(settings.MEDIA_ROOT, f"id_cards/{member.membership_id}.png")
	base.save(path)

	return f"id_cards/{member.membership_id}.png"
