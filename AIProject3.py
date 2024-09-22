from PIL import Image, ImageDraw
import random
import numpy as np
import random
import torch


def _create_image():
    image = np.empty((20,20))
    color_list = ['red', 'blue', 'green', 'yellow']

    red_integer, yellow_integer, wire_to_cut, safety = 0, 0, None, 'Safe'

    if random.random() < 0.5:
        #Start with row
        row_integer = random.randint(1,20)
        color = random.choice(color_list)
        image[row_integer, :] = color 
        
        if (color == 'red'):
            red_integer = row_integer
        elif(color == 'yellow'):
            yellow_integer = row_integer

        color_list.remove(color)

        #col 1 
        col_integer = random.randint(1,20)
        color = random.choice(color_list)
        image[:,col_integer] = color 

        if (color == 'red'):
            red_integer = col_integer
        elif(color == 'yellow'):
            yellow_integer = col_integer

        color_list.remove(color)

        #row 2        
        row_2_integer = random.randint(1,20)
        if(row_2_integer == row_integer):
            row_2_integer = random.randint(1,20)

        color = random.choice(color_list)
        image[row_2_integer, :] = color 

        if (color == 'red'):
            red_integer = row_2_integer
        elif(color == 'yellow'):
            yellow_integer = row_2_integer

        wire_to_cut = color
        color_list.remove(color)

        #col 2
        col_2_integer = random.randint(1,20)
        if(col_2_integer == row_integer):
            col_2_integer = random.randint(1,20)

        color = random.choice(color_list)
        image[:, col_2_integer] = color
        
        if (color == 'red'):
            red_integer = col_2_integer
        elif(color == 'yellow'):
            yellow_integer = col_2_integer

        color_list.remove(color)
    
    else:
        #col 1 
        col_integer = random.randint(1,20)
        color = random.choice(color_list)
        image[:,col_integer] = color 

        if (color == 'red'):
            red_integer = col_integer
        elif(color == 'yellow'):
            yellow_integer = col_integer

        color_list.remove(color)

        #Start with row
        row_integer = random.randint(1,20)
        color = random.choice(color_list)
        image[row_integer, :] = color 

        if (color == 'red'):
            red_integer = row_integer
        elif(color == 'yellow'):
            yellow_integer = row_integer

        color_list.remove(color)

        #col 2
        col_2_integer = random.randint(1,20)
        if(col_2_integer == row_integer):
            col_2_integer = random.randint(1,20)

        color = random.choice(color_list)
        image[:, col_2_integer] = color 

        if (color == 'red'):
            red_integer = col_2_integer
        elif(color == 'yellow'):
            yellow_integer = col_2_integer
        
        wire_to_cut = color
        color_list.remove(color)

        #row 2        
        row_2_integer = random.randint(1,20)
        if(row_2_integer == row_integer):
            row_2_integer = random.randint(1,20)

        color = random.choice(color_list)
        image[row_2_integer, :] = color 

        if (color == 'red'):
            red_integer = row_2_integer
        elif(color == 'yellow'):
            yellow_integer = row_2_integer

        color_list.remove(color)

    if red_integer < yellow_integer:
        safety = 'Dangerous'

    return (image, safety, wire_to_cut)

#So like the data set should be {(diagram,dangerous or not), (),...}
def create_data_set(num_iters: int):
    data_set = [num_iters]
    
    for i in range(num_iters):
        data_set.append(_create_image())
                
    return data_set



# Function to sigmoid activation
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Function to compute the loss (binary cross-entropy)
def compute_loss(y_true, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return - (y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)).mean()

def generate_image(iteration: int):
    # Create a white 20x20 image
    image = Image.new("RGB", (20, 20), "white")
    draw = ImageDraw.Draw(image)

    # Define colors
    colors = ["red", "blue", "yellow", "green"]

    # Randomly choose whether to start with rows or columns
    start_with_rows = random.choice([True, False])

    # Initialize variables to keep track of selected rows and columns
    selected_row = None
    selected_col = None

    # Variable to track whether the image is dangerous
    is_dangerous = False

    for _ in range(2):
        for _ in range(2):
            # Randomly select a row or column
            if start_with_rows:
                selected_row = random.randint(0, 19)
                color = random.choice(colors)
                draw.line([(0, selected_row), (19, selected_row)], fill=color, width=1)
            else:
                selected_col = random.randint(0, 19)
                color = random.choice([c for c in colors if c != image.getpixel((selected_col, 0))])
                draw.line([(selected_col, 0), (selected_col, 19)], fill=color, width=1)

            # Update colors
            colors.remove(color)

            if color == "red" and "yellow" in colors:
                is_dangerous = True

            # Switch starting point
            start_with_rows = not start_with_rows

    # Save the image
    
    if is_dangerous:
        image.save(f"dataset/is_dangerous/generated_image_{iteration}.png")
    else:
        image.save(f"dataset/safe/generated_image_{iteration}.png")

if __name__ == "__main__":
    for i in range(1000):
        generate_image(i)
        


    
    