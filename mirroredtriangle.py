n = int(input("How many rows do you want for the mirrored triangle: "))

i = 1
try :
    def mirrored_triangle(n):
        for i in range(1, n + 1):
            s = ' ' * (n - i)
            print(s , end = '')
            shape = '*' * i
            print(shape)

except (ValueError , NameError) :
    print("the input must be integer or in numerical form " )

mirrored_triangle(n)