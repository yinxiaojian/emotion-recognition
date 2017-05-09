import os
import generatevector
from my_svm import MySvm
from sklearn.externals import joblib
import numpy as np

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
    clf = joblib.load('model\\happy_model.m')
    select = joblib.load('model\\vector_select.m')
    vector = [[933.333333333,4.5,3068.7153483,1,11111,11110,0.0833333333333,925.916666667,1010.0,1.0,3192.39061178,-50,11105,11155,-4.54545454545,1009.54545455,1019.27272727,0.332149649474,1110.5,1.0,3331.7255064,-100,11105,11205,-10.0,1110.5,1131.5,0.3687210678]]
    new_vector = select.transform(vector)
    print(new_vector)
    result = clf.predict(new_vector)
    print(result)


if __name__ == '__main__':
    train_module()
    predict_result()

