import ast
from sklearn import svm,model_selection
import numpy as np

fileIn = open("../Features/ftr_dmoz.txt",'r')

features = []
labels = []

for line in fileIn:
	features.append(ast.literal_eval(line)[0])
	labels.append(ast.literal_eval(line)[1])

features = np.array(features)
labels = np.array(labels)

X_train, X_test, y_train, y_test = model_selection.train_test_split(features, labels, test_size=0.2)

clf = svm.SVC()
clf.fit(X_train,y_train)
score = clf.score(X_test,y_test)

print(score)

