a = 5
b = 10
print(f"Original: a={a}, b={b}")
a, b = b, a
print(f"Swapped:  a={a}, b={b}")

num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial: {factorial}")

n_terms = 10
n1, n2 = 0, 1
count = 0
print("Fibonacci:", end=" ")
while count < n_terms:
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print()

l = [1, 2, 3, 4, 5, 6, 7]
print(f"Length: {len(l)}")

print(f"Sum: {sum(l)}")

ar = [1, 2, 3, 4, 100, 6, 7]
print(f"Max: {max(ar)}, Min: {min(ar)}")

arr = [5, 100, 12, 20, 4, 99]
arr[0], arr[-1] = arr[-1], arr[0]
print(f"List after swap: {arr}")

students = [
    {"name": "Lara", "grades": [95, 88, 92]},
    {"name": "Omar", "grades": [75, 80, 72]},
    {"name": "Sara", "grades": [60, 55, 68]}
]

search_name = input("Enter student name: ")
found = False
for student in students:
    if student["name"].lower() == search_name.lower():
        avg = sum(student["grades"]) / len(student["grades"])
        print(f"Average: {avg:.2f}")
        if avg >= 90:
            print("Excellent!")
        elif 70 <= avg <= 89:
            print("Good job.")
        else:
            print("Needs improvement.")
        found = True
        break

if not found:
    print("Student not found.")

numbers = input("Input numbers: ")
list_res = numbers.split(",")
tuple_res = tuple(list_res)
print("List:", list_res)
print("Tuple:", tuple_res)