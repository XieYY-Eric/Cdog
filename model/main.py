import os
import sys
import logging #nice message
import numpy as np
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt #display image
import cv2 #for image resize
import tqdm #give a nice process bar visualization
import random
from collections import defaultdict
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

DATA_DIR = "./datas/"
IMG_SIZE = 255
NUM_CLASSES = 2
TEST_SIZE = 0.5
BATCH_SIZE = 64
NO_EPOCHS = 20


def label_pet_image_one_hot_encoder(img):
    pet = img.split('.')[-3]
    if pet == 'cat': return [1,0]
    elif pet == 'dog': return [0,1]

def process_data(data_image_list, DATA_FOLDER, isTrain=True):
    data_df = []
    for img in tqdm.tqdm(data_image_list):
        path = os.path.join(DATA_FOLDER,img)
        if(isTrain):
            label = label_pet_image_one_hot_encoder(img)
        else:
            label = img.split('.')[0]
        img = cv2.imread(path,cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        data_df.append([np.array(img),np.array(label)])
    random.shuffle(data_df)
    return data_df

def plot_image_list_count(data_image_list):
    labels = []
    categoral = defaultdict(int)
    for img in data_image_list:
        classname = img.split('.')[-3]
        categoral[classname] += 1
    df = pd.DataFrame.from_dict(categoral,orient='index')
    df.plot.bar()
    plt.show()

def show_images(data, isTest=False):
    f, ax = plt.subplots(5,5, figsize=(10,10))
    for i,data in enumerate(data[:25]):
        img_num = data[1]
        img_data = data[0]
        label = np.argmax(img_num)
        if label  == 1: 
            str_label='Dog'
        elif label == 0: 
            str_label='Cat'
        if(isTest):
            str_label="None"
        ax[i//5, i%5].imshow(img_data)
        ax[i//5, i%5].axis('off')
        ax[i//5, i%5].set_title("Label: {}".format(str_label))
    plt.show()

def plot_accuracy_and_loss(train_model):
    hist = train_model.history
    acc = hist['acc']
    val_acc = hist['val_acc']
    loss = hist['loss']
    val_loss = hist['val_loss']
    epochs = range(len(acc))
    f, ax = plt.subplots(1,2, figsize=(14,6))
    ax[0].plot(epochs, acc, 'g', label='Training accuracy')
    ax[0].plot(epochs, val_acc, 'r', label='Validation accuracy')
    ax[0].set_title('Training and validation accuracy')
    ax[0].legend()
    ax[1].plot(epochs, loss, 'g', label='Training loss')
    ax[1].plot(epochs, val_loss, 'r', label='Validation loss')
    ax[1].set_title('Training and validation loss')
    ax[1].legend()
    plt.show()


def main():
    print("hello world")
    
    if not os.path.exists(DATA_DIR):
        logging.error(f"{DATA_DIR} not found")
        exit()
    else:
        raw_data_file = os.path.join(DATA_DIR,"dogs-vs-cats")
        if os.path.exists(raw_data_file):
            logging.info("zip file found")
            test_dir = os.path.join(raw_data_file,"test1")
            train_dir = os.path.join(raw_data_file,"train")
            plot_image_list_count(os.listdir(train_dir))
            
            train = process_data(os.listdir(train_dir)[:100],train_dir)
            test = process_data(os.listdir(test_dir),test_dir,False)
            show_images(train)
            show_images(test,True)

            X, Y = zip(*train)
            X = np.array(X)
            X = [x.reshape(-1,IMG_SIZE,IMG_SIZE,3) for x in X]
            Y = np.array(Y)

            #use ResNet-50
            model = keras.Sequential()
            model.add(keras.applications.ResNet50(include_top=False,pooling='max'))
            model.add(keras.layers.Dense(NUM_CLASSES,activation="softmax"))
            model.layers[0].trainable = False
            model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
            model.summary()



            #prepare data for training
            X_train, X_val, y_train, y_val = train_test_split(X, Y, test_size=TEST_SIZE)
            
            #Train
            train_model = model.fit(X_train, y_train,
                  batch_size=BATCH_SIZE,
                  epochs=NO_EPOCHS,
                  verbose=1,
                  validation_data=(X_val, y_val))
            
            plot_accuracy_and_loss(train_model)

            score = model.evaluate(X_val, y_val, verbose=0)
            print('Validation loss:', score[0])
            print('Validation accuracy:', score[1])

            #get the predictions for the test data
            predicted_classes = model.predict_classes(X_val)
            #get the indices to be plotted
            y_true = np.argmax(y_val,axis=1)
            correct = np.nonzero(predicted_classes==y_true)[0]
            incorrect = np.nonzero(predicted_classes!=y_true)[0]
            target_names = ["Class {}:".format(i) for i in range(NUM_CLASSES)]
            print(classification_report(y_true, predicted_classes, target_names=target_names))
        
            f, ax = plt.subplots(5,5, figsize=(10,10))
            for i,data in enumerate(test[:25]):
                img_num = data[1]
                img_data = data[0]
                orig = img_data
                data = img_data.reshape(-1,IMG_SIZE,IMG_SIZE,3)
                model_out = model.predict([data])[0]
                
                if np.argmax(model_out) == 1: 
                    str_predicted='Dog'
                else: 
                    str_predicted='Cat'
                ax[i//5, i%5].imshow(orig)
                ax[i//5, i%5].axis('off')
                ax[i//5, i%5].set_title("Predicted:{}".format(str_predicted))    
            plt.show()
        else:
            logging.error("unable to find the zip files")
            exit()


if __name__ == "__main__":
    main()