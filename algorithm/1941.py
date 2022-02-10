result = 0
sentence = input()
words = ["c=", "c-", "dz=", "d-", "lj", "nj", 's=', "z="]
for word in words:
    result += sentence.count(word)
    sentence = sentence.replace(word, "+")

for i in sentence:
    if i != "+":
        result += 1

print(result)