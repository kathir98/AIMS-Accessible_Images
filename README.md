# AIMS-Accessible_Images

This project makes images accessible to visually impaired persons by helping developers in creating alternate text (alt text) to images using machine learning and embeeded it into images via AIMS builder module which are used in website during the developement. Then in turn in Visually impaired users side, alternate text is extracted from images present in website then translated into user preferred lamguage and updated in the alt attribute of image tag using chrome extension (AIMS browser extension) which can be easily read by screen readers.

It contains 2 modules, 
i) AIMS Builder
ii) AIMS browser extension

## AIMS Builder
- AIMS builder is the web application which gets the image as the input from the user and sends the data to the python flask server.
- Flask server performs object detection and returns the detected objects.
- Input image and detected objects are embedded into the image using the LSB steganography algorithm.
- Then finally we got the annotated image as the output which can be downloaded and used on web pages.  



  ![image](https://github.com/kathir98/AIMS-Accessible_Images/assets/61177402/792da0bc-1513-46a6-b955-b33b3ac0afd6)

  #### *<ins>Note </ins>: I'm using ImageAI python library to perfrom object detection using already trained "resnet50_coco_best_v2.0.1.h5" module.*
  #### *You can train your own ML module or use resnet module (resnet50_coco_best_v2.0.1.h5) which I used by downloading it from internet.*


  ## AIMS Extension

- AIMS browser extension main functionality is to extract the embedded message from the image.
- AIMS extension also gets the user preferred language as input and translates the extracted message as per the user preferences.
- The detailed flow of the AIMS browser extension is given as below.  



  ![image](https://github.com/kathir98/AIMS-Accessible_Images/assets/61177402/1431126f-d700-4308-b31d-a19c0b828405)  

  
  1 - VI user surfs the websites
  
  2 - Image src is passed to extension as input
  
  3 - The embedded message is decoded from the image and the language user chosen is sent to the flask server
  
  4 - The flask server translates the embedded message as per the user preference and returns the result to the extension
  
  5 - Extension set alt attribute to the image tags


  ## How to run it?

  - First run the AIMS builder flask app which gives you UI to create annonated (embeeded) images.
  - Then run AIMS extenson flask app which performs the trasnlation and update the alt text.

  Note : you can test the same using the test website - Mediumish created using annotated images by running the simple local php/python server.

  #### *Detialed descreption document is present in Document folder, feel free to check it out..*
  
