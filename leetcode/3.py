'''
Sliding Window
'''

s = "abcabcbb"

char_map = [0] * 128
left = right = 0
result = 0

while right < len(s):
    right_char = s[right]
    char_map[ord(right_char)] += 1

    while char_map[ord(right_char)] > 1:
        left_char = s[left]
        char_map[ord(left_char)] -= 1
        left += 1

    result = max(result, right - left + 1)
    right += 1

print(result)