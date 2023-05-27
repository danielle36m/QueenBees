import colorsys

def get_complementary_color(color):
    # Convert color from hexadecimal to RGB
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    
    # Convert RGB to HSL
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    
    # Calculate the complementary hue (180 degrees opposite)
    complementary_h = (h + 0.5) % 1.0
    
    # Convert complementary hue back to RGB
    r_c, g_c, b_c = colorsys.hls_to_rgb(complementary_h, l, s)
    
    # Convert RGB values to hexadecimal
    complementary_color = f"#{int(r_c * 255):02X}{int(g_c * 255):02X}{int(b_c * 255):02X}"
    
    return complementary_color

def generate_complementary_variations(base_color):
    variations = []
    
    # Get the base complementary color
    base_complementary = get_complementary_color(base_color)
    variations.append(base_complementary)
    
    # Generate variations by adjusting saturation, brightness, or hue
    for i in range(1, 5):
        h, l, s = colorsys.rgb_to_hls(int(base_complementary[1:3], 16) / 255, int(base_complementary[3:5], 16) / 255, int(base_complementary[5:7], 16) / 255)
        
        # Adjust saturation
        saturation = (1.0 + i) / 6
        modified_color = colorsys.hls_to_rgb(h, l, saturation)
        variations.append(f"#{int(modified_color[0] * 255):02X}{int(modified_color[1] * 255):02X}{int(modified_color[2] * 255):02X}")
        
        # Adjust brightness
        brightness = (1.0 + i) / 6
        modified_color = colorsys.hls_to_rgb(h, brightness, s)
        variations.append(f"#{int(modified_color[0] * 255):02X}{int(modified_color[1] * 255):02X}{int(modified_color[2] * 255):02X}")
        
        # Adjust hue
        hue = (h + (i * 0.1)) % 1.0
        modified_color = colorsys.hls_to_rgb(hue, l, s)
        variations.append(f"#{int(modified_color[0] * 255):02X}{int(modified_color[1] * 255):02X}{int(modified_color[2] * 255):02X}")
    
    return variations

# Example usage
if __name__ == "__main__":
    print("starting")
    base_color = "#6A666E"
    complementary_variations = generate_complementary_variations(base_color)
    print(complementary_variations)
