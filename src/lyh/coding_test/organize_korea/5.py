def ArrayRotation(arr):
  # code goes here
  rotate_idx = arr[0]
  new_arr = arr[rotate_idx:] + arr[:rotate_idx]

  return ''.join(str(x) for x in new_arr)

# keep this function call here 
print(ArrayRotation(input()))