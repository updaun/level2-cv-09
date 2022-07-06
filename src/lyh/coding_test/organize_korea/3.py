def LongestConsecutive(arr):
  arr = list(set(arr))
  arr.sort()

  LCS = 0
  temp_num, temp_len = -99, 0
  for x in arr:
    if x == temp_num + 1:
      temp_len += 1
      temp_num += 1
    else:
      LCS = max(LCS, temp_len)
      temp_num = x
      temp_len = 1
  LCS = max(LCS, temp_len)

  return LCS

# keep this function call here 
print(LongestConsecutive(input()))