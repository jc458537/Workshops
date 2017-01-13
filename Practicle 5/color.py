__author__ = 'jc458537'
COLOR_NAME = {"#f0f8ff": "AliceBlue", "#faebd7": "AntiqueWhite", "#ffefdb": "AntiqueWhite1", "#eedfcc": "AntiqueWhite2",
              "#cdc0b0": "AntiqueWhite3", "	#8b8378": "AntiqueWhite4", "#7fffd4": "aquamarine1"}

for key in COLOR_NAME:
    # print(key,'is',Color[key])
    print('{} is {}'.format(key, COLOR_NAME[key]))
color = input("Enter color code: ")

while color != "":
    if color in COLOR_NAME:
        print(color, "is", COLOR_NAME[color])
    else:
        print("Invalid color code")
    color = input("Enter color code: ")
