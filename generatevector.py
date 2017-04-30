import scipy.io as mat
import getattr
import csv


def generate_vector():
    # n vector
    data = mat.loadmat('data\\EDA.mat')
    vector = getattr.get_vector(data['data'])   # feature vector
    flag = 1    # Emotion marker: happy->1  sad->2
    vector.append(1)
    # with open('data_vector.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows([vector])
    # print(vector)
    vector = [vector, vector]
    mat.savemat('module\\vector.mat', {'data': vector})
