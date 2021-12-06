range_ = int(input("How many words are you going to enter?\n"))
print("Enter the words.\n")
count1 = 0
firstInp = input("")
for i in range(len(firstInp)):
    if ord(firstInp[i]) == 69 or 101:
        count1 += 1
for n in range(range_-1):
    count2 = 0
    word = input("")
    for j in range(len(word)):
        if ord(word[j]) == 69 or 101:
            count2+=1
    if count2 > count1:
        firstInp = word
        count1 = count2
print(f"The word with the most Es is {firstInp}")
