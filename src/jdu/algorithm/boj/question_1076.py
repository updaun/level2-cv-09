import sys
register = {
    'black':'0',
    'brown':'1',
    'red':'2',
    'orange':'3',
    'yellow':'4',
    'green':'5',
    'blue':'6',
    'violet':'7',
    'grey':'8',
    'white':'9',
}
register_value = ''
for i in range(2):
    register_value += register[sys.stdin.readline().rstrip()]
print(int(register_value)* 10**int(register[sys.stdin.readline().rstrip()]))