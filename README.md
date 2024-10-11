**OBJECT DETECTION USING OPENCV AND YOLO**

__OVERVIEW__  
This project uses the YOLOv8 model to detect and track objects. Users can input an image or a video file, and the program will output the detected objects, bounding boxes, and confidence scores.  

__REQUIREMENTS__  
To configure the environment, it is required to install the following:  
Python: Download and install from python.org.  
Visual Studio Code can be downloaded and installed directly from code.visualstudio.com.  

__INSTALLATION__  
After installing Python and VSCode, open command prompt (or terminal) and run:  

pip install opencv-contrib-python  
pip install ultralytics  
pip install random  

__USAGE__  
1.Launch Visual Studio Code and open the project.  
2.Launch the Python program. A choice between an image and a video will be presented.  
3.Specify the location of the picture or video file.  
4.The application will print the data(number and name of objects detected) in the console and show the identified objects with bounding boxes containing information about class name and confidence scores.  

__EXAMPLE OUTPUT IN CONSOLE__  
1. Image Object Detection

python detect_objects.py  
Input 1 for image object detection and 2 for video object detection: 1  
Specify the path of your image: pic3.jpg  

image 1/1 C:\Users\dell\OneDrive\Documents\OpenCV files\object\pic3.jpg: 352x640 15 persons, 14 cars, 1 bus, 2 trucks, 228.2ms  
Speed: 18.0ms preprocess, 228.2ms inference, 20.4ms postprocess per image at shape (1, 3, 352, 640)  

2. Video Object Detection

python detect_objects.py  
Input 1 for image object detection and 2 for video object detection: 2  
Specify the path of your video file: vid.mp4  

0: 384x640 2 persons, 2 cars, 1 truck, 133.5ms
Speed: 5.0ms preprocess, 133.5ms inference, 2.0ms postprocess per image at shape (1, 3, 384, 640)

0: 384x640 1 person, 3 cars, 207.4ms
Speed: 14.8ms preprocess, 207.4ms inference, 2.7ms postprocess per image at shape (1, 3, 384, 640)

0: 384x640 1 person, 2 cars, 123.8ms
Speed: 7.6ms preprocess, 123.8ms inference, 0.0ms postprocess per image at shape (1, 3, 384, 640)

0: 384x640 1 person, 4 cars, 153.8ms
Speed: 2.8ms preprocess, 153.8ms inference, 2.1ms postprocess per image at shape (1, 3, 384, 640)  

After pressing 'd', the video stops and the window gets closed.  

__VISUAL OUTPUT__  
A window will display the modified image or video with the detected objects.  

__CONCLUSION__  
This project demonstrates the YOLOv8 model's potent real-time object detection and tracking capabilities in both images and videos. Users can quickly implement and test object detection in their own applications by following the setup and usage instructions.
