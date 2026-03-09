# Trying to build a very small AI model (perceptron idea)
# Goal: make it understand which numbers are BIG and SMALL
# I'm just experimenting and learning here

data = [(1, 0), (2, 0), (8, 1), (9, 1)]  # (number, label) -> 1 = BIG , 0 = SMALL

w = 0.0   # weight (starting from 0)
b = 0.0   # bias
lr = 0.1  # learning rate

# training the model using the small dataset above
# repeating several times so it can adjust the weight
for _ in range(20):
    for x, y in data:

        # model prediction
        y_pred = 1 if (w * x + b) > 0 else 0

        # see how wrong it was
        error = y - y_pred

        # adjust parameters a little
        w += lr * error * x
        b += lr * error

# now testing the model with user input
state = True

print("\n=== BIG vs SMALL Predictor ===\n")

while state:
    try:
        print("Enter 0 if you want to stop\n")

        x = float(input("Enter a number: "))

        if x == 0:
            print("\nExiting the predictor. Bye!\n")
            break

        # model tries to guess
        y_pred = 1 if (w * x + b) > 0 else 0

        print("\nMy guess:", "BIG" if y_pred == 1 else "SMALL")
        print("\n")

    except ValueError:
        print("\nPlease enter a valid number\n")
        print("\n")