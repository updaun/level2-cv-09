import sys
input = sys.stdin.readline
books = dict()
for i in range(int(input())):
    name = input().rstrip()
    if name not in books.keys():
        books[name] = 1
    else:
        books[name] += 1
print(sorted(books, key=lambda x:(-books[x], x), reverse=True)[-1])

        