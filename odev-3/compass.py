# kerem inci
# 1306190041
# goruntu isleme odev-3

import cv2 as cv
import numpy as np

def max_mask_value(i,j):
    #(img[i-1,j-1] + img[i,j-1] + img[i + 1,j-1] + img[i-1,j] + img[i,j] + img[i+1,j] + img[i-1,j+1] + img[i,j+1] + img[i+1,j+1])
    masks = []
    masks.append((-img[i-1,j-1] - img[i,j-1] - img[i + 1,j-1] + img[i-1,j] -2* img[i,j] + img[i+1,j] + img[i-1,j+1] + img[i,j+1] + img[i+1,j+1]))
    masks.append((-img[i-1,j-1] - img[i,j-1] + img[i + 1,j-1] - img[i-1,j] -2* img[i,j] + img[i+1,j] + img[i-1,j+1] + img[i,j+1] + img[i+1,j+1]))
    masks.append((-img[i-1,j-1] + img[i,j-1] + img[i + 1,j-1] - img[i-1,j] -2* img[i,j] + img[i+1,j] - img[i-1,j+1] + img[i,j+1] + img[i+1,j+1]))
    masks.append((+img[i-1,j-1] + img[i,j-1] + img[i + 1,j-1] - img[i-1,j] -2* img[i,j] + img[i+1,j] - img[i-1,j+1] - img[i,j+1] + img[i+1,j+1]))

    masks.append((+img[i-1,j-1] + img[i,j-1] + img[i + 1,j-1] + img[i-1,j] -2* img[i,j] + img[i+1,j] - img[i-1,j+1] - img[i,j+1] - img[i+1,j+1])) #180
    masks.append((+img[i-1,j-1] + img[i,j-1] + img[i + 1,j-1] + img[i-1,j] -2* img[i,j] - img[i+1,j] + img[i-1,j+1] - img[i,j+1] - img[i+1,j+1])) #225
    masks.append((+img[i-1,j-1] + img[i,j-1] - img[i + 1,j-1] + img[i-1,j] -2* img[i,j] - img[i+1,j] + img[i-1,j+1] + img[i,j+1] - img[i+1,j+1])) #270
    masks.append((+img[i-1,j-1] - img[i,j-1] - img[i + 1,j-1] + img[i-1,j] -2* img[i,j] - img[i+1,j] + img[i-1,j+1] + img[i,j+1] + img[i+1,j+1])) #315

    return max(masks)



def compass():
    for i in range(1,width - 1):
        for j in range(1,height - 1):

            result = max_mask_value(i,j)

            new_img[i][j] = result

    
    return



img = cv.imread("apple.jpg", cv.IMREAD_GRAYSCALE)
new_img = np.copy(img)
height, width= img.shape

compass()


cv.imshow("Display window", new_img)
cv.waitKey(0)
