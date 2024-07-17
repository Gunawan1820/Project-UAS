def bubble_sort(numbers):
  is_sorted = False
  while not is_sorted:
    is_sorted = True
    for i in range(len(numbers) - 1):
      if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        is_sorted = False
        
  return numbers

data = []
num_inputs = int(input("Masukkan jumlah angka yang ingin diurutkan: "))

for i in range(num_inputs):
  number = float(input(f"Masukkan angka ke-{i+1}: "))
  data.append(number)

print(f"Daftar sebelum diurutkan: {data}")
sorted_data = bubble_sort(data)
print(f"Daftar setelah diurutkan: {sorted_data}")
