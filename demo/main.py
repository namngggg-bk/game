import math

def calculate_area(radius):
    if radius < 0:
        print("Radius cannot be negative!")
        return None
    return math.pi * radius * radius

def greet_user(name):
    print(f"Hello, {name}")  # Lỗi: thiếu kiểm tra nếu `name` là None.

# Gọi hàm
print(calculate_area(-5))  # Lỗi: giá trị âm không hợp lệ.
greet_user(None)  # Lỗi: Truyền giá trị None vào chuỗi.
