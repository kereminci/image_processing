# kerem inci
# 1306190041
# goruntu isleme odev-1

import cv2 as cv
import numpy as np

def histogram(img):
    # histogramini bulur
    frequency = np.array(np.unique(img, return_counts=True)).T
    return frequency

def histogram_equalization(img,frequency):
    
    total_pixel = img.size
    arr = np.zeros((256,),dtype=np.float16)
    sum = 0

    #slayttaki histogram esitleme yontemi kullanildi

    for element in frequency:
        
        p = round(element[1] / total_pixel, 3)
        sum = sum + p
        j = round(sum * 255)
        arr[j] = arr[j] + element[1]
    
    arr = arr.astype(np.uint8)
    return arr

    
def histogram_mapping(img, b):
    #histogram degerleri resimdeki degerleri ile eslendi

    for i in range(width):
        for j in range(height):
            g = img[j,i]
            img[j,i]= b[g]



def histogram_stretching(img):
    
    arr = np.zeros((256,),dtype=np.float16)

    minValue = np.amin(img)
    maxValue = np.amax(img)

    #hardcoded values
    newMin = 100
    newMax = 200
    # histogram germe uygulandı
    for i in range(width):
        for j in range(height):
            g = img[j,i]
            img[j,i]= (g - minValue) / (maxValue - minValue) * 255

    h = histogram(img)

    for el in h:
        arr[el[0]] = arr[el[0]] + el[1]
    
    arr = arr.astype(np.uint8) # yeni histogram
    
    return arr


# sample resimleri oldugu datapath eklendi
cv.samples.addSamplesDataSearchPath("C:\opencv\sources\samples\data")
img = cv.imread(cv.samples.findFile("apple.jpg"), cv.IMREAD_GRAYSCALE)
height, width= img.shape

#histogram esitleme
#f = histogram(img)
#h = histogram_equalization(img,f)
#histogram_mapping(img,h)

# histogram germe
#histogram_stretching(img)


#cv.imshow("Display window", img)
#cv.waitKey(0)