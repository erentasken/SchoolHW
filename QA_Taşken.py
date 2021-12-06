range_ = int(input("How many words are you going to enter?\n"))
boolCheck = True
print("Enter the words.\n")
for i in range(range_):
    wordInp = input("")
    if boolCheck:
        min = wordInp
        boolCheck = False
        continue
    control = True
    if control:
        for j in range(1000):
            if ord(wordInp[j].lower()) > ord(min[j].lower()):
                control = False
                break
            elif ord(wordInp[j].lower()) == ord(min[j].lower()):
                continue
            else:
                min = wordInp
                control = False
                break

print(f"The first word alphabetically is {min}.")
