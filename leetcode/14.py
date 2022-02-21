
strs = ["flower","flow","flight"]
strs_size = len(strs)
common_prefix = ""
found = False
for i in range(len(strs[0])):
    common_char = ""
    for j in range(strs_size):
        if len(strs[j]) <= i:
            found = True
            break
        if j == 0:
            common_char = strs[j][i]
        elif strs[j][i] != common_char:
            found = True
            break
    if found:
        break
    else:
        common_prefix += common_char

print(common_prefix)


