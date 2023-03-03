# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a, b, *args, instructor="Colt", **kwargs):
  return [a, b, args, instructor, kwargs]

# display_info(1, 2, 3, last_name="Steele", job="Instructor")

print(display_info(1,2,3, last_name="Steele", job="Instructor"))

[1, 2, (3,), 'Colt', {'job': 'Instructor', 'last_name': 'Steele'}]

# When you have a tuple with one item - Python needs to distinguish between parenthesis and a tuple!