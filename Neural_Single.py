//Neural Single Layer Network
import math

def read_input():
    choice = input("Enter 1 for user input, 2 for file input: ")
    X, Y = [], []
    if choice == '1':
        n = int(input("Enter number of samples: "))
        for i in range(n):
            x1 = int(input(f"Sample {i+1} x1: "))
            x2 = int(input(f"Sample {i+1} x2: "))
            y = int(input(f"Sample {i+1} target: "))
            X.append((x1, x2)); Y.append(y)
    elif choice == '2':
        filename = input("Enter file name: ")
        with open(filename, 'r') as f:
            for line in f:
                x1, x2, y = map(int, line.split())
                X.append((x1, x2)); Y.append(y)
    else:
        X, Y = [(0,0), (0,1), (1,0), (1,1)], [0, 0, 0, 1]
    return X, Y

def net_input(x1, x2, w1, w2, theta):
    return (x1 * w1) + (x2 * w2) + theta

def activation(net, choice):
    if choice == 1: return 1 if net >= 0 else 0
    elif choice == 2: return 1 / (1 + math.exp(-net))
    elif choice == 3: return math.tanh(net)
    return 1 if net >= 0 else 0

def update(w1, w2, theta, alpha, error, x1, x2):
    w1 += alpha * error * x1
    w2 += alpha * error * x2
    theta += alpha * error
    return w1, w2, theta

def train(X, Y, w1, w2, alpha, theta, epochs, act_choice):
    for epoch in range(epochs):
        error_sum = 0
        print(f"\nEpoch {epoch+1}")
        for i in range(len(X)):
            x1, x2 = X[i]
            net = net_input(x1, x2, w1, w2, theta)
            out = activation(net, act_choice)
            if act_choice != 1:
                output = 1 if out >= 0.5 else 0
            else:
                output = out
            error = Y[i] - output
            error_sum += abs(error)
            w1, w2, theta = update(w1, w2, theta, alpha, error, x1, x2)
            print(f"Input:{X[i]} Target:{Y[i]} Output:{output} Error:{error}")
        if error_sum == 0:
            print(f"\nConverged in {epoch+1} epochs")
            break
    return w1, w2, theta

def display(w1, w2, theta):
    print(f"\nFinal Weights: W1={w1}, W2={w2}, Theta={theta}")

X_data, Y_data = read_input()

print("\n--- Set Initial Parameters ---")
init_w1 = float(input("Enter initial w1: "))
init_w2 = float(input("Enter initial w2: "))
alpha = float(input("Enter learning rate (alpha): "))
theta_val = float(input("Enter threshold (theta): "))
max_epochs = int(input("Enter max epochs: "))

while True:
    print("\n--- Activation Menu ---")
    print("1. Step\n2. Sigmoid\n3. Tanh\n4. Exit")
    act_choice = int(input("Enter choice: "))

    if act_choice == 4:
        break

    if act_choice in [1, 2, 3]:
        # Reset to initial weights for a fresh run with the new activation
        w1, w2, theta = train(X_data, Y_data, init_w1, init_w2, alpha, theta_val, max_epochs, act_choice)

        display(w1, w2, theta)
        print("\nTesting:")
        for x1, x2 in X_data:
            net = net_input(x1, x2, w1, w2, theta)
            out = activation(net, act_choice)
            if act_choice != 1: out = 1 if out >= 0.5 else 0
            print(f"{(x1, x2)} -> {out}")
    else:
        print("Invalid choice!")
