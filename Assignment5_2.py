subjects = ["Americans","Indians"]
verbs = ["play","watch"]
objects = ["Baseball","Cricket"]

sentence = [s + " " + v + " " + o for s in subjects for v in verbs for o in objects]
for i in sentence:
    print(i)