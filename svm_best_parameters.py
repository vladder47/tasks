from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
import csv
import numpy as np

x = []
y = []
with open('soybean-large.data', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        temp = []
        for elem in line[1:]:
            if elem != '?':
                temp.append(int(elem))
            else:
                temp.append(0)
        x.append(temp)
        y.append(line[0])

C = [i for i in np.arange(0.1, 5.0, 0.1)]
gamma = [i for i in np.arange(0.1, 5.0, 0.1)]
degree = [2, 3, 4]
#kernel = ['linear', 'poly', 'rbf', 'sigmoid']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
svm_model = SVC(kernel='linear')

gs_clf = GridSearchCV(svm_model, param_grid={'C': C})
gs_clf.fit(x_train, y_train)
best_cv_err = 1 - gs_clf.best_score_
best_param_c = gs_clf.best_estimator_.C
# best_param_gamma = gs_clf.best_estimator_.gamma

print('############################')
print('SVM-модель с линейным ядром:')
print('Значение ошибки перекрестного контроля: ', best_cv_err)
print('Наилучшее значение параметра C:', best_param_c)

svm_model = SVC(kernel='linear', C=best_param_c)
svm_model.fit(x_train, y_train)
err_train = np.mean(y_train != svm_model.predict(x_train))
err_test = np.mean(y_test != svm_model.predict(x_test))
print('Ошибка на обучающей выборке:', err_train)
print('Ошибка на тестовой выборке:', err_test)

y_pred = svm_model.predict(x_test)
print(classification_report(y_test, y_pred, zero_division=0))
print('############################')
