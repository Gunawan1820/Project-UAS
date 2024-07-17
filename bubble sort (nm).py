def bubble_sort(numbers):
  is_sorted = False
  while not is_sorted:
    is_sorted = True
    for i in range(len(numbers) - 1):
      if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        is_sorted = False

  return numbers


if __name__ == "__main__":
  data = [5, 2, 4, 1, 3]
  print(f"Daftar sebelum diurutkan: {data}")

  sorted_data = bubble_sort(data)
  print(f"Daftar setelah diurutkan: {sorted_data}")
    