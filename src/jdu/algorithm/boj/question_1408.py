import sys
sh, sm, ss = list(map(int, sys.stdin.readline().split(":")))
eh, em, es = list(map(int, sys.stdin.readline().split(":")))
start = sh*60*60 + sm *60 + ss
end = eh*60*60 + em *60 + es
target = end - start
# 내가 놓친 부분
if target < 0:
    target += 60*60*24
th, tm = divmod(target, 3600)
tm, ts = divmod(tm, 60)
print(f'{str(th).zfill(2)}:{str(tm).zfill(2)}:{str(ts).zfill(2)}')