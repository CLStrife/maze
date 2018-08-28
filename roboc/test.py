import os

score = [1,2,3,4,5]
with open("save\save.txt", "w+") as f:
    for s in score:
        f.write(str(s) + "\n")

