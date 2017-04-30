import os
import generatevector
from my_svm import MySvm


def train_module():
    if os.path.isfile('butter.py'):
        print('The model already exists, do you want to retrain it?')
        print('1:retain 2:skip')
    choice = input()
    while (choice != '1') and (choice != '2'):
        choice = input()
        print('error input, please retry')
    if choice == '1':
        print('use last module')
        return
    print("training... please waiting")
    generatevector.generate_vector()
    mysvm = MySvm()
    mysvm.feature_selection()
    mysvm.svm_train()
    print('training finish, use last module')

if __name__ == '__main__':
    train_module()
