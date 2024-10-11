#OBJECT DETECTION USING OPEN CV AND YOLO

#Importing necessary libraries
import cv2 as cv
import random
from ultralytics import YOLO

# Loading the yolov8n model
yolo = YOLO('yolov8n.pt')

# Class Colours (for bounding box and text)
colours ={}
def getColours(cls_num):
    #checks if colour for the specifies class is present in colours
    if cls_num not in colours:
        #if not then generate random colour for the class
        colours[cls_num] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return colours[cls_num]

# Get input of choice from user 
choice = int(input("Input 1 for image object detection and 2 for video object detection: "))

# Image Object Detection
if choice==1:
    # get the path of image file from user
    path=input("Specify the path of your image: ")
    # reading the image
    img = cv.imread(path)
    # predicting the image and returns array of objects
    results = yolo.predict(path)

    # looping through each object
    for result in results:
        # get the classes names
            names = result.names

            # looping over each bounding box
            for box in result.boxes:
                # check if confidence is greater than 40 percent
                if box.conf[0] > 0.2:
                    # get coordinates using xyxy
                    [x1, y1, x2, y2] = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # get the class in its numeral ID format
                    cls = int(box.cls[0])

                    # get the class name using the ID
                    class_name = names[cls]

                    # get the  bounding box and text colour for the class
                    colour = getColours(cls)

                    # draw the bounding box
                    cv.rectangle(img, (x1, y1), (x2, y2), colour, 2)

                    txt=f'{names[cls]} {box.conf[0]:.2f}'
                    # Calculate the text size
                    size = cv.getTextSize(txt, cv.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]

                    # to draw a filled rectangle behind the text
                    txt_x = x1
                    txt_y = y1  # Adjust y-coordinate for better positioning

                    # draw bounding box
                    cv.rectangle(img, (txt_x, txt_y - size[1] - 5), (txt_x + size[0], txt_y), colour, cv.FILLED)
                    # to specify class name and confidence on top of the bounding box
                    cv.putText(img , txt , (txt_x, txt_y), cv.FONT_HERSHEY_PLAIN, 1.0, 0, 2)
    
    # show the image
    cv.imshow('Object Detection', img)
    cv.waitKey(0)

# Video Object Detection
else:
    path=input("Specify the path of your video file: ")
    capture = cv.VideoCapture(path)
    while True:
        # reading each frame
        ret, frame = capture.read()
        if not ret:
            continue
        # for object tracking
        results = yolo.track(frame, stream=True)
        
        for result in results:
        # get the classes names
            names = result.names

            # looping over each box
            for box in result.boxes:

                # checking if confidence is greater than 40 percent
                if box.conf[0] > 0.4:
                    # get coordinates using xyxy 
                    [x1, y1, x2, y2] = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # get the class in its numeral ID format
                    cls = int(box.cls[0])

                    # get the class name using the ID
                    class_name = names[cls]

                    # get the  bounding box and text colour for the class
                    colour = getColours(cls)

                    # to draw the bounding box
                    cv.rectangle(frame, (x1, y1), (x2, y2), colour, 3)

                    txt=f'{names[cls]} {box.conf[0]:.2f}'
                    # Calculate the text size
                    size = cv.getTextSize(txt, cv.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]

                    # to draw a filled rectangle behind the text
                    txt_x = x1
                    txt_y = y1  # Adjust y-coordinate for better positioning

                    # draw bounding box
                    cv.rectangle(frame, (txt_x, txt_y - size[1] - 5), (txt_x + size[0], txt_y), colour, cv.FILLED)
                    # to specify class name and confidence on top of the bounding box
                    cv.putText(frame , txt , (txt_x, txt_y), cv.FONT_HERSHEY_PLAIN, 1.0, (255,255,255), 2)


        # defining the window name and size
        cv.namedWindow('Object Detection', cv.WINDOW_NORMAL)
        cv.resizeWindow('Object Detection',1500, 800)       
        # show the video frame
        cv.imshow('Object Detection', frame)

        # break the loop if 'd' is pressed
        if cv.waitKey(1) & 0xFF == ord('d'):
            break

    # release the video capture
    capture.release()
    # destroy all windows
    cv.destroyAllWindows()
