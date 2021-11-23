import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape


# Load the image and convert it to grayscale:
img = cv.imread(r'C:\Users\user\Desktop\cv-master\samples\data\shape_.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
################################    CONTOURING   ############################################# 
# Apply thresholding to get a binary image:
ret, threshImg = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY)

# Find contours using the thresholded image:
contours, hierarchy = cv.findContours(threshImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# number of detected contours:
print(f"There is {len(contours)}", "shape in the image")

####################################  Identify shape  ###############################################


def detect_shape():
    plt.figure(figsize=(12,8))

    # approxPolyDP():
    imgApproxPolyDP = img.copy()
    for contour in contours:
        perimeter = cv.arcLength(contour, True)
        epsilon = 0.04 * perimeter
        approxPolyDP = cv.approxPolyDP(contour, epsilon, True)

        
        color = (0, 255, 255)
        thickness = 5
        # draw line
        for approx in approxPolyDP:
            cv.drawContours(imgApproxPolyDP, [approx], 0, color, thickness)
        color = (255, 255, 255)
        thickness = 5
        # draw points
        for approx in [approxPolyDP]:
            # draw points
            squeeze = np.squeeze(approx)
            #print('contour:',approx.shape, squeeze.shape)
            for p in squeeze:
                pp = tuple(p.reshape(1, -1)[0])
                cv.circle(imgApproxPolyDP, pp, 10, color, -1)


        # determine shape   
        verticeNumber = len(approxPolyDP)
        if verticeNumber == 3:
            vertice_shape = (verticeNumber, 'Triangle')
        elif verticeNumber == 4:
            # get aspect ratio
            x, y, width, height = cv.boundingRect(approxPolyDP)
            aspectRatio = float(width) / height
            #print(aspectRatio)
            if 0.90 < aspectRatio < 1.1: 
                vertice_shape = (verticeNumber, 'Square')
            else:
                vertice_shape = (verticeNumber, 'Rectangle')
        elif verticeNumber == 5:
            vertice_shape = (verticeNumber, 'Pentagon')
        elif verticeNumber == 6:
            vertice_shape = (verticeNumber, 'Hexagon')
        elif verticeNumber == 9:
            vertice_shape = (verticeNumber, 'Nanogon')
        else:
            vertice_shape = (verticeNumber, 'Circle')
        
        # write shape
        # Compute the moment of contour:
        M = cv.moments(contour)

        # The center or centroid can be calculated as follows:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])

        # Get the position to draw:    
        text = vertice_shape[1]
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        thickness = 2
        text_size = cv.getTextSize(text, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgApproxPolyDP, text, (text_x, text_y), fontFace, fontScale, color, thickness)
        
    # BGR to RGB
    imgRGB = imgApproxPolyDP[:,:,::-1]
    plt.subplot(122)
    plt.title("Shapes name")
    plt.imshow(imgRGB)

    plt.show()
############################################   sort by size   ##########################################
def sort_by_size():

    imgSize = img.copy()

    imgGray = cv.cvtColor(imgSize, cv.COLOR_BGR2GRAY)
    # Apply thresholding to get a binary image:
    ret, threshImg = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY)

    # Find contours using the thresholded image:
    contours, hierarchy = cv.findContours(threshImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    contours_sizes = [cv.contourArea(contour) for contour in contours]
    size_shape_list = zip(contours_sizes, contours)
    sorted_size_shape_list = sorted(size_shape_list)

    for i, (size, contour) in enumerate(sorted_size_shape_list):
        # Compute the moment of contour:
        M = cv.moments(contour)

        # The center or centroid can be calculated as follows:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])

        # Get the position to draw:    
        text = str(i + 1)
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 2
        thickness = 5
        text_size = cv.getTextSize(text, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        img1 = img.copy()
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgSize, text, (text_x, text_y), fontFace, fontScale, color, thickness)
        
    plt.figure(figsize=(12,8))
    # BGR to RGB
    imgRGB = imgSize[:,:,::-1]
    plt.subplot(122)
    plt.title("sort by size")
    plt.imshow(imgRGB)

    plt.show()

###################################### sort by shape ##################################################
def sort_by_shape():
    Lst =[]
    # approxPolyDP():
    imgshape = img.copy()
    for contour in contours:
        perimeter = cv.arcLength(contour, True)
        epsilon = 0.04 * perimeter
        approxPolyDP = cv.approxPolyDP(contour, epsilon, True)

        

        color = (0, 255, 255)
        thickness = 5
        # draw line
        for approx in approxPolyDP:
            cv.drawContours(imgshape, [approx], 0, color, thickness)
        color = (255, 255, 255)
        thickness = 5
        # draw points
        for approx in [approxPolyDP]:
            # draw points
            squeeze = np.squeeze(approx)
            #print('contour:',approx.shape, squeeze.shape)
            for p in squeeze:
                pp = tuple(p.reshape(1, -1)[0])
                cv.circle(imgshape, pp, 10, color, -1)


        # determine shape   
        verticeNumber = len(approxPolyDP)
        if verticeNumber == 3:
            vertice_shape = (verticeNumber, '1 Triangle')
        elif verticeNumber == 4:
            # get aspect ratio
            x, y, width, height = cv.boundingRect(approxPolyDP)
            aspectRatio = float(width) / height
            #print(aspectRatio)
            if 0.90 < aspectRatio < 1.1: 
                vertice_shape = (verticeNumber, '2 Square')
            else:
                vertice_shape = (verticeNumber, '3 Rectangle')
        elif verticeNumber == 5:
            vertice_shape = (verticeNumber, '4 Pentagon')
        elif verticeNumber == 6:
            vertice_shape = (verticeNumber, '5 Hexagon')
        elif verticeNumber == 9:
            vertice_shape = (verticeNumber, '6 Nanogon')
        else:
            vertice_shape = (verticeNumber, '7 Circle')
        Lst.append(verticeNumber)
        print(sorted(Lst))
        contours_sizes = [cv.contourArea(contour) for contour in contours]
        size_shape_list = zip(contours_sizes, Lst)
        sorted_size_shape_list = sorted(size_shape_list)
        print(sorted_size_shape_list)
        
        # write shape
        # Compute the moment of contour:
        M = cv.moments(contour)

        # The center or centroid can be calculated as follows:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])

        # Get the position to draw:    
        text = vertice_shape[1]
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        thickness = 2
        text_size = cv.getTextSize(text, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgshape, text, (text_x, text_y), fontFace, fontScale, color, thickness)
        
            
            #Lst.append(vertice_shape)
            #sorted_shape = sorted(Lst)
            #print(Lst.sort)          
    plt.figure(figsize=(12,8))
    # BGR to RGB
    imgRGB = imgshape[:,:,::-1]
    plt.subplot(122)
    plt.title("sort by shape then size")
    plt.imshow(imgRGB)

    plt.show()

def sort_by_shape_then_size():
   Lst =[]
   plt.figure(figsize=(12,8))

    # approxPolyDP():
   imgsize_1st = img.copy()
   for contour in contours:
        perimeter = cv.arcLength(contour, True)
        epsilon = 0.04 * perimeter
        approxPolyDP = cv.approxPolyDP(contour, epsilon, True)

        
        color = (0, 255, 255)
        thickness = 5
        # draw line
        for approx in approxPolyDP:
            cv.drawContours(imgsize_1st, [approx], 0, color, thickness)
        color = (255, 255, 255)
        thickness = 5
        # draw points
        for approx in [approxPolyDP]:
            # draw points
            squeeze = np.squeeze(approx)
            #print('contour:',approx.shape, squeeze.shape)
            for p in squeeze:
                pp = tuple(p.reshape(1, -1)[0])
                cv.circle(imgsize_1st, pp, 10, color, -1)


        # determine shape   
        verticeNumber = len(approxPolyDP)
        if verticeNumber == 3:
            vertice_shape = (verticeNumber, '2 Triangle')
        elif verticeNumber == 4:
            # get aspect ratio
            x, y, width, height = cv.boundingRect(approxPolyDP)
            aspectRatio = float(width) / height
            #print(aspectRatio)
            if 0.90 < aspectRatio < 1.1: 
                vertice_shape = (verticeNumber, '5 Square')
            else:
                vertice_shape = (verticeNumber, '6 Rectangle')
        elif verticeNumber == 5:
            vertice_shape = (verticeNumber, '3 Pentagon')
        elif verticeNumber == 6:
            vertice_shape = (verticeNumber, '1 Hexagon')
        elif verticeNumber == 9:
            vertice_shape = (verticeNumber, '7 Nanogon')
        else:
            vertice_shape = (verticeNumber, '4 Circle')

        Lst.append(verticeNumber)
        print(sorted(Lst))
        # write shape
        # Compute the moment of contour:
        M = cv.moments(contour)

        # The center or centroid can be calculated as follows:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])

        # Get the position to draw:    
        text = vertice_shape[1]
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        thickness = 2
        text_size = cv.getTextSize(text, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgsize_1st, text, (text_x, text_y), fontFace, fontScale, color, thickness)
        
    # BGR to RGB
   imgRGB = imgsize_1st[:,:,::-1]
   plt.subplot(122)
   plt.title("Shapes_then_size")
   plt.imshow(imgRGB)

   plt.show()            
            
##################################### sort by size then shape ###############################################
def certain_shape():
    

    # Find contours using the thresholded image:
    # Note: cv2.findContours() has been changed to return only the contours and the hierarchy
    contours, hierarchy = cv.findContours(threshImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # approxPolyDP():
    imgcertain = img.copy()
    for contour in contours:
        perimeter = cv.arcLength(contour, True)
        epsilon = 0.04 * perimeter
        approxPolyDP = cv.approxPolyDP(contour, epsilon, True)

        
        color = (0, 255, 255)
        thickness = 5
        # draw line
        for approx in approxPolyDP:
            cv.drawContours(imgcertain, [approx], 0, color, thickness)
        color = (255, 255, 255)
        thickness = 5
        # draw points
        for approx in [approxPolyDP]:
            # draw points
            squeeze = np.squeeze(approx)
            #print('contour:',approx.shape, squeeze.shape)
            for p in squeeze:
                pp = tuple(p.reshape(1, -1)[0])
                cv.circle(imgcertain, pp, 10, color, -1)


        # determine shape   
        verticeNumber = len(approxPolyDP)
        if verticeNumber == 3:
            vertice_shape = (verticeNumber, 'No match')
        elif verticeNumber == 4:
            # get aspect ratio
            x, y, width, height = cv.boundingRect(approxPolyDP)
            aspectRatio = float(width) / height
            #print(aspectRatio)
            if 0.90 < aspectRatio < 1.1: 
                vertice_shape = (verticeNumber, 'No match')
            else:
                vertice_shape = (verticeNumber, 'No match')
        elif verticeNumber == 5:
            vertice_shape = (verticeNumber, 'No match')
        elif verticeNumber == 6:
            vertice_shape = (verticeNumber, 'No match')
        elif verticeNumber == 9:
            vertice_shape = (verticeNumber, 'No match')
        else:
            vertice_shape = (verticeNumber, 'Circle')
            
        
        # write shape
        # Compute the moment of contour:
        M = cv.moments(contour)

        # The center or centroid can be calculated as follows:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])

        # Get the position to draw:    
        text = vertice_shape[1]
        fontFace = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        thickness = 2
        text_size = cv.getTextSize(text, fontFace, fontScale, thickness)[0]

        text_x = cX - text_size[0] / 2
        text_x = round(text_x)
        text_y = cY + text_size[1] / 2
        text_y = round(text_y)
        
        # Write the ordering of the shape on the center of shapes
        color = (0, 0, 0)
        cv.putText(imgcertain, text, (text_x, text_y), fontFace, fontScale, color, thickness)

    plt.figure(figsize=(12,8))    
    # BGR to RGB
    imgRGB = imgcertain[:,:,::-1]
    plt.subplot(122)
    plt.title("circle")
    plt.imshow(imgRGB)

    plt.show()



if __name__ == "__main__":
    detect_shape()
    sort_by_size()
    sort_by_shape()
    sort_by_shape_then_size()
    certain_shape()