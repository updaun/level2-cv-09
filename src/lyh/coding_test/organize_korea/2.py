def HistogramArea(arr):
  max_height = max(arr)
  max_area = 0

  for h in range(1, max_height+1):
    temp_max = 0
    temp_cnt = 0
    for x in arr:
      if x >= h:
        temp_cnt += 1
      else:
        if temp_cnt * h > temp_max:
          temp_max = temp_cnt*h
        temp_cnt = 0
    if max_area < temp_max:
      max_area = temp_max
  # code goes here
  return max_area

# keep this function call here 
print(HistogramArea(input()))