A=[-4561,-68892]


def add(x, y):
    return [x[0] + y[0], x[1] + y[1]]

def multiply(x, y):
    return [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]]

def divide(x, y):
    return [int(x[0] / y[0]), int(x[1] / y[1])]

def result_to_string(result):
    return f"[{result[0]},{result[1]}]"

def draw_point(a):
    result = [0, 0]
    for i in range(100):
        result = multiply(result, result)
        result = divide(result, [100000,100000])
        result = add(result, a)
        if abs(result[0]) > 1000000 or abs(result[1]) > 1000000:
            return False
    return abs(result[0]) <= 1000000 or abs(result[1]) <= 1000000

def do_process(a):
    print(f"Processing: {a}")
    total_points = 0
    for y in range(101):
        for x in range(101):
            if draw_point([a[0] + x * 10, a[1] + y * 10]):
                total_points += 1
    print(f"Total points: {total_points}")

def main():
    do_process([35300,-64910])
    do_process(A)

if __name__ == "__main__":
    main()