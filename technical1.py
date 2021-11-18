# provide code that iterates in multiples of 7 up until 100, then in multiples of 8 up to 200, then multiples of 9 up to 300.
def itermultiples():
    for i in range(1, 101, 7):
        print(i)
    for i in range(1, 201, 8):
        print(i)
    for i in range(1, 301, 9):
        print(i)

itermultiples()