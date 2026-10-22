from PIL import Image, ImageDraw

# 1. Create a blank canvas (width, height)
# Make sure your image resolution looks good for your screen
canvas = Image.new('RGB', (800, 600), color='white')

# 2. Get the drawing "pen" (this is like a marker)
draw = ImageDraw.Draw(canvas)

# 3. Draw shapes
# A Circle
draw.ellipse([100, 100, 400, 400], fill='skyblue')

# A Rectangle
draw.rectangle([500, 200, 750, 400], outline='red', width=3)

# Add some text
try:
    # Try to load a font. If your system doesn't have fonts installed for PIL easily, 
    # this might throw an error on Windows/Linux. 
    # We will handle it gracefully below or assume you have one.
    try:
        import ftfy
    except:
        pass

    draw.text((300, 580), "Hello Python!", fill='black', font=("Arial", 40))
except ImportError:
    # Fallback if you don't have specific fonts on your system
    print("Note: Ensure 'Arial' or a similar font is installed.")

# 4. Save the image
filename = "my_python_art.png"
canvas.save(filename)
print(f"🎨 Image saved as {filename}")
