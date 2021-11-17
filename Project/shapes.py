import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

def font_size():
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
plt.figure(figsize=(16,12))

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
    font_size()
# BGR to RGB
imgRGB = imgApproxPolyDP[:,:,::-1]
plt.subplot(212)
plt.title("Shapes name")
plt.imshow(imgRGB)

plt.show()

############################################   sort by size   ##########################################
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
    font_size()

plt.figure(figsize=(8,12))
# BGR to RGB
imgRGB = imgSize[:,:,::-1]
plt.subplot(212)
plt.title("sort by size")
plt.imshow(imgRGB)

plt.show()

##################################### sort by size then shape ###############################################
imgApproxPolyDP = img.copy()
contours_sizes = [cv.contourArea(contour) for contour in contours]
size_shape_list = zip(contours_sizes, contours)
sorted_size_shape_list = sorted(size_shape_list)
    
for i, (size, contour) in enumerate(sorted_size_shape_list):
    
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
        elif verticeNumber == 8:
            vertice_shape = (verticeNumber, 'Octagon')
        else:
            vertice_shape = (verticeNumber, 'Circle')
        
        font_size()

plt.figure(figsize=(6,8))
# BGR to RGB
imgRGB = imgApproxPolyDP[:,:,::-1]
plt.subplot(212)
plt.title("sort by size then shape")
plt.imshow(imgRGB)

plt.show()

############################################ sort shape then size ###################################

imgApproxPolyDP1 = img.copy()
contours_sizes = [cv.contourArea(contour) for contour in contours]
size_shape_list = zip(contours_sizes, contours)
sorted_size_shape_list = sorted(size_shape_list)
lst = []    
for i, (size, contour) in enumerate(sorted_size_shape_list):
    
    for contour in contours:
        perimeter = cv.arcLength(contour, True)
        epsilon = 0.03 * perimeter
        approxPolyDP = cv.approxPolyDP(contour, epsilon, True)
    

        color = (0, 255, 255)
        thickness = 5
    # draw line
        for approx in approxPolyDP:
            cv.drawContours(imgApproxPolyDP1, [approx], 0, color, thickness)
            color = (255, 255, 255)
            thickness = 5
    # draw points
        for approx in [approxPolyDP]:
        # draw points
            squeeze = np.squeeze(approx)
        #print('contour:',approx.shape, squeeze.shape)
            for p in squeeze:
                pp = tuple(p.reshape(1, -1)[0])
                cv.circle(imgApproxPolyDP1, pp, 10, color, -1)
       
        list_shape = lst.append(verticeNumber)
        
       


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
        elif verticeNumber == 8:
            vertice_shape = (verticeNumber, 'Octagon')
        else:
            vertice_shape = (verticeNumber, 'Circle')
        
        font_size()

    #shape_sorted =sorted(verticeNumber)
    #print("sorted shape are by",shape_sorted)
sorted_shape = cv.sort(list_shape)
print(sorted_shape)
plt.figure(figsize=(8,6))
# BGR to RGB
imgRGB = imgApproxPolyDP1[:,:,::-1]
plt.subplot(221)
plt.title("sort by size then shape")
plt.imshow(imgRGB)

plt.show()
