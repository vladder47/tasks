from keras.models import Sequential
from keras.layers import Dense
import numpy

numpy.random.seed(1)

X = numpy.array([[0,0], [0, 1], [1, 0], [1, 1]])
Y = numpy.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(2, input_dim=2, activation='sigmoid'))
model.add(Dense(6, activation="sigmoid"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
model.fit(X, Y, epochs=10000, batch_size=4)
scores = model.evaluate(X, Y)
print(model.metrics_names[0], scores[0])
print(model.metrics_names[1], scores[1])

X_predicted = numpy.array([[0,0], [1, 0]])
Y_predicted = model.predict_classes(X_predicted)

for i in range(len(X_predicted)):
    print("X=%s, Predicted=%s" % (X_predicted[i], Y_predicted[i]))