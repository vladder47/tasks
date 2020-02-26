import numpy as np

#сигмоидальная функция активации
def sigmoid(x, deriv = False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

x = np.array([[0, 0] , [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

lr = 0.1
inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2, 4, 1

hidden_weights = np.random.uniform(size=(inputLayerNeurons, hiddenLayerNeurons))
hidden_bias = np.random.uniform(size=(1, hiddenLayerNeurons))
output_weights = np.random.uniform(size=(hiddenLayerNeurons, outputLayerNeurons))
output_bias = np.random.uniform(size=(1, outputLayerNeurons))

for iter in range(100000):
    hidden_layer_activation = np.dot(x, hidden_weights)
    hidden_layer_activation += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)

    output_layer_activation = np.dot(hidden_layer_output, output_weights)
    output_layer_activation += output_bias
    predicted_output = sigmoid(output_layer_activation)

    error = y - predicted_output
    d_predicted_output = error * sigmoid(predicted_output, deriv=True)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid(hidden_layer_output, deriv=True)

    output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    hidden_weights += x.T.dot(d_hidden_layer) * lr
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

print("Результаты обучения:")
print(predicted_output)

T = np.array([[1, 0]])
T_hidden = sigmoid(np.dot(T, hidden_weights))
T_exit = sigmoid(np.dot(T_hidden, output_weights))
print(T_exit)