__author__ = 'jc458537'
num = 0
out_file = open("numbers.txt", "w")
while num >= 0:
    num = int(input("number:"))
    if num >= 0:
        print(str(num), file=out_file)
out_file.close()

