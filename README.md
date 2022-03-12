# object_detection
This repo contains two files related to object detection.
The first is a jupyter notebook which takes coin images and augments them to result in a larger training and testing dataset.

The second file is python script for detecting and identifying coins in a video frame. It utilizes OpenCV functions and results will vary based on camera height from the coins. 
   
   - The camera used for this exercise was an iphone which was working as an IP camera through the app called 'IP camera Lite'
      - The IP address was then used as the source for the video feed being accessed by the python script.
      - The IP camera app requires a username and password which can be inputted as: 'rtsp://username:password@your_rtsp_ip_address'
    - This code can also be copied to a raspberry pi and can use different camera inputs by changing the source for the video capture.
