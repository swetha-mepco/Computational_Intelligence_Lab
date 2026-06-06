//Neural Multi layer Network
import math
import random

# -------- Activation --------
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)   # x is already sigmoid output

# -------- Forward Pass --------
def forward(x1, x2, weights):
    # Hidden layer
    h1 = sigmoid(x1*weights['w1'] + x2*weights['w2'] + weights['b1'])
    h2 = sigmoid(x1*weights['w3'] + x2*weights['w4'] + weights['b2'])

    # Output layer
    o1 = sigmoid(h1*weights['w5'] + h2*weights['w6'] + weights['b3'])

    return h1, h2, o1

# -------- Training (Backpropagation) --------
def train(X, Y, weights, alpha, epochs):
    for epoch in range(epochs):
        total_error = 0

        print(f"\nEpoch {epoch+1}")

        for i in range(len(X)):
            x1, x2 = X[i]
            target = Y[i]

            # Forward
            h1, h2, output = forward(x1, x2, weights)

            # Error
            error = target - output
            total_error += abs(error)

            # -------- Backpropagation --------
            # Output layer gradient
            d_output = error * sigmoid_derivative(output)

            # Hidden layer gradients
            d_h1 = d_output * weights['w5'] * sigmoid_derivative(h1)
            d_h2 = d_output * weights['w6'] * sigmoid_derivative(h2)

            # -------- Update Weights --------
            # Output layer
            weights['w5'] += alpha * d_output * h1
            weights['w6'] += alpha * d_output * h2
            weights['b3'] += alpha * d_output

            # Hidden layer
            weights['w1'] += alpha * d_h1 * x1
            weights['w2'] += alpha * d_h1 * x2
            weights['b1'] += alpha * d_h1

            weights['w3'] += alpha * d_h2 * x1
            weights['w4'] += alpha * d_h2 * x2
            weights['b2'] += alpha * d_h2

            print(f"Input:{X[i]} Target:{target} Output:{round(output,3)} Error:{round(error,3)}")

        if total_error < 0.01:
            print("\nConverged!")
            break

    return weights

# -------- Testing --------
def test(X, weights):
    print("\nTesting:")
    for x1, x2 in X:
        _, _, out = forward(x1, x2, weights)
        print(f"{(x1,x2)} -> {1 if out >= 0.5 else 0}")

# -------- MAIN --------
X = [(0,0), (0,1), (1,0), (1,1)]
Y = [0,1,1,0]   # XOR problem

# Initialize weights randomly
weights = {
    'w1': random.uniform(-1,1), 'w2': random.uniform(-1,1),
    'w3': random.uniform(-1,1), 'w4': random.uniform(-1,1),
    'w5': random.uniform(-1,1), 'w6': random.uniform(-1,1),
    'b1': random.uniform(-1,1), 'b2': random.uniform(-1,1),
    'b3': random.uniform(-1,1)
}

alpha = 0.5
epochs = 10000

weights = train(X, Y, weights, alpha, epochs)
test(X, weights)
