import cv2
import numpy as np



def detectPersons(img_path):
    #load YOLO
    net = cv2.dnn.readNet("./yolov3.weights", "./yolov3.cfg")

    classes = []

    with open("./yolov3.txt", 'r') as f:
        classes = f.read().splitlines()

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

    #loading image

    img = cv2.imread(img_path)
    #img = cv2.resize(img, None, fx = 0.4, fy = 0.4)
    height, width, channels = img.shape
    #Detecting objects

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416,416), (0,0,0), True, crop = False)
    for b in blob:
        for n, img_blob in enumerate(b):
            cv2.imshow(str(n), img_blob)

    net.setInput(blob)
    outs = net.forward(output_layers)

    #Showing informations on the screen
    boxes = []
    confidences = []
    class_ids = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                #Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Recangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    numberof_object_detected = len(boxes)
    numberof_person_detected = 0
    font = cv2.FONT_HERSHEY_PLAIN
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,0.4)
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            #draw rectangle and count only if object is person
            if class_ids[i] == 0:
                label = str(classes[class_ids[i]])+str(round(confidences[i],3))
                cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),2)
                #cv2.putText(img,label,(x,y),font,1,(0,0,0),3)
                numberof_person_detected+=1
    #print(numberof_object_detected)
    #print(numberof_person_detected)
    outputs = {}
    if numberof_person_detected > 0:
        outputs['detections']={}
        outputs['detections']['labels']=[]
        numberof_person_detected = 1
        for i in indexes.flatten():
            if class_ids[i]==0:
                detection = {}
                detection['Number of person'] = numberof_person_detected
                detection['Label']=classes[class_ids[i]]
                detection['Confidence'] = round(confidences[i],3)
                detection['X'] = boxes[i][0]
                detection['Y'] = boxes[i][1]
                detection['Width'] = boxes[i][2]
                detection['Height'] = boxes[i][3]
                outputs['detections']['labels'].append(detection)
                numberof_person_detected+=1
    else:
        outputs['detections'] = 'No person detected'
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return outputs
