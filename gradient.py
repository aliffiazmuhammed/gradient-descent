import numpy as np

def cubic_equation(a, b, c, d):
    #setting variables
    x = np.random.rand()
    learning_rate = 0.01
    n = 100

    #Stochastic Gradient Descent
    for i in range(n):
        
        grad = 3 * a * x**2 + 2 * b * x + c
        
        #applying ReLU
        grad = max(0, grad)

        # Update x using SGD
        x = x-learning_rate * grad

    return x

#reading and displaying inputs
print("Enter the coefficients a, b, c, d:")
a, b, c, d = map(int, input().split())

print(f"The Equation is {a}*x**3 + {b}*x**2 + {c}*x + {d}")

#calling function
solution = cubic_equation(a, b, c, d)

#result
print(f"The Solution for x is: {solution:.4f}")
