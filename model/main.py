import os
import sys
import logging
from tensorflow import keras
from tqdm import tqdm
import cv2
import random
from matplotlib import pyplot as plt #display image
import numpy as np

DATA_DIR = "./model/datas/"
KERAS_SAVE_MODEL = './model/datas/my_model.h5'

def main():

    if not os.path.exists(KERAS_SAVE_MODEL):
        logging.error(f"Couldn't located the model file {KERAS_SAVE_MODEL}")
        exit()
    
    model = keras.models.load_model(KERAS_SAVE_MODEL)

    
    raw_data_file = os.path.join(DATA_DIR,"dogs-vs-cats")
    if not os.path.exists(raw_data_file):
        logging.error(f"Couldn't located the model file {raw_data_file}, please download the data file")
        exit()
    test_dir = os.path.join(raw_data_file,"test1")

    data_df = []
    for img in tqdm(os.listdir(test_dir)):
        full_path = os.path.join(test_dir,img)
        label = img.split('.')[0]
        img = cv2.imread(full_path,cv2.IMREAD_COLOR)
        img = cv2.resize(img, (255,255))
        data_df.append([np.array(img), np.array(label)])
    random.shuffle(data_df)

    f, ax = plt.subplots(5,5, figsize=(10,10))
    for i,data in enumerate(data_df[:25]):
        img_num = data[1]
        img_data = data[0]
        orig = img_data
        data = img_data.reshape(-1,255,255,3)
        model_out = model.predict(data)[0]

        if np.argmax(model_out) == 1: 
            str_predicted='Dog'
        else: 
            str_predicted='Cat'

        ax[i//5, i%5].imshow(orig)
        ax[i//5, i%5].axis('off')
        ax[i//5, i%5].set_title("Pred:{}".format(str_predicted)) 

    plt.show()

    

if __name__ == "__main__":
    main()