__author__ = 'jc458537'
scores = []
score = int(input("Score: "))
while score > 0:
    scores.append(score)
    score= int(input("Score: "))
if scores !=[]:
    print("your highest score is", max(scores))
