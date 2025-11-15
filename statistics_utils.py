import math

class Stats:
    @staticmethod
    def mean(l):
        return sum(l) / len(l)

    @staticmethod
    def variance(l):
        mean_val = Stats.mean(l)
        return sum((i - mean_val) ** 2 for i in l) / len(l)

    @staticmethod
    def std_dev(l):
        return math.sqrt(Stats.variance(l))

    @staticmethod
    def covariance(x, y):
        if len(x) != len(y):
            raise ValueError("Lists must be of same length")

        mean_x = Stats.mean(x)
        mean_y = Stats.mean(y)

        temp = 0
        for i in range(len(x)):
            temp += (x[i] - mean_x) * (y[i] - mean_y)

        return temp / len(x)

    @staticmethod
    def correlation(x, y):
        return Stats.covariance(x, y) / (Stats.std_dev(x) * Stats.std_dev(y))


if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]

    print("Mean of X:", Stats.mean(X))
    print("Variance of X:", Stats.variance(X))
    print("Std Dev of X:", Stats.std_dev(X))
    print("Covariance:", Stats.covariance(X, Y))
    print("Correlation:", Stats.correlation(X, Y))
