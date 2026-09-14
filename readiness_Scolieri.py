print("Hello, I am luigi scolieri, and my student ID is 2001366589.")


def mean_and_max(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum


numbers = [10, 20, 30, 40, 50]

mean, maximum = mean_and_max(numbers)

print("Numbers:", numbers)
print("Mean:", mean)
print("Maximum:", maximum)