
"""

def generate_id_card(member):
    template_path = os.path.join(settings.BASE_DIR, 'templates/id_template.png')
    
    # ✅ Create template if it doesn't exist
    if not os.path.exists(template_path):
        base = create_default_id_template(template_path)
    else:
        base = Image.open(template_path).convert('RGB')
    
    draw = ImageDraw.Draw(base)
    
    # ✅ Try to load custom font, fallback to default
    font_path = os.path.join(settings.BASE_DIR, 'fonts/arial.ttf')
    try:
        font = ImageFont.truetype(font_path, 24)
    except OSError:
        # Fallback to default PIL font
        font = ImageFont.load_default()
    
    # Draw member info
    draw.text((200, 50), member.full_name, fill='black', font=font)
    draw.text((200, 100), member.membership_id, fill='black', font=font)
    draw.text((200, 130), f"Role: {member.role.title()}", fill='black', font=font)
    draw.text((200, 170), f"Phone: {member.mobile_no}", fill='black', font=font)
    
    # Paste photo if available
    if member.photo and os.path.exists(member.photo.path):
        try:
            photo = Image.open(member.photo.path).resize((120, 120))
            base.paste(photo, (50, 50))
        except Exception:
            pass  # Skip photo if there's an error
    
    # Ensure output directory exists
    output_dir = os.path.join(settings.MEDIA_ROOT, 'id_cards')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the generated ID card
    filename = f"{member.membership_id}.png"
    path = os.path.join(output_dir, filename)
    base.save(path)
    
    return f"id_cards/{filename}"
  """



    
    # Ensure template directory exists
   """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Create a white image
    img = Image.new('RGB', (400, 250), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw a border
    draw.rectangle([10, 10, 390, 240], outline='blue', width=3)
    
    # Draw header
    draw.rectangle([10, 10, 390, 40], fill='blue')
    try:
        header_font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts/arial.ttf'), 16)
        draw.text((200, 25), "LEADERSHIP BRIDGE", fill='white', font=header_font, anchor='mm')
    except:
        draw.text((200, 25), "LEADERSHIP BRIDGE", fill='white', anchor='mm')
    
    # Draw photo placeholder box
    draw.rectangle([50, 50, 170, 170], outline='gray', width=2)
    try:
        placeholder_font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts/arial.ttf'), 10)
        draw.text((110, 110), "PHOTO", fill='gray', font=placeholder_font, anchor='mm')
    except:
        draw.text((110, 110), "PHOTO", fill='gray', anchor='mm')
    
    # Save and return
    img.save(save_path)
    return img.convert('RGB')
    """


"""
def generate_id_card(member):
    # Open template
    base = Image.open(os.path.join(settings.BASE_DIR, 'templates/id_template.png')).convert('RGB')
    
    # CREATE THE DRAW OBJECT 
    draw = ImageDraw.Draw(base)
    
    # Load font
    font_path = os.path.join(settings.BASE_DIR, 'fonts/arial.ttf')
    font = ImageFont.truetype(font_path, 24)
    
    # Draw text
    draw.text((200, 50), member.full_name, fill='black', font=font)
    draw.text((200, 100), member.membership_id, fill='black', font=font)
    draw.text((200, 130), f"Role: {member.role.title()}", fill='black', font=font)
    draw.text((200, 170), f"Phone: {member.mobile_no}", fill='black', font=font)
    
    # Paste photo (with error handling in case photo is missing)
    if member.photo and os.path.exists(member.photo.path):
        photo = Image.open(member.photo.path).resize((120, 120))
        # Add comma between photo and coordinates
        base.paste(photo, (50, 50))
    
    # Ensure output directory exists
    output_dir = os.path.join(settings.MEDIA_ROOT, 'id_cards')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the image
    filename = f"{member.membership_id}.png"
    path = os.path.join(output_dir, filename)
    base.save(path)
    
    # Return relative path for Django to store
    return f"id_cards/{filename}"

"""


"""


def generate_id_card(member):
	base = Image.open(os.path.join(settings.BASE_DIR, 'templates/id_template.png')).convert('RGB')
	font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts/arial.ttf'), 24)
	draw.text((200, 50), member.full_name, fill='black', font=font)
	draw.text((200, 100), member.membership_id, fill='black', font=font)
	#draw.text((200, 50), member.full_name, fill='black', font=font)
	draw.text((200, 130), f"Role: {member.role.title()}", fill='black', font=font)
	draw.text((200, 170), f"Phone: {member.mobile_no}", fill='black', font=font)
	photo = Image.open(member.photo.path).resize((120, 120))
	base.paste(photo (50, 50))

	path = os.path.join(settings.MEDIA_ROOT, f"id_cards/{member.membership_id}.png")
	base.save(path)

	return f"id_cards/{member.membership_id}.png"

"""
