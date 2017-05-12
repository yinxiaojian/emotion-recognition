import os
import re
import generatevector
import getattr
import database
import time
import serial
from my_svm import MySvm
from sklearn.externals import joblib
import matplotlib.pyplot as plt


def train_module():
    if os.path.isfile('model\\happy_model.m'):
        print('The model already exists, do you want to retrain it?')
        print('1:skip 2:retrain')

        choice = input()
        while (choice != '1') and (choice != '2'):
            print('error input, please retry')
            choice = input()
        if choice == '1':
            print('use last model')
            return
    print("training... please waiting")
    generatevector.generate_vector()
    mysvm = MySvm()
    mysvm.feature_selection()
    mysvm.svm_train()
    print('training finish, use last model')


def predict_result():
    ser = serial.Serial(  # 下面这些参数根据情况修改
        port='COM6',
        baudrate=1200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    serial_data = []
    plt.xlim(0, 100)
    plt.ylim(300, 700)
    plt.title('GSR')
    plt.ion()
    i = 0
    j = 0
    id = 0
    while True:
        line = ser.readline()
        line = int(line)
        serial_data.append(line)
        if i > 100:
            plt.xlim(i - 100, i)
        plt.plot(serial_data)
        i += 1
        j += 1
        if j >= 50:
            clf = joblib.load('model\\happy_model.m')
            select = joblib.load('model\\vector_select.m')
            vector = getattr.get_vector(serial_data)
            new_vector = select.transform(vector)
            print(new_vector)
            result = clf.predict(new_vector)
            if result[0] == '2':
                clf = joblib.load('model\\sad_model.m')
                result = clf.predict(new_vector)
            j = 0
            plt.plot([i, i], [300, 700], 'r--')
            if result[0] == '1':
                plt.annotate('happy', xy=(i, 600), xytext=(i - 10, 600), arrowprops=dict(facecolor='red', shrink=0.05))
                res = 1
                database.insert(id, res)
            elif result[0] == '2':
                plt.annotate('normal', xy=(i, 600), xytext=(i - 10, 600), arrowprops=dict(facecolor='blue', shrink=0.05))
                res = 0
                database.insert(id, res)
            else:
                plt.annotate('sad', xy=(i, 600), xytext=(i - 10, 600),arrowprops=dict(facecolor='black', shrink=0.05))
                res = 2
                database.insert(id, res)
            print(result)
            id += 1
        plt.pause(0.001)


if __name__ == '__main__':
    # train_module()
    database.connect()
    predict_result()

