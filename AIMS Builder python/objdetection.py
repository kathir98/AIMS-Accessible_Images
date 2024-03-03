import warnings

warnings.filterwarnings("ignore",category=FutureWarning)
warnings.filterwarnings("ignore")

from imageai.Detection import ObjectDetection
import os
import requests

def detectobj():
    allObjects =[]
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "C:\\Users\\kathi\\PycharmProjects\\AIMS\\venv\\static\\files\\image.jpg"), output_image_path=os.path.join(execution_path , "C:\\Users\\kathi\\PycharmProjects\\AIMS\\venv\\static\\files\\detectedobj\\imagenew.jpg"))
    for eachObject in detections:
        # print(eachObject["name"])
        allObjects.append(eachObject["name"])

    allObjectslist= list(dict.fromkeys(allObjects))
    # print(allObjectslist)
    values = {"value": "This image contains " +' '.join(allObjectslist)}
    # print(values['value'])
    return values['value']

    # url = "https://httpbin.org/post"
    # url = "http://localhost:5000/uploader"
    # r = requests.get(url=url, params=values)
    # print(r.content)



# detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), extract_detected_objects=True)

# print("-----")

