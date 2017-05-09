import scipy.io as mat
import getattr
import csv
import os


def generate_vector():
    # n vector
    # data = mat.loadmat('data\\EDA.mat')
    # vector = getattr.get_vector(data['data'])   # feature vector
    # vector.append(1)
    # with open('data_vector.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows([vector])
    # print(vector)
    # vector = [vector, vector]
    # mat.savemat('model\\vector.mat', {'data': vector})

    happy = []
    normal = []
    sad_h = []
    sad_n = []
    path_dir = os.listdir('data\\happy')
    for file in path_dir:
        full_name = os.path.join('data\\happy', file)
        with open(full_name, 'r') as f:
            reader = csv.reader(f)
            vector = [int(row[0]) for row in reader]
            vector = getattr.get_vector(vector)
            vector.append(1)
        happy.append(vector)

    path_dir = os.listdir('data\\normal')
    for file in path_dir:
        full_name = os.path.join('data\\normal', file)
        with open(full_name, 'r') as f:
            reader = csv.reader(f)
            vector = [int(row[0]) for row in reader]
            vector = getattr.get_vector(vector)
            vector.append(2)
        normal.append(vector)

    path_dir = os.listdir('data\\sad')
    for file in path_dir:
        full_name = os.path.join('data\\sad', file)
        with open(full_name, 'r') as f:
            reader = csv.reader(f)
            vector = [int(row[0]) for row in reader]
            vector_h = getattr.get_vector(vector)
            vector_n = getattr.get_vector(vector)
            vector_h.append(2)
            vector_n.append(3)
        sad_h.append(vector_h)
        sad_n.append(vector_n)

    # save vector as csv, happy_other\normal_sad
    with open('model\\happy_other.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(happy+normal+sad_h)

    with open('model\\normal_sad.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(normal+sad_n)

