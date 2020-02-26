import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder, normalize
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def get_model():
    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(1000,)))
    model.add(Dropout(0.2))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.summary()
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

dataset = pd.read_csv('spam.csv', delimiter=',', encoding='latin-1')
print(dataset.head())
dataset = dataset.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1)
print(dataset.head())

X = dataset.v2
Y = dataset.v1

epochs = 20

le = LabelEncoder()
Y = le.fit_transform(Y)
tok = Tokenizer(num_words=1000, filters='[^A-Za-z]', lower=True, split=' ', char_level=False)
tok.fit_on_texts(X)
matrix_X = tok.texts_to_matrix(X, mode='count')
X = normalize(matrix_X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = get_model()
history = model.fit(X_train, Y_train, epochs=epochs, batch_size=32)

history = history.history
plt.style.use("ggplot")
fig, (ax1, ax2,) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

x = range(epochs)

ax1.plot(x, history['acc'], label='Accuracy')
ax1.legend(loc='lower right')

ax2.plot(x, history['loss'], label='Losses')
ax2.legend(loc='upper right')

plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Loss/Accuracy")
plt.legend()

fig.show()


print()
Y_predicted = model.predict_classes(X_test)

for i in range(len(X_test)):
    print('Predicted: ', Y_predicted[i], 'Should be: ', Y_test[i])
    print()

print(classification_report(Y_test, Y_predicted))