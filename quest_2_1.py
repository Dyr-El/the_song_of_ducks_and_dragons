A=[164, 52]

def add(x, y):
    return [x[0] + y[0], x[1] + y[1]]

def multiply(x, y):
    return [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]]

def divide(x, y):
    return [x[0] // y[0], x[1] // y[1]]

def result_to_string(result):
    return f"[{result[0]},{result[1]}]"

def do_process(a):
    print(f"Processing: {a}")
    result = [0, 0]
    for i in range(3):
        result = multiply(result, result)
        print(f"Result: {result}")
        result = divide(result, [10, 10])
        print(f"Result: {result}")
        result = add(result, a)
        print(f"Result: {result_to_string(result)}")

def main():
    do_process([25, 9])
    do_process(A)

if __name__ == "__main__":
    main()