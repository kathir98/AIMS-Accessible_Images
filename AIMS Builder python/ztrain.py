from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsRetinaNet()
trainer.setDataDirectory(data_directory="G:\\train")
trainer.setTrainConfig(object_names_array=[ 'person',   'bicycle',   'car',   'motorcycle,   'airplane',
    'bus',   'train',   'truck',   'boat',   'traffic light',   'fire hydrant',   'stop_sign',
    'parking meter',   'bench',   'bird',   'cat',   'dog',   'horse',  'sheep',   'cow',   'elephant',   'bear',   'zebra',
    'giraffe',   'backpack',   'umbrella',   'handbag',   'tie',   'suitcase',   'frisbee',   'skis',   'snowboard',
    'sports ball',   'kite',   'baseball bat',   'baseball glove',   'skateboard',   'surfboard',   'tennis racket',
    'bottle',   'wine glass',   'cup',   'fork',   'knife',   'spoon',   'bowl',   'banana',   'apple',   'sandwich',   'orange',
    'broccoli',   'carrot',  'hot dog',   'pizza',   'donot',   'cake',   'chair',   'couch',   'potted plant',   'bed',
    'dining table',   'toilet',   'tv',   'laptop',   'mouse',   'remote',   'keyboard',   'cell phone',   'microwave',
    'oven',   'toaster',   'sink',   'refrigerator',   'book',   'clock',   'vase',   'scissors',   'teddy bear',  'hair dryer',
    'toothbrush'], batch_size=4, num_experiments=200)
trainer.trainModel()
