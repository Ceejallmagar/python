import torch
import torch.nn as nn

print("--- Starting the Training Process ---\n")

# 1. THE DATA (The "Numbers" you provide)
# We give it X and y. The model doesn't know the formula y = 3x + 2 yet.
X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[5.0], [8.0], [11.0], [14.0], [17.0]])

# 2. THE MODEL (The "Blank Slate")
# We create a tiny neural network with just ONE neuron. 
# It has exactly 1 Weight (multiplier) and 1 Bias (adder).
model = nn.Linear(1, 1) 

# Let's see its random, untrained "brain" before we start:
print("Before training:")
print(f"Random Weight: {model.weight.item():.4f}")
print(f"Random Bias: {model.bias.item():.4f}\n")

# 3. THE GRADER AND THE ADJUSTER
# Loss function: Measures how wrong the model is (Mean Squared Error)
criterion = nn.MSELoss() 
# Optimizer: Adjusts the weights based on the error (Stochastic Gradient Descent)
# lr = 0.01 is the "learning rate" (how big of a step it takes to fix mistakes)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01) 

# 4. THE TRAINING LOOP (The "Practice")
epochs = 1000 # We will make it practice 1,000 times

for epoch in range(epochs):
    # --- FORWARD PASS (Make a guess) ---
    predictions = model(X)
    
    # --- CALCULATE LOSS (Grade the guess) ---
    loss = criterion(predictions, y)
    
    # --- BACKWARD PASS (Calculate how to fix the weights) ---
    optimizer.zero_grad() # Clear old gradients
    loss.backward()       # Calculate new gradients (the calculus part!)
    
    # --- OPTIMIZER STEP (Actually update the weights) ---
    optimizer.step()
    
    # Print progress every 200 epochs so we can watch it learn
    if (epoch + 1) % 200 == 0:
        print(f"Epoch {epoch+1}/1000 | Error (Loss): {loss.item():.4f}")

# 5. THE RESULT (What it "Stored")
print("\n--- Training Complete! ---")
final_weight = model.weight.item()
final_bias = model.bias.item()

print(f"Learned Weight (Multiplier): {final_weight:.2f}")
print(f"Learned Bias (Adder): {final_bias:.2f}")

# Let's test it with a number it has NEVER seen before!
new_X = torch.tensor([[10.0]])
prediction = model(new_X)
print(f"\nIf we ask the model for X = 10, it predicts: {prediction.item():.2f}")
print("(The actual math answer for 3(10) + 2 is 32)") 