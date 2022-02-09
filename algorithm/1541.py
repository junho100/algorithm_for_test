sen = input()
sen_dup = sen
sen_dup = sen_dup.replace("-", "+")
nums = sen_dup.split("+")
ops = []
for i in range(len(sen)):
    if sen[i] == "+" or sen[i] == "-":
        ops.append(sen[i])
def stripAndInt(i):
    i = i.lstrip("0")
    i = int(i)
    return i

nums = list(map(stripAndInt, nums))

result = nums.pop(0)

mode = True
for i in range(len(nums)):
    if ops[i] == "-":
        mode = False
    
    if mode == True:
        result += nums[i]
    else:
        result -= nums[i]

print(result)

