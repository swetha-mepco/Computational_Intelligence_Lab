//Decision Tree
import pandas as pd
import math

# ---------------- LOAD DATASET ----------------
data = pd.read_csv("dataset.csv")

# Remove Day column since it is just an ID
if "Day" in data.columns:
    data = data.drop(columns=["Day"])

print("\n================ DATASET ================\n")
print(data)

target_column = data.columns[-1]

# ---------------- ENTROPY ----------------
def entropy(column, print_steps=False):
    values = column.value_counts()
    total = len(column)
    ent = 0

    if print_steps:
        print("\nEntropy Calculation:")

    for value, count in values.items():
        p = count / total

        if print_steps:
            print(f"P({value}) = {count}/{total} = {round(p,4)}")

        ent -= p * math.log2(p)

    if print_steps:
        print("Entropy =", round(ent, 4))

    return ent

# ----------- INFORMATION GAIN -------------
def information_gain(data, attribute, print_steps=False):

    if print_steps:
        print("\n========================================")
        print(f"Calculating Information Gain for '{attribute}'")
        print("========================================")

    total_entropy = entropy(data[target_column], print_steps)
    weighted_entropy = 0

    for value in data[attribute].unique():

        subset = data[data[attribute] == value]

        if print_steps:
            print(f"\nSubset where {attribute} = {value}")

        sub_entropy = entropy(subset[target_column], print_steps)

        weight = len(subset) / len(data)
        weighted_entropy += weight * sub_entropy

        if print_steps:
            print(f"Weighted Entropy = {round(weight,4)} × {round(sub_entropy,4)}")

    ig = total_entropy - weighted_entropy

    if print_steps:
        print(f"\nInformation Gain ({attribute}) = {round(ig,4)}")

    return ig


def find_best_attribute_entropy(data, print_steps=False):

    attributes = data.columns[:-1]
    gains = {}

    for attribute in attributes:
        gains[attribute] = information_gain(data, attribute, print_steps)

    best_attr = max(gains, key=gains.get)

    if print_steps:
        print("\nInformation Gain Summary:")
        for k, v in gains.items():
            print(k, ":", round(v, 4))

        print("\nRoot Node (Entropy):", best_attr)

    return best_attr


# ---------------- GINI INDEX ----------------
def gini_index(column, print_steps=False):

    values = column.value_counts()
    total = len(column)
    gini = 1

    if print_steps:
        print("\nGini Index Calculation:")

    for value, count in values.items():

        p = count / total

        if print_steps:
            print(f"P({value}) = {count}/{total} = {round(p,4)}")

        gini -= p ** 2

    if print_steps:
        print("Gini Index =", round(gini, 4))

    return gini


# ---------------- GINI GAIN ----------------
def gini_gain(data, attribute, print_steps=False):

    if print_steps:
        print("\n========================================")
        print(f"Calculating Gini Gain for '{attribute}'")
        print("========================================")

    total_gini = gini_index(data[target_column], print_steps)
    weighted_gini = 0

    for value in data[attribute].unique():

        subset = data[data[attribute] == value]

        if print_steps:
            print(f"\nSubset where {attribute} = {value}")

        sub_gini = gini_index(subset[target_column], print_steps)

        weight = len(subset) / len(data)
        weighted_gini += weight * sub_gini

        if print_steps:
            print(f"Weighted Gini = {round(weight,4)} × {round(sub_gini,4)}")

    g_gain = total_gini - weighted_gini

    if print_steps:
        print(f"\nGini Impurity Reduction ({attribute}) = {round(g_gain,4)}")

    return g_gain


def find_best_attribute_gini(data, print_steps=False):

    attributes = data.columns[:-1]
    gains = {}

    for attribute in attributes:
        gains[attribute] = gini_gain(data, attribute, print_steps)

    best_attr = max(gains, key=gains.get)

    if print_steps:
        print("\nGini Gain Summary:")
        for k, v in gains.items():
            print(k, ":", round(v, 4))

        print("\nRoot Node (Gini):", best_attr)

    return best_attr

# ---------------- PRINT DECISION TREE ----------------
def build_tree(data, method="entropy", depth=0):
    target_values = data[target_column]

    # Leaf if all examples have same class
    if len(target_values.unique()) == 1:
        print("  " * depth + "Leaf:", target_values.iloc[0])
        return

    # Leaf if no attributes left
    if len(data.columns) == 1:
        majority = target_values.mode()[0]
        print("  " * depth + "Leaf:", majority)
        return

    # Choose best attribute based on method
    if method == "entropy":
        best_attr = find_best_attribute_entropy(data)
    elif method == "gini":
        best_attr = find_best_attribute_gini(data)
    else:
        raise ValueError("Method must be 'entropy' or 'gini'")

    print("  " * depth + f"[{best_attr}]")

    for value in data[best_attr].unique():
        print("  " * depth + f" ├── {value}")
        subset = data[data[best_attr] == value].drop(columns=[best_attr])
        build_tree(subset, method=method, depth=depth+1)

# ---------------- EXECUTION ----------------

print("\n\n============= STEP 1: TOTAL ENTROPY & GINI =============")
entropy(data[target_column], print_steps=True)
gini_index(data[target_column], print_steps=True)

print("\n\n============= STEP 2: INFORMATION GAIN (ENTROPY) =============")
find_best_attribute_entropy(data, print_steps=True)

print("\n\n============= STEP 3: GINI GAIN (IMPURITY REDUCTION) =============")
find_best_attribute_gini(data, print_steps=True)

print("\n\n============= STEP 4: FINAL DECISION TREE (ENTROPY) =============")
build_tree(data, method="entropy")

print("\n\n============= STEP 5: FINAL DECISION TREE (GINI) =============")
build_tree(data, method="gini")


