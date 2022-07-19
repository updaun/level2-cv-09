import sys
input_word = sys.stdin.readline().rstrip()
suffix = [input_word]
for i in range(1, len(input_word)):
    suffix.append(input_word[i:])
print("\n".join(map(str, sorted(suffix))))
