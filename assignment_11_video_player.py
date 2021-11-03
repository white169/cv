import cv2 as cv
import sys 

print(f'argunment array{sys.argv}')
print(' 1st argument:',sys.argv[0])
#print(' 2nd argument:',sys.argv[1])

filepath = sys.argv[0]

capture = cv.VideoCapture(filepath)
# check if connected
if capture.isOpened() is False:
    print("Error opening camera 0")
    exit()
    
frame_width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv.CAP_PROP_FPS)

print(f"CV_CAP_PROP_FRAME_WIDTH: {frame_width}")
print(f"CV_CAP_PROP_FRAME_HEIGHT : {frame_height}")
print(f"CAP_PROP_FPS : {fps}")

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
video_out = cv.VideoWriter('output_border.avi', fourcc, 20.0, (640,  480))

while capture.isOpened():
    # capture frames, if read correctly ret is True
    ret, frame = capture.read()

    if not ret:
        print("Didn't receive frame. Stop ")
        break

    # write the flipped frame
    video_out.write(frame)


    # top border
    frame[:10,:] = [100,190,90]
    # bottom border
    frame[-10:,:] = [255,0,255]
    # left border
    frame[:,:10] = [200,190,10]
    # right border
    frame[:,-10:] = [80,255,255]
    
     # display frame
    cv.imshow("Camera frame", frame)

    k = cv.waitKey(1) 
    # check if key is q then exit
    if k == ord("q"):
        break

capture.release()
video_out.release()
cv.destroyAllWindows()