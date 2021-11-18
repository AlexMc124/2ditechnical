# provide code that iterates in multiples of 7 up until 100, then in multiples of 8 up to 200, then multiples of 9 up to 300.
def itermultiples():
    for i in range(1, 100, 7):
        print(i)
    for i in range(1, 200, 8):
        print(i)
    for i in range(1, 300, 9):
        print(i)

itermultiples()

# code that prints multiples of 7 until 100, then multiples of 8 up to 200, then multiples of 9 up to 300.
def itermultiples2():
    x = 0
    while x < 100:
        print(x)
        x += 7
    while x < 200: 
        print(x)
        x += 8
    while x < 300:
        print(x)
        x += 9
        
itermultiples2()