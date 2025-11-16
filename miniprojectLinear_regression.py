import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([2, 4, 5, 4, 5, 7, 8, 9])

# 1. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 2. Create & Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Predictions
y_pred = model.predict(X_test)

# 4. Check performance
print("Slope (coefficient):", model.coef_)
print("Intercept:", model.intercept_)
print("R² Score:", r2_score(y_test, y_pred))

# 5. Plotting
plt.scatter(X, y, label="Data Points")
plt.plot(X, model.predict(X), label="Regression Line")
plt.xlabel("X Values")
plt.ylabel("Target (y)")
plt.title("Linear Regression using Scikit-learn")
plt.legend()
plt.show()
