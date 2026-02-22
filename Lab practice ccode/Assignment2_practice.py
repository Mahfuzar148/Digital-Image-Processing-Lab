
import matplotlib.pyplot as plt
import numpy as np


def main() :
    h,w = 200,200
    shades = [85,170,255]
    colors = {
       "white":[1,1,1],
       "red": [1,0,0],
       "green":[0,1,0],
       "blue":[0,0,1],
       "yellow":[1,1,0],
       "magenta":[1,0,1],
       "cyan":[0,1,1] 
    }
    
    plt.figure(figsize=(18,12),constrained_layout = True)
    
    for row,(name,base) in enumerate(colors.items()):
        for col,shade in enumerate(shades):
            
            img =np.zeros((h,w,3),dtype=np.uint8)
            
            img[:,:,0] = base[0] * shade 
            img[:,:,1] = base[1]* shade 
            img[:,:,2] = base[2] *shade
            
            plt.subplot(len(colors),3,row*3+col+1)
            plt.imshow(img)
            plt.title(f"{name}-{shade}")
            plt.axis('off')
            
    plt.tight_layout()
    plt.savefig("output.png",dpi=300,bbox_inches="tight")
    plt.show()
    
            

if __name__ == "__main__" :
    main()   