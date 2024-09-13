import matplotlib.pyplot as plt
import random

# Define the space dimensions
space_width = 100
space_height = 100

# Generate random rectangles (width, height)
def generate_rectangles(num_rectangles=5):
    rectangles = []
    for _ in range(num_rectangles):
        width = random.randint(10, 30)
        height = random.randint(10, 30)
        rectangles.append((width, height))
    return rectangles

# Function to recursively partition the space and place rectangles
def place_rectangles(space, rectangles):
    if not rectangles:
        return []
    
    rect = rectangles[0]
    remaining_rects = rectangles[1:]
    
    width, height = rect
    space_width, space_height, space_x, space_y = space
    
    # Try placing the rectangle without rotation
    if width <= space_width and height <= space_height:
        # Place rectangle and split remaining space
        remaining_space_1 = (space_width - width - 1, space_height, space_x + width + 1, space_y)
        remaining_space_2 = (width, space_height - height - 1, space_x, space_y + height + 1)
        return [(space_x, space_y, width, height)] + place_rectangles(remaining_space_1, remaining_rects) + place_rectangles(remaining_space_2, remaining_rects)
    
    # Try placing the rectangle with rotation
    if height <= space_width and width <= space_height:
        # Rotate and place
        remaining_space_1 = (space_width - height - 1, space_height, space_x + height + 1, space_y)
        remaining_space_2 = (height, space_height - width - 1, space_x, space_y + width + 1)
        return [(space_x, space_y, height, width)] + place_rectangles(remaining_space_1, remaining_rects) + place_rectangles(remaining_space_2, remaining_rects)
    
    # If we cannot place the rectangle, return error
    raise ValueError("Placement not possible for this rectangle configuration")

# Function to plot the rectangles
def plot_rectangles(rectangles):
    fig, ax = plt.subplots()
    
    for rect in rectangles:
        x, y, width, height = rect
        ax.add_patch(plt.Rectangle((x, y), width, height, fill=None, edgecolor='blue'))
    
    plt.xlim(0, space_width)
    plt.ylim(0, space_height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

# Main function
def main():
    rectangles = generate_rectangles(5)
    print("Generated Rectangles (width, height):", rectangles)
    
    try:
        placed_rectangles = place_rectangles((space_width, space_height, 0, 0), rectangles)
        print("Placed rectangles:", placed_rectangles)
        plot_rectangles(placed_rectangles)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
