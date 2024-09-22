import random
import numpy as np

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
