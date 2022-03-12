# object_detection
This repo contains two files related to object detection.

The first is a jupyter notebook, named _**obj_det.ipynb**_, which takes coin images and augments them to result in a larger training and testing dataset. It also uses thresholding to detect object location and crops the original image so that the resulting image is a zoomed in version of the original image.

The second file is named _**video_coin_identifier.py**_. It is python script for detecting and identifying coins in a video frame. It utilizes OpenCV functions to label US coins that come into the video frame. Results will vary based on camera height from the coins, but a user may update sizing based on the height of their own camera from the coins.
   
   - The camera used for this exercise was an iphone which was working as an IP camera through the app called 'IP camera Lite'
      - The IP address was then used as the source for the video feed being accessed by the python script.
      - The IP camera app requires a username and password which can be inputted as: 'rtsp://username:password@your_rtsp_ip_address'

   - This code can also be copied to a raspberry pi and can use a different camera input by changing the source for the video capture.
