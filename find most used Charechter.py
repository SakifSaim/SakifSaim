from pprint import pprint
sentene = "This is a common interview question"
char_fre = {}
for char in sentene:
    if char in char_fre:
        char_fre[char] += 1
    else:
        char_fre[char] = 1

char_fre_sorted = sorted(
    char_fre.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_fre_sorted[0])
