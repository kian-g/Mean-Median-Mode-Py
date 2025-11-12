data_pts = {}  # value: frequency


def print_options():
    print("(q)quit")
    print("(a)dd data points")
    print("(m)ean")
    print("(me)dian")
    print("(mo)de")


def add_data():
    print("(q) to quit")

    n = len(data_pts) + 1

    while True:
        pt = input(f"Data point {n}: ").lower()

        if pt == "q":
            break

        try:
            value = float(pt)
        except ValueError:
            pass

        else:
            n += 1
            # Use the data pt num as key and frequency as value
            if float(pt) in data_pts:
                data_pts[float(pt)] = data_pts[float(pt)] + 1
            else:
                data_pts[float(pt)] = 1


def mean():
    num_data = 0
    for val in data_pts.values():
        num_data += val

    num_sum = 0
    for key, val in data_pts.items():
        num_sum += key * val

    result = num_sum / num_data
    print(f"Mean: {result}")
    return result


def median():
    data_array = []

    for key, val in data_pts.items():
        data_array.extend([key] * val)

    data_array.sort()
    n = len(data_array)

    if n % 2 == 1:
        med = data_array[n // 2]

    else:
        med = (data_array[n // 2 - 1] + data_array[n // 2]) / 2

    print(f"Median: {med}")
    return med


def mode():
    modes = []
    max_freq = 0
    for val in data_pts.values():
        if val > max_freq:
            max_freq = val

    for key, val in data_pts.items():
        if val == max_freq:
            modes.append(key)

    print("Modes: ", end="")
    for mode in modes:
        print(mode, end=" ")
    print(end="\n")

    return modes


def print_not_enough_data():
    print("You need at least one data point! Try adding some data!")


while True:
    print_options()

    cmd = input("> ").lower()

    if cmd == "q":
        print("Quitting...")
        break

    if cmd == "a" or cmd == "add":
        add_data()

    if cmd == "m" or cmd == "mean":
        if len(data_pts) == 0:
            print_not_enough_data()
        else:
            mean()

    if cmd == "me" or cmd == "median":
        if len(data_pts) == 0:
            print_not_enough_data()
        else:
            median()

    if cmd == "mo" or cmd == "mode":
        if len(data_pts) == 0:
            print_not_enough_data()
        else:
            mode()
