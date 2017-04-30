from sklearn import svm
X = [[0, 0], [2, 2]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
res = clf.predict([[2., 2.]])
print(res)
