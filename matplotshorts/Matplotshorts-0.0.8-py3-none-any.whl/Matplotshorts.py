import matplotlib.pyplot as plt
import math

def grid_display(list_of_images, list_of_titels = False, number_of_columns=2, figsize=(3,3)):
    arr_x = min(number_of_columns,len(list_of_images))
    arr_y = int(math.ceil(len(list_of_images)/number_of_columns))
    fig, axs = plt.subplots(arr_y, arr_x , sharex='all', sharey='all', figsize=(figsize[1]*arr_x,figsize[0]*arr_y))
    axs
    if len(list_of_images) != len(list_of_titels):
        list_of_titels = False
    
    for idx, img in enumerate(list_of_images):
        y = idx//number_of_columns
        x = idx%number_of_columns
        if arr_x == 1:
            axs[y].imshow(img)
            if(list_of_titels):
                axs[y].title.set_text(str(list_of_titels[idx]))
                
        elif arr_y == 1:
            axs[x].imshow(img)
            if(list_of_titels):
                axs[x].title.set_text(str(list_of_titels[idx]))
                
        else:
            axs[y,x].imshow(img)
            if(list_of_titels):
                axs[y,x].title.set_text(str(list_of_titels[idx]))