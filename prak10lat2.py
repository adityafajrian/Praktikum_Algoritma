def bubble_sort(data):
  for i in range(len(data) - 1, -1, -1):
    for j in range(i):
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]

  return data

data = [3, 1, 5, 2, 4]
sorted_data = bubble_sort(data)

print(sorted_data)
