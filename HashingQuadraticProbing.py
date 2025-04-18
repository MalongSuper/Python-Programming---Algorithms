# This program implements Hashing (Quadratic Probing)
import numpy as np
import matplotlib.pyplot as plt
# Initialize N
number = 100


# Create a hash function of your choice
def hash_function(key):
    return key % number


# Quadratic Probing Function
def insert(key, hash_table):
    miss = 0
    index = hash_function(key)
    i = 1
    while hash_table[index] != 0:
        index = (index + (i ** 2)) % number
        miss += 1
        i += 1
    hash_table[index] = key
    return miss


def main():
    print("Hashing (Quadratic Probing)")
    # Create an array of 100 random numbers
    keys = np.random.randint(1, 1000, 100)
    hash_table = np.zeros(number)
    misses = []
    for key in keys:
        m = insert(key, hash_table)
        misses.append(m)
    print("Hash Tables:\n", hash_table)
    # Convert misses list to array
    print("Misses:\n", np.array(misses))
    # Plot a graph of the load factor and the number of collisions
    x = np.arange(number)
    plt.title("Variation of the number of collisions in Quadratic Probing")
    plt.xlabel("Keys")
    plt.ylabel("Collisions")
    plt.plot(x, misses)
    plt.show()


main()
