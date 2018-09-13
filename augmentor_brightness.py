import cv2
import os

images_path = '../../dataset/RKB_v4/aligned/original/'
augmented_path = '../../dataset/RKB_v4/aligned/augmented/brightness/'
VALUE = 25

name = [n for n in os.listdir(images_path)]

for i in range (0, len(name)):
    files = [f for f in os.listdir(images_path + name[i])]

    if not os.path.exists(augmented_path + name[i]):
        os.makedirs(augmented_path + name[i])

    for j in range (0, len (files)):
        img = cv2.imread(images_path + name[i] + '/' + files[j]) #load rgb image
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
        
        if ((hsv[:,:,2]+VALUE) >= 255).any():
            hsv[:,:,2] -= VALUE
        else:
            hsv[:,:,2] += VALUE

        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imwrite(augmented_path + name[i] + '/' + files[j][:-4] + '_brightnessAugmented.png', img)
        print files[j][:-4] + '_brightnessAugmented.png', 'has been augmented'