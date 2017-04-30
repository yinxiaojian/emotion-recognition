from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.externals import joblib
import scipy.io as mat


class MySvm:
    train_vector = []
    target_vector = []
    ex_vector = []

    def feature_selection(self):
        # with open('data_vector.csv', 'r') as f:
        #     reader = csv.reader(f)
        #     vector = [row for row in reader]
        # use .mat replace .csv

        vector = mat.loadmat('module\\vector.mat')
        vector = vector['data']

        self.train_vector = vector[:, 0:34]
        self.target_vector = vector[:, 34:35]

        # print(vector)
        # print(train_vector)
        # print(target_vector)

        clf = ExtraTreesClassifier()
        clf = clf.fit(self.train_vector, self.target_vector.ravel())
        model = SelectFromModel(clf, threshold='1.25*mean', prefit=True)
        self.ex_vector = model.transform(self.train_vector)   # after extract

    def svm_train(self):
        clf = svm.SVC()
        clf.fit(self.ex_vector, self.target_vector.ravel())
        joblib.dump(clf, 'module\\train_model.m')
