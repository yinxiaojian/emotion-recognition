from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.externals import joblib
import scipy.io as mat
import csv
import numpy as np


class MySvm:
    train_vector_happy = []
    target_vector_happy = []
    train_vector_sad = []
    target_vector_sad = []
    ex_vector_happy = []
    ex_vector_sad = []

    def feature_selection(self):
        # use .csv replace .mat
        # vector = mat.loadmat('model\\vector.mat')
        # vector = vector['data']

        with open('model\\happy_other.csv', 'r') as f:
            reader = csv.reader(f)
            vector_happy = []
            for line in reader:
                for i in range(len(line) - 1):
                    line[i] = float(line[i])
                vector_happy.append(line)
        vector_happy = np.array(vector_happy)
        print(vector_happy)
        with open('model\\normal_sad.csv', 'r') as f:
            reader = csv.reader(f)
            vector_sad = []
            for line in reader:
                for i in range(len(line) - 1):
                    line[i] = float(line[i])
                vector_sad.append(line)
        vector_sad = np.array(vector_sad)

        self.train_vector_happy = vector_happy[:, 0:28]
        self.target_vector_happy = vector_happy[:, 28:29]
        self.train_vector_sad = vector_sad[:, 0:28]
        self.target_vector_sad = vector_sad[:, 28:29]

        clf = ExtraTreesClassifier()
        clf = clf.fit(self.train_vector_happy, self.target_vector_happy.ravel())
        model = SelectFromModel(clf, threshold='1.25*mean', prefit=True)
        joblib.dump(model, 'model\\vector_select.m')

        self.ex_vector_happy = model.transform(self.train_vector_happy)   # after extract
        print(self.ex_vector_happy)
        self.ex_vector_sad = model.transform(self.train_vector_sad)  # after extract

    def svm_train(self):
        clf = svm.SVC()
        clf.fit(self.ex_vector_happy, self.target_vector_happy.ravel())
        joblib.dump(clf, 'model\\happy_model.m')
        clf.fit(self.ex_vector_sad, self.target_vector_sad.ravel())
        joblib.dump(clf, 'model\\sad_model.m')

