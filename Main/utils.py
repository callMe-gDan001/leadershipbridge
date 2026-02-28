2from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from django.conf import settings
import os
from datetime import datetime
import textwrap




def generate_id_card(member):
    template_path = os.path.join(settings.BASE_DIR, 'templates/id_template.png')
    
    # Create premium template if it doesn't exist
    if not os.path.exists(template_path):
        base = create_premium_3d_template(template_path)
    else:
        base = Image.open(template_path).convert('RGB')
    
    draw = ImageDraw.Draw(base)
    
    # Load fonts
    bold_font = load_font(26, bold=True)
    regular_font = load_font(19)
    small_font = load_font(15)
    tiny_font = load_font(12)
    
    # Draw member info with proper positioning
    # Full Name (with smart truncation)
    name = member.full_name.upper()
    if len(name) > 20:
        name = name[:18] + ".."
    draw.text((215, 68), name, fill='#0d3d3d', font=bold_font)
    
    # Membership ID in 3D-styled box
    id_text = member.membership_id
    draw_3d_box(draw, 210, 98, 335, 122, '#0d7377', '#14919b', '#0a5c5f')
    draw.text((215, 103), id_text, fill='white', font=small_font)
    
    # Role badge with 3D effect
    role_color = get_role_color(member.role)
    role_color_dark = darken_color(role_color, 30)
    draw_3d_box(draw, 210, 128, 315, 152, role_color, role_color_dark, role_color)
    draw.text((215, 133), member.role.upper(), fill='white', font=tiny_font)
    
    # Phone number
    phone = member.mobile_no
    if len(phone) > 14:
        phone = phone[:12] + ".."
    draw.text((215, 165), f"📞 {phone}", fill='#1a5c5c', font=regular_font)
    
    # Validity date
    valid_until = datetime.now().year + 1
    draw.text((215, 190), f"Valid Through: DEC {valid_until}", fill='#3d7f7f', font=tiny_font)
    
    # ✅ Paste photo with perfect fitting
    if member.photo and os.path.exists(member.photo.path):
        try:
            photo = Image.open(member.photo.path).convert('RGBA')
            # Smart crop to fit square perfectly
            photo = smart_square_crop(photo, 145, 145)
            
            # Create circular mask with anti-aliasing
            mask = Image.new('L', (145, 145), 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse([0, 0, 145, 145], fill=255)
            
            # Apply mask
            photo.putalpha(mask)
            
            # Add 3D border effect (multiple layers)
            # Outer shadow
            shadow = Image.new('RGBA', (145, 145), (0, 0, 0, 80))
            shadow.putalpha(mask)
            base.paste(shadow, (57, 67), shadow)
            
            # White border
            border_white = Image.new('RGBA', (151, 151), (255, 255, 255, 255))
            draw_border = ImageDraw.Draw(border_white)
            draw_border.ellipse([0, 0, 151, 151], fill=255)
            photo_with_border = Image.new('RGBA', (151, 151), (0, 0, 0, 0))
            photo_with_border.paste(photo, (3, 3))
            
            # Gold accent border
            border_gold = Image.new('RGBA', (157, 157), (0, 0, 0, 0))
            draw_gold = ImageDraw.Draw(border_gold)
            draw_gold.ellipse([0, 0, 157, 157], outline='#d4af37', width=3)
            
            # Paste all layers
            base.paste(border_gold, (49, 57), border_gold)
            base.paste(border_white, (52, 60), border_white)
            base.paste(photo_with_border, (52, 60), photo_with_border)
            
        except Exception as e:
            print(f"Photo error: {e}")
            draw_placeholder_photo(draw, 52, 60, 145)
    else:
        draw_placeholder_photo(draw, 52, 60, 145)
    
    # Save the generated ID card
    output_dir = os.path.join(settings.MEDIA_ROOT, 'id_cards')
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{member.membership_id}.png"
    path = os.path.join(output_dir, filename)
    base.save(path, quality=95, dpi=(300, 300))
    
    return f"id_cards/{filename}"


def create_premium_3d_template(save_path):
    """Creates a premium 3D ID card with visible teal/green patterns"""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Create base image (400x250)
    img = Image.new('RGB', (400, 250), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    # ✅ VISIBLE TEAL/GREEN GRADIENT BACKGROUND
    # Base gradient
    for y in range(250):
        if y < 70:
            # Rich teal header gradient
            factor = y / 70
            r = int(20 + (40 - 20) * factor)
            g = int(118 + (140 - 118) * factor)
            b = int(126 + (148 - 126) * factor)
            color = (r, g, b)
        else:
            # Visible light teal body with pattern
            factor = (y - 70) / 180
            r = int(220 + (240 - 220) * factor)
            g = int(245 + (255 - 245) * factor)
            b = int(240 + (250 - 240) * factor)
            color = (r, g, b)
        draw.line([(0, y), (400, y)], fill=color)
    
    # PROMINENT SECURITY PATTERN (Visible like real ID cards)
    # Diagonal stripe pattern
    for i in range(-300, 700, 50):
        opacity = 60 if (i // 100) % 2 == 0 else 30
        draw.line([(i, 70), (i+200, 250)], fill=(20, 118, 126, opacity), width=2)
    
    # Geometric pattern overlay
    for x in range(30, 400, 60):
        for y in range(90, 240, 50):
            # Hexagon-like shapes
            draw.polygon([
                (x, y-15), (x+12, y-8), (x+12, y+8), 
                (x, y+15), (x-12, y+8), (x-12, y-8)
            ], outline=(140, 200, 190, 100), width=1)
    
    # Wave pattern
    for x in range(0, 400, 30):
        draw.arc([x-15, 100, x+45, 160], 0, 180, fill=(20, 118, 126, 40), width=2)
        draw.arc([x-15, 150, x+45, 210], 180, 360, fill=(20, 118, 126, 40), width=2)
    
    # ✅ 3D HEADER WITH DEPTH
    # Main header
    draw.rectangle([0, 0, 400, 70], fill='#14919b')
    
    # Header highlight (top edge - 3D effect)
    draw.line([(0, 0), (400, 0)], fill='#2ec4b6', width=3)
    
    # Header shadow (bottom edge - 3D effect)
    draw.line([(0, 69), (400, 69)], fill='#0d7377', width=3)
    
    # Decorative gradient overlay on header
    for x in range(400):
        factor = x / 400
        r = int(20 + (60 - 20) * factor)
        g = int(118 + (180 - 118) * factor)
        b = int(126 + (196 - 126) * factor)
        draw.line([(x, 0), (x, 70)], fill=(r, g, b, 30))
    
    # Organization name with shadow
    title_font = load_font(22, bold=True)
    # Shadow
    draw.text((202, 27), "LEADERSHIP BRIDGE", fill='#0a5c5f', font=title_font, anchor='mm')
    # Main text
    draw.text((200, 25), "LEADERSHIP BRIDGE", fill='white', font=title_font, anchor='mm')
    
    # Tagline
    tagline_font = load_font(10)
    draw.text((200, 48), "Empowering Leaders • Transforming Communities", fill='#a8fff5', 
              font=tagline_font, anchor='mm')
    
    # ✅ 3D BORDER AROUND ENTIRE CARD
    # Outer border (dark)
    draw.rectangle([0, 0, 399, 249], outline='#0d7377', width=4)
    # Inner border (light - creates 3D effect)
    draw.rectangle([3, 3, 396, 246], outline='#2ec4b6', width=2)
    # Innermost border (dark again)
    draw.rectangle([6, 6, 393, 243], outline='#0d7377', width=1)
    
    # ✅ 3D PHOTO FRAME
    # Outer shadow
    draw.rounded_rectangle([48, 56, 200, 208], radius=10, fill='#000000', outline='#0a5c5f', width=3)
    # Main frame
    draw.rounded_rectangle([50, 58, 198, 206], radius=9, fill='#ffffff', outline='#14919b', width=3)
    # Inner highlight
    draw.rounded_rectangle([53, 61, 195, 203], radius=7, fill='#f0fffe', outline='#2ec4b6', width=1)
    # Corner accents (3D effect)
    draw.rectangle([52, 58, 58, 64], fill='#d4af37')  # Top-left gold
    draw.rectangle([192, 58, 198, 64], fill='#d4af37')  # Top-right gold
    draw.rectangle([52, 200, 58, 206], fill='#d4af37')  # Bottom-left gold
    draw.rectangle([192, 200, 198, 206], fill='#d4af37')  # Bottom-right gold
    
    # ✅ 3D BOTTOM STRIP
    # Main strip
    draw.rectangle([0, 235, 400, 250], fill='#0d7377')
    # Highlight
    draw.line([(0, 235), (400, 235)], fill='#2ec4b6', width=2)
    # Shadow
    draw.line([(0, 248), (400, 248)], fill='#0a5c5f', width=2)
    
    # Security microtext
    micro_font = load_font(6)
    draw.text((10, 240), "LB•SECURE•ID•2025" * 8, fill='#5a9f9f', font=micro_font)
    
    # Holographic-style circles (security feature)
    for i in range(5):
        x = 320 + (i * 15)
        y = 80 + (i * 5)
        draw.ellipse([x, y, x+8, y+8], outline=(212, 175, 55, 80), width=1)
    
    # Save template
    img.save(save_path, dpi=(300, 300))
    
    return img.convert('RGB')


def smart_square_crop(image, width, height):
    """Smart crop to fit square perfectly while maintaining focus"""
    # Get dimensions
    img_width, img_height = image.size
    
    # Calculate crop box for center square
    min_dim = min(img_width, img_height)
    left = (img_width - min_dim) // 2
    top = (img_height - min_dim) // 2
    right = left + min_dim
    bottom = top + min_dim
    
    # Crop to square
    image = image.crop((left, top, right, bottom))
    
    # Resize to target dimensions
    image = image.resize((width, height), Image.Resampling.LANCZOS)
    
    return image


def draw_3d_box(draw, x1, y1, x2, y2, main_color, highlight_color, shadow_color):
    """Draw a 3D-styled rounded rectangle box"""
    # Shadow (bottom-right)
    draw.rounded_rectangle([x1+2, y1+2, x2+2, y2+2], radius=5, fill=shadow_color)
    # Highlight (top-left)
    draw.rounded_rectangle([x1, y1, x2, y2], radius=5, fill=highlight_color)
    # Main color
    draw.rounded_rectangle([x1+1, y1+1, x2-1, y2-1], radius=4, fill=main_color)


def draw_placeholder_photo(draw, x, y, size):
    """Draw a professional placeholder for missing photo"""
    # Background
    draw.rounded_rectangle([x, y, x+size, y+size], radius=8, fill='#f0fffe', outline='#14919b', width=2)
    # Icon circle
    draw.ellipse([x+40, y+40, x+size-40, y+size-40], outline='#2ec4b6', width=2)
    # Person icon (simple)
    draw.ellipse([x+55, y+50, x+size-55, y+85], fill='#2ec4b6')  # Head
    draw.arc([x+45, y+85, x+size-45, y+120], 0, 180, fill='#2ec4b6', width=4)  # Shoulders
    # Text
    tiny_font = load_font(11)
    draw.text((x+size//2, y+size//2+20), "PHOTO", fill='#999', font=tiny_font, anchor='mm')


def load_font(size, bold=False):
    """Load font with multiple fallbacks"""
    font_paths = [
        os.path.join(settings.BASE_DIR, 'fonts', 'arialbd.ttf' if bold else 'arial.ttf'),
        'C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    
    return ImageFont.load_default()


def get_role_color(role):
    """Return premium color based on role"""
    colors = {
        'Volunteer': '#27ae60',           # Emerald Green
        'Community Leader': '#2980b9',    # Royal Blue
        'Donor': '#d4af37',               # Metallic Gold
        'Trainee': '#8e44ad',             # Deep Purple
    }
    return colors.get(role, '#14919b')


def darken_color(hex_color, percent):
    """Darken a hex color by percentage"""
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    factor = 1 - (percent / 100)
    r = max(0, int(r * factor))
    g = max(0, int(g * factor))
    b = max(0, int(b * factor))
    return f'#{r:02x}{g:02x}{b:02x}'




