array = [int(x) for x in input("Input numbers from 1 to 999 in any order, separated by a space: ").split()]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input("Input a number to set the element's position: "))

while True:
    try:
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("You have to input numbers")
    except Exception:
        print("Incorrect range")

print(binary_search(array, element, 0, len(array)))
