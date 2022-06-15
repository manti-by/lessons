from time import sleep


def regular_function():
    result = []
    for i in range(10):
        sleep(1)
        result.append(i)
    return result


def regular_generator():
    for i in range(10):
        sleep(1)
        yield i


if __name__ == "__main__":
    print("Run regular function")
    for item in regular_function():
        print(".", end="")

    print()

    print("Run regular generator")
    for item in regular_generator():
        print(".", end="")
