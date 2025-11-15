class LinearRegressionScratch:
    def __init__(self, lr=0.01, iterations=1000):
        self.lr = lr
        self.iterations = iterations
        self.theta0 = 0
        self.theta1 = 0

    def predict(self, x):
        return self.theta0 + self.theta1 * x

    def cost_function(self, X, Y):
        m = len(X)
        total_error = 0
        for i in range(m):
            total_error += (self.predict(X[i]) - Y[i]) ** 2
        return total_error / (2 * m)

    def gradient_descent(self, X, Y):
        m = len(X)
        for _ in range(self.iterations):
            sum_error_theta0 = 0
            sum_error_theta1 = 0

            for i in range(m):
                prediction = self.predict(X[i])
                error = prediction - Y[i]
                sum_error_theta0 += error
                sum_error_theta1 += error * X[i]

            # Update rules
            self.theta0 -= self.lr * (sum_error_theta0 / m)
            self.theta1 -= self.lr * (sum_error_theta1 / m)

    def train(self, X, Y):
        self.gradient_descent(X, Y)
        return self.theta0, self.theta1

if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]

    model = LinearRegressionScratch(lr=0.01, iterations=1000)
    theta0, theta1 = model.train(X, Y)

    print("Theta0 (intercept):", theta0)
    print("Theta1 (slope):", theta1)

    # Test prediction
    print("Prediction for x=7:", model.predict(7))
