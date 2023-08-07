# Write your solution here

import string, random


def generate_password(length):
    a = string.ascii_lowercase
    password = ""

    while len(password) < length:
        randch = a[random.randint(0, len(a) - 1)]
        password += randch
    return password


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
