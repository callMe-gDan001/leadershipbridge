
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







"""
def generate_id_card(member):
    template_path = os.path.join(settings.BASE_DIR, 'templates/id_template.png')
    
    # Create premium template if it doesn't exist
    if not os.path.exists(template_path):
        base = create_premium_id_template(template_path)
    else:
        base = Image.open(template_path).convert('RGB')
    
    draw = ImageDraw.Draw(base)
    
    # Load fonts with fallbacks
    bold_font = load_font(28, bold=True)
    regular_font = load_font(20)
    small_font = load_font(16)
    tiny_font = load_font(12)
    
    # ✅ Draw member info with premium styling
    draw.text((220, 70), member.full_name.upper(), fill='#1a1a2e', font=bold_font)
    
    # Membership ID with background badge
    id_text = f"ID: {member.membership_id}"
    id_width = draw.textlength(id_text, font=small_font)
    draw.rounded_rectangle([(220, 110), (220 + id_width + 20, 135)], 
                          radius=8, fill='#16213e', outline='#0f3460')
    draw.text((230, 115), member.membership_id, fill='white', font=small_font)
    
    # Role with colored badge
    role_color = get_role_color(member.role)
    draw.rounded_rectangle([(220, 145), (340, 170)], radius=10, fill=role_color)
    draw.text((230, 150), member.role.upper(), fill='white', font=tiny_font)
    
    # Phone with icon
    draw.text((220, 185), f"📞 {member.mobile_no}", fill='#4a4a68', font=regular_font)
    
    # Validity date
    valid_until = datetime.now().year + 1
    draw.text((220, 215), f"Valid Until: Dec {valid_until}", fill='#6a6a8a', font=tiny_font)
    
    # Paste photo with premium styling
    if member.photo and os.path.exists(member.photo.path):
        try:
            photo = Image.open(member.photo.path)
            # Resize and crop to circle
            photo = photo.resize((140, 140), Image.Resampling.LANCZOS)
            
            # Create circular mask
            mask = Image.new('L', (140, 140), 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse([0, 0, 140, 140], fill=255)
            
            # Apply mask and add border
            photo.putalpha(mask)
            border = Image.new('RGBA', (146, 146), (255, 255, 255, 255))
            border.paste(photo, (3, 3))
            
            # Add to base image
            base.paste(border, (52, 60), border)
            
            # Add shadow effect
            shadow = Image.new('RGBA', (140, 140), (0, 0, 0, 40))
            shadow.putalpha(mask)
            base.paste(shadow, (55, 63), shadow)
            
        except Exception as e:
            print(f"Photo error: {e}")
            pass
    
    # Save the generated ID card
    output_dir = os.path.join(settings.MEDIA_ROOT, 'id_cards')
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{member.membership_id}.png"
    path = os.path.join(output_dir, filename)
    base.save(path, quality=95)
    
    return f"id_cards/{filename}"


def create_premium_id_template(save_path):
    """Creates a premium, modern ID card template"""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Create base image (400x250)
    img = Image.new('RGBA', (400, 250), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Gradient background (top to bottom)
    for y in range(250):
        if y < 70:
            # Dark blue header
            color = interpolate_color((22, 33, 62), (15, 52, 96), y / 70)
        else:
            # Light gray body
            color = (245, 247, 250)
        draw.line([(0, y), (400, y)], fill=color)
    
    # Header section with gradient
    draw.rectangle([0, 0, 400, 70], fill=(22, 33, 62))
    
    # Decorative curved line in header
    draw.arc([300, -50, 450, 90], 0, 180, fill=(230, 196, 88), width=3)
    
    # Organization name
    try:
        title_font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts/arialbd.ttf'), 20)
    except:
        title_font = ImageFont.load_default()
    
    draw.text((200, 25), "LEADERSHIP BRIDGE", fill='white', font=title_font, anchor='mm')
    
    # Tagline
    try:
        tagline_font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts/arial.ttf'), 10)
    except:
        tagline_font = ImageFont.load_default()
    draw.text((200, 48), "Empowering Leaders, Transforming Communities", fill='#e8c558', 
              font=tagline_font, anchor='mm')
    
    # Left decorative element
    draw.rectangle([10, 10, 15, 60], fill='#e8c558')
    
    # Right decorative element
    draw.rectangle([385, 10, 390, 60], fill='#e8c558')
    
    # Photo placeholder area with border
    draw.rounded_rectangle([50, 58, 190, 198], radius=10, fill='white', outline='#16213e', width=2)
    
    # Photo placeholder text
    draw.text((120, 120), "PHOTO", fill='#a0a0a0', font=tagline_font, anchor='mm')
    draw.text((120, 135), "AREA", fill='#a0a0a0', font=tagline_font, anchor='mm')
    
    # Bottom decorative stripe
    draw.rectangle([0, 245, 400, 250], fill='#16213e')
    
    # Security pattern (subtle diagonal lines)
    for i in range(0, 400, 40):
        draw.line([(i, 75), (i+50, 240)], fill=(230, 230, 235), width=1)
    
    # Convert to RGB and save
    img_rgb = Image.new('RGB', (400, 250), (255, 255, 255))
    img_rgb.paste(img, mask=img.split()[3])
    img_rgb.save(save_path)
    
    return img_rgb.convert('RGB')


def load_font(size, bold=False):
    """Load font with fallback"""
    try:
        font_name = 'arialbd.ttf' if bold else 'arial.ttf'
        return ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts', font_name), size)
    except:
        return ImageFont.load_default()


def get_role_color(role):
    """Return color based on role"""
    colors = {
        'Volunteer': '#27ae60',      # Green
        'Community Leader': '#2980b9', # Blue
        'Donor': '#e8c558',          # Gold
        'Trainee': '#8e44ad',        # Purple
    }
    return colors.get(role, '#34495e')


def interpolate_color(color1, color2, factor):
    """Interpolate between two RGB colors"""
    return tuple(int(c1 + (c2 - c1) * factor) for c1, c2 in zip(color1, color2))




def generate_id_card(member):
    template_path = os.path.join(settings.BASE_DIR, 'templates/id_template.png')
    
    # Create premium template if it doesn't exist
    if not os.path.exists(template_path):
        base = create_visa_style_template(template_path)
    else:
        base = Image.open(template_path).convert('RGB')
    
    draw = ImageDraw.Draw(base)
    
    # Load fonts
    bold_font = load_font(24, bold=True)
    regular_font = load_font(18)
    small_font = load_font(14)
    tiny_font = load_font(11)
    
    # ✅ Draw member info with proper positioning
    # Full Name (with truncation if too long)
    name = member.full_name.upper()
    if len(name) > 22:
        name = name[:20] + "..."
    draw.text((210, 65), name, fill='#1a3a3a', font=bold_font)
    
    # Membership ID in a styled box
    id_text = member.membership_id
    draw.rounded_rectangle([(210, 95), (330, 118)], radius=5, fill='#0d7377', outline='#14919b')
    draw.text((215, 100), id_text, fill='white', font=small_font)
    
    # Role badge with color
    role_color = get_role_color(member.role)
    draw.rounded_rectangle([(210, 125), (310, 148)], radius=8, fill=role_color)
    draw.text((215, 130), member.role.upper(), fill='white', font=tiny_font)
    
    # Phone number (with truncation if too long)
    phone = member.mobile_no
    if len(phone) > 15:
        phone = phone[:13] + "..."
    draw.text((210, 160), f"☎ {phone}", fill='#2c5f5f', font=regular_font)
    
    # Validity date
    valid_until = datetime.now().year + 1
    draw.text((210, 185), f"Valid: Dec {valid_until}", fill='#5a8f8f', font=tiny_font)
    
    # ✅ Paste photo properly
    if member.photo and os.path.exists(member.photo.path):
        try:
            photo = Image.open(member.photo.path).convert('RGBA')
            # Resize photo
            photo = photo.resize((140, 140), Image.Resampling.LANCZOS)
            
            # Create circular crop
            mask = Image.new('L', (140, 140), 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse([0, 0, 140, 140], fill=255)
            
            # Apply circular mask
            photo.putalpha(mask)
            
            # Add white border
            bordered = Image.new('RGBA', (146, 146), (255, 255, 255, 255))
            bordered.paste(photo, (3, 3))
            
            # Add subtle shadow
            shadow = Image.new('RGBA', (140, 140), (0, 0, 0, 50))
            shadow.putalpha(mask)
            base.paste(shadow, (57, 63), shadow)
            
            # Paste on base
            base.paste(bordered, (52, 60), bordered)
            
        except Exception as e:
            print(f"Photo error: {e}")
            # Draw placeholder if photo fails
            draw.ellipse([55, 63, 185, 193], outline='#14919b', width=3)
            draw.text((120, 120), "NO PHOTO", fill='#999', font=tiny_font, anchor='mm')
    else:
        # Draw placeholder circle
        draw.ellipse([55, 63, 185, 193], outline='#14919b', width=3, fill='#f0f9f9')
        draw.text((120, 120), "NO PHOTO", fill='#999', font=tiny_font, anchor='mm')
    
    # Save the generated ID card
    output_dir = os.path.join(settings.MEDIA_ROOT, 'id_cards')
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{member.membership_id}.png"
    path = os.path.join(output_dir, filename)
    base.save(path, quality=95)
    
    return f"id_cards/{filename}"


def create_visa_style_template(save_path):
    """Creates a professional visa-style ID card with teal/green pattern"""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Create base image (400x250)
    img = Image.new('RGB', (400, 250), '#e8f4f4')
    draw = ImageDraw.Draw(img)
    
    # ✅ Create beautiful teal/green gradient background
    for y in range(250):
        if y < 65:
            # Dark teal header
            r = int(20 + (32 - 20) * (y / 65))
            g = int(100 + (128 - 100) * (y / 65))
            b = int(100 + (128 - 100) * (y / 65))
            color = (r, g, b)
        else:
            # Light teal/mint body with subtle pattern
            pattern = 240 if (y // 5) % 2 == 0 else 245
            color = (pattern, 250, 248)
        draw.line([(0, y), (400, y)], fill=color)
    
    # ✅ Header with gradient
    draw.rectangle([0, 0, 400, 65], fill='#14919b')
    
    # Decorative wave pattern in header
    for x in range(0, 400, 20):
        draw.arc([x-10, -20, x+30, 40], 0, 180, fill='#0d7377', width=2)
    
    # Organization name
    title_font = load_font(20, bold=True)
    draw.text((200, 22), "LEADERSHIP BRIDGE", fill='white', font=title_font, anchor='mm')
    
    # Tagline
    tagline_font = load_font(9)
    draw.text((200, 42), "Empowering Leaders, Transforming Communities", fill='#a8e6e6', 
              font=tagline_font, anchor='mm')
    
    # ✅ Security pattern (like real ID cards)
    # Diagonal lines
    for i in range(-200, 600, 30):
        draw.line([(i, 70), (i+150, 250)], fill='#d4f0f0', width=1)
    
    # Dotted pattern
    for x in range(20, 400, 40):
        for y in range(80, 240, 30):
            draw.ellipse([x-1, y-1, x+1, y+1], fill='#c4e8e8')
    
    # Geometric shapes (security feature)
    draw.rectangle([350, 75, 390, 115], outline='#14919b', width=1)
    draw.polygon([(370, 120), (360, 140), (380, 140)], outline='#0d7377', width=1)
    draw.ellipse([355, 145, 385, 175], outline='#14919b', width=1)
    
    # Left decorative stripe
    draw.rectangle([0, 65, 6, 250], fill='#0d7377')
    
    # Right decorative stripe
    draw.rectangle([394, 65, 400, 250], fill='#0d7377')
    
    # Photo area placeholder with border
    draw.rounded_rectangle([50, 60, 190, 200], radius=8, fill='white', outline='#14919b', width=2)
    
    # Inner photo border
    draw.rounded_rectangle([54, 64, 186, 196], radius=6, fill='#f8ffff', outline='#d4f0f0', width=1)
    
    # Bottom security strip
    draw.rectangle([0, 245, 400, 250], fill='#0d7377')
    
    # Microtext (security feature)
    micro_font = load_font(6)
    draw.text((10, 247), "LB" * 50, fill='#5a8f8f', font=micro_font)
    
    # Corner decorations
    draw.rectangle([8, 8, 18, 18], fill='#0d7377')
    draw.rectangle([382, 8, 392, 18], fill='#0d7377')
    draw.rectangle([8, 47, 18, 57], fill='#0d7377')
    draw.rectangle([382, 47, 392, 57], fill='#0d7377')
    
    # Save template
    img.save(save_path)
    
    return img.convert('RGB')


def load_font(size, bold=False):
    """Load font with fallback"""
    try:
        font_name = 'arialbd.ttf' if bold else 'arial.ttf'
        font_path = os.path.join(settings.BASE_DIR, 'fonts', font_name)
        return ImageFont.truetype(font_path, size)
    except:
        try:
            # Try Windows fonts
            if bold:
                return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size)
            else:
                return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)
        except:
            return ImageFont.load_default()


def get_role_color(role):
    """Return color based on role"""
    colors = {
        'Volunteer': '#27ae60',           # Green
        'Community Leader': '#2980b9',    # Blue
        'Donor': '#d4af37',               # Gold
        'Trainee': '#8e44ad',             # Purple
    }
    return colors.get(role, '#14919b')    # Teal default


