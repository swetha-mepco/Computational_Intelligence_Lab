//Bayes rule, Conditional and Marginal Probability
# Experiment No: 9
# Bayes Rule, Conditional and Marginal Probability

# -------------------------------
# Step 1: Read Joint Probability Table
# -------------------------------

def read_table():
    print("Enter joint probability table values")

    try:
        # Taking simple 2x2 table input
        p_a_b = float(input("Enter P(A and B): "))
        p_a_notb = float(input("Enter P(A and not B): "))
        p_nota_b = float(input("Enter P(not A and B): "))
        p_nota_notb = float(input("Enter P(not A and not B): "))

        total = p_a_b + p_a_notb + p_nota_b + p_nota_notb

        print("\nChecking total probability...")
        print("Total =", total)

        # Basic validation
        if total != 1:
            print("Error: Probabilities must sum to 1")
            return None

        return [p_a_b, p_a_notb, p_nota_b, p_nota_notb]

    except:
        print("Invalid input! Please enter numeric values only")
        return None


# -------------------------------
# Step 2: Marginal Probability
# -------------------------------

def marginal_prob(table):
    print("\nCalculating Marginal Probabilities...")

    p_a = table[0] + table[1]
    p_b = table[0] + table[2]

    print("P(A) = P(A and B) + P(A and not B)")
    print("P(A) =", p_a)

    print("P(B) = P(A and B) + P(not A and B)")
    print("P(B) =", p_b)

    return p_a, p_b


# -------------------------------
# Step 3: Conditional Probability
# -------------------------------

def conditional_prob(table, p_a, p_b):
    print("\nCalculating Conditional Probabilities...")

    if p_b != 0:
        p_a_given_b = table[0] / p_b
        print("P(A|B) = P(A and B) / P(B)")
        print("P(A|B) =", p_a_given_b)
    else:
        print("Cannot divide by zero for P(A|B)")
        p_a_given_b = 0

    if p_a != 0:
        p_b_given_a = table[0] / p_a
        print("P(B|A) = P(A and B) / P(A)")
        print("P(B|A) =", p_b_given_a)
    else:
        print("Cannot divide by zero for P(B|A)")
        p_b_given_a = 0

    return p_a_given_b, p_b_given_a


# -------------------------------
# Step 4: Bayes Rule
# -------------------------------

def bayes_rule(p_b_given_a, p_a, p_b):
    print("\nApplying Bayes Rule...")

    if p_b != 0:
        result = (p_b_given_a * p_a) / p_b
        print("P(A|B) using Bayes Rule = (P(B|A) * P(A)) / P(B)")
        print("Result =", result)
    else:
        print("Cannot apply Bayes Rule due to zero probability")
        result = 0

    return result


# -------------------------------
# MAIN PROGRAM
# -------------------------------

print("----- VALID INPUT TEST CASE -----")

table = read_table()

if table is not None:

    p_a, p_b = marginal_prob(table)

    p_a_given_b, p_b_given_a = conditional_prob(table, p_a, p_b)

    final_result = bayes_rule(p_b_given_a, p_a, p_b)


# -------------------------------
# INVALID TEST CASE
# -------------------------------

print("\n----- INVALID INPUT TEST CASE -----")

# manually giving wrong input (sum not equal to 1)
wrong_table = [0.5, 0.5, 0.5, 0.5]

total_wrong = 0
for i in range(len(wrong_table)):
    total_wrong = total_wrong + wrong_table[i]

print("Total of wrong table =", total_wrong)

if total_wrong != 1:
    print("Error detected: Invalid probability distribution")
