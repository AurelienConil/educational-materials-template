def calculate_area(length, width):
    area = length * width
    return area

##insert main function 
def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = calculate_area(length, width)
    print("The area of the rectangle is", area)

__main__ = main()