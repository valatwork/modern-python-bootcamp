# example 1

def sum_all_values(*args):
    total = 0
    for val in args:
        total += val

    return total

sum_all_values(1, 2, 3) # 6

sum_all_values(1, 2, 3, 4, 5) # 15

# example 2

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"

    return "Not sure who you are..."

ensure_correct_info() # Not sure who you are...

ensure_correct_info(1, True, "Steele", "Colt")