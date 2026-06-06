//Ensemble Classifier
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder

# 1. Load your own dataset
file_path = input("Enter the path to your CSV file: ").strip()
df = pd.read_csv(file_path)

print("\nColumns available:", df.columns.tolist())
target_col = input("Enter the name of the target (label) column: ").strip()

# Prepare features (X) and target (y)
X = df.drop(columns=[target_col])
y = df[target_col]

# Convert categorical targets to numbers (e.g., 'Small' -> 0)
if y.dtype == 'object':
    le = LabelEncoder()
    y = le.fit_transform(y)

# Take user input for Model Parameters
criterion_choice = input("Enter criterion (gini / entropy): ").strip().lower()
if criterion_choice not in ["gini", "entropy"]:
    print("Invalid choice! Defaulting to 'gini'")
    criterion_choice = "gini"

n_trees = int(input("Enter number of trees: "))

# Define splits
split_ratios = [0.30, 0.40, 0.25]  
split_names = ["70-30", "60-40", "75-25"]
final_results = []

for i in range(len(split_ratios)):
    print(f"\n{'='*30}\nSplit: {split_names[i]}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=split_ratios[i], random_state=42
    )

    # Initialize and Train
    rf = RandomForestClassifier(
        n_estimators=n_trees,
        criterion=criterion_choice,
        random_state=42
    )
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    # Metrics
    accuracy = round(accuracy_score(y_test, y_pred), 4)
    precision = round(precision_score(y_test, y_pred, average='weighted', zero_division=0), 4)
    recall = round(recall_score(y_test, y_pred, average='weighted', zero_division=0), 4)
    f1 = round(f1_score(y_test, y_pred, average='weighted', zero_division=0), 4)

    print(f"Accuracy : {accuracy}\nF1 Score : {f1}")
    final_results.append([split_names[i], accuracy, precision, recall, f1])    

print("\n\nFinal Consolidated Results:")
print("Split   Accuracy  Precision  Recall   F1-Score")
for row in final_results:
    print(f"{row[0]:6}   {row[1]:8}   {row[2]:8}   {row[3]:8}   {row[4]:8}")
