//K Nearest Neighbour

import math
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

class KNN:
    def __init__(self):
        self.train_data = [] # Stores [coords, label_index]
        self.test_data = []  # Stores [coords, actual_label_index]
        self.target_names = []
        self.k = 3 # Default K

    def load_sklearn_data(self, test_size=0.3):
        """Replaces read_input to get data from load_iris()"""
        iris = load_iris()
        self.target_names = iris.target_names

        # Split the data
        X_train, X_test, Y_train, Y_test = train_test_split(
            iris.data, iris.target, test_size=test_size
        )

        # Convert to the list format used by your manual functions
        self.train_data = [[X_train[i], Y_train[i]] for i in range(len(X_train))]
        self.test_data = [[X_test[i], Y_test[i]] for i in range(len(X_test))]
        return True

    def get_distance(self, x1, x2, method):
        """Manual distance calculation logic."""
        if method == 'e': # Euclidean
            return math.sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2)))
        elif method == 'm': # Manhattan
            return sum(abs(a - b) for a, b in zip(x1, x2))
        else: # Chebyshev
            return max(abs(a - b) for a, b in zip(x1, x2))

    def unweighted_vote(self, neighbors):
        vote_count = {}
        for _, label in neighbors:
            vote_count[label] = vote_count.get(label, 0) + 1
        return max(vote_count, key=vote_count.get)

    def weighted_vote(self, neighbors):
        vote_count = {}
        for d, label in neighbors:
            # weight = 1/d^2
            weight = 1 / (d**2) if d != 0 else 1000
            vote_count[label] = vote_count.get(label, 0) + weight
        return max(vote_count, key=vote_count.get)

    def run_prediction(self, dist_method, vote_method):
        predictions = []
        for test_point, _ in self.test_data:
            distances = []
            for train_point, label in self.train_data:
                d = self.get_distance(test_point, train_point, dist_method)
                distances.append((d, label))

            distances.sort(key=lambda x: x[0])
            neighbors = distances[:self.k]

            if vote_method == "weighted":
                predictions.append(self.weighted_vote(neighbors))
            else:
                predictions.append(self.unweighted_vote(neighbors))
        return np.array(predictions)

# --------- Main Execution Workflow ---------
knn = KNN()
# Load Iris instead of reading file
if knn.load_sklearn_data():
    while True:
        print("\n      KNN MENU: WEIGHTED VS UNWEIGHTED (IRIS DATA)")
        print("1. Start Classification\n2. Exit")

        choice = input("\nSelect Option: ")
        if choice == "2":
            print("Closing Program...\n")
            break

        if choice == "1":
            k_input = input(f"Enter K (Current {knn.k}): ")
            if k_input: knn.k = int(k_input)

            print("\nDistance Metric:\n1. Euclidean\n2. Manhattan\n3. Chebyshev")
            d_choice = int(input("Select (1-3): "))
            d_mode = {1: 'e', 2: 'm', 3: 'c'}.get(d_choice, 'e')

            print("\nVoting Mode:\n1. Unweighted\n2. Weighted")
            v_choice = int(input("Select (1-2): "))
            v_mode = "unweighted" if v_choice == 1 else "weighted"

            # Execute manual prediction loop
            y_pred = knn.run_prediction(d_mode, v_mode)
            y_actual = [item[1] for item in knn.test_data]

            print("\n" + "-"*65)
            print(f"{'No.':<4} | {'Actual Class':<15} | {'Predicted Class':<15} | {'Status'}")
            print("-" * 65)

            # Display results for test set
            for i in range(len(y_pred)):
                actual_name = knn.target_names[y_actual[i]]
                pred_name = knn.target_names[y_pred[i]]
                status = "CORRECT" if actual_name == pred_name else "WRONG"

                # Show all 45 test samples (Iris test size 30% of 150)
                print(f"{i+1:<4} | {actual_name:<15} | {pred_name:<15} | {status}")

            print("-" * 65)
            print("\n--- Performance Results ---")
            print(f"Accuracy:  {accuracy_score(y_actual, y_pred):.4f}")
            print(f"Precision: {precision_score(y_actual, y_pred, average='weighted'):.4f}")
            print(f"Recall:    {recall_score(y_actual, y_pred, average='weighted'):.4f}")
            print(f"F1 Score:  {f1_score(y_actual, y_pred, average='weighted'):.4f}")
            print("\nConfusion Matrix:\n", confusion_matrix(y_actual, y_pred))
