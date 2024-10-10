from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random


# Function to generate 32x32 black and white image for a given character (number or alphabet)
def generate_image(character, font_path=None, size=(64, 64)):
    # Create a new blank image (black background)
    img = Image.new("L", size, color=0)  # 'L' for grayscale mode, 0 for black
    
    # Initialize drawing context
    draw = ImageDraw.Draw(img)
    
    # Load a font (optional: you can provide a custom font path)
    if font_path:
        font = ImageFont.truetype(font_path, 40)  # Adjust font size as needed
    else:
        font = ImageFont.load_default()  # Use default bitmap font if none is provided
    
    # Get the bounding box of the character
    text_bbox = draw.textbbox((0, 0), character, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Calculate position to center the text in the image
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    # Draw the character (white color) at the centered position
    draw.text(position, character, fill=255, font=font)
    
    return np.array(img.rotate(random.randint(-90,90)))



def add_noise(pattern, noise_level=0.1):
    """
    Add noise to a pattern by flipping a percentage of bits.
    
    Args:
        pattern (np.ndarray): The original pattern (binary 1 or 0).
        noise_level (float): The fraction of bits to flip (default is 10%).
    
    Returns:
        np.ndarray: The noisy pattern.
    """
    # Flatten the pattern (in case it's 2D) to work with it as a 1D array
    pattern_flat = pattern.flatten()
    
    # Determine the number of bits to flip based on the noise level
    n_flip = int(noise_level * len(pattern_flat))
    
    # Randomly choose indices to flip
    flip_indices = np.random.choice(len(pattern_flat), size=n_flip, replace=False)
    
    # Create a copy of the pattern to modify
    noisy_pattern = pattern_flat.copy()
    
    # Flip the chosen bits (1 -> 0, 0 -> 1)
    noisy_pattern[flip_indices] = 1 - noisy_pattern[flip_indices]
    
    # Reshape back to the original pattern shape
    return noisy_pattern.reshape(pattern.shape)