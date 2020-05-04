# Copyright 2020 NXP Semiconductors
# SPDX-License-Identifier: BSD-3-Clause

import os
import time

import cv2 as opencv
import numpy as np
from tflite_runtime.interpreter import Interpreter

from eiq.tflite.inference import inference
from eiq.tflite.ssd.utils import *

class eIQObjectDetectionImage(object):
    def __init__(self):
        
    # end this    
        
    def run_detection(image, interpreter):
        interpreter.set_tensor(input_details[0]['index'], image)

        inference(interpreter)

        boxes = interpreter.get_tensor(output_details[0]['index'])
        classes = interpreter.get_tensor(output_details[1]['index'])
        scores = interpreter.get_tensor(output_details[2]['index'])
        num = interpreter.get_tensor(output_details[3]['index'])

        boxes, scores, classes = np.squeeze(boxes), np.squeeze(scores), np.squeeze(classes + 1).astype(np.int32)
        out_scores, out_boxes, out_classes = non_max_suppression(scores, boxes, classes)
                
        return out_scores, out_boxes, out_classes

    def image_object_detection(interpreter, colors):
        image = opencv.imread('images/dog.jpg')
        image_data = preprocess_image_for_tflite(image, model_image_size=300)
        out_scores, out_boxes, out_classes = run_detection(image_data, interpreter)

        result = draw_boxes(image, out_scores, out_boxes, out_classes, class_names, colors)
        opencv.imwrite(os.path.join("out", "ssdlite_mobilenet_v2_dog.jpg"), result, [opencv.IMWRITE_JPEG_QUALITY, 90])
        
    def real_time_object_detection(interpreter, colors):
        camera = cv2.VideoCapture(0)

        while camera.isOpened():
            start = time.time()
            ret, frame = camera.read() 

            if ret:
                image_data = preprocess_image_for_tflite(frame, model_image_size=300)
                out_scores, out_boxes, out_classes = run_detection(image_data, interpreter)
                # Draw bounding boxes on the image file
                result = draw_boxes(frame, out_scores, out_boxes, out_classes, class_names, colors)
                end = time.time()

                # fps
                t = end - start
                fps  = "Fps: {:.2f}".format(1 / t)
                cv2.putText(result, fps, (10, 30),
		                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            
                cv2.imshow("Object detection - ssdlite_mobilenet_v2", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Load TFLite model and allocate tensors.
    interpreter = Interpreter(model_path="model_data/ssdlite_mobilenet_v2.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # label
    class_names = read_classes('model_data/coco_classes.txt')
    # Generate colors for drawing bounding boxes.
    colors = generate_colors(class_names)
    
    ## TWO WAYS, IMAGE AND VIDEO   
    image_object_detection(interpreter, colors)
    #real_time_object_detection(interpreter, colors)
