def longest_increasing_subsequence(sequence):
    longest = [] 
    current = []  
    
    for i in range(len(sequence)):
        #контрольна точка - друк поточного числа
        print(f"Обробляється число {sequence[i]}")
        
        if i == 0 or sequence[i] > sequence[i - 1]:
            current.append(sequence[i])  #додаємо число до поточної підпослідовності
        else:
            if len(current) > len(longest):
                longest = current  #оновлення найдовшої підпослідовності
            current = [sequence[i]]  #початок нової підпослідовності
        
        #контрольна точка - відображення поточної підпослідовності
        print(f"Поточна зростаюча підпослідовність: {current}")
    
    if len(current) > len(longest):
        longest = current  #оновлення найдовшої підпослідовності, якщо потрібно
    
    return longest

#зчитування послідовності чисел
numbers = list(map(int, input("Введіть послідовність чисел через пробіл: ").split()))

#контрольна точка - вхідні дані
print(f"Введена послідовність: {numbers}")

result = longest_increasing_subsequence(numbers)

print(f"Найдовша зростаюча підпослідовність: {result}")
