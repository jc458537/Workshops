__author__ = 'jc458537'
lower = 40
upper = 100
print("Enter a number (" + str(lower) + "-" + str(upper) + "): ")
str = "Enter a number({} + {}):".format(lower, upper)
print(str)


for i in range(lower, upper):
    print("{} {}".format(i, chr(i)))
for i in range(upper, lower):
    print("{} {}".format(i, chr(i)))