import scipy.io as mat
import getattr
import csv
# n vector
data = mat.loadmat('EDA.mat')
vector = getattr.get_vector(data['data'])   # feature vector
flag = 1    # Emotion marker: happy->1  sad->2
vector.append(1)
with open('data_vector.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([vector])
