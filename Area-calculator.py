def  triangle(b, h):
    return 1/2 * b * h
def square(s):
    return s**2
def rectangle(w, h):
    return w * h
def circle(r):
    return 3.14 * (r **2)

print("What's the matter")
print("1.Triangle")
print("2.Square")
print("3.Rectangle")
print("4.Circle")

while True:
    method = input("Enter your choices: ")

    if method in ('1', '2', '3', '4'):
        if method == '1':
            b = int(input("Enter base: "))
            h = int(input("Enter height: "))
            print("Your area of Triangle is: ",triangle(b, h))
        if method == '2':
            s = int(input("Enter side: "))
            print("Your area of Square is: ",square(s))
        if method == '3':
            w = int(input("Enter Width: "))
            h = int(input("Enter Height: "))
            print("Your area of Rectangle is: ",rectangle(w, h))
        if method == '4':
            r = int(input("Enter Radius: "))
            print("Your area of circle is: ", circle(r))
    else: print("Invalid")
