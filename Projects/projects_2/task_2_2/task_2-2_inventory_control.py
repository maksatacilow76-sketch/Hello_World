reactive_name = input('Введите название необходимого реактива: ')
reactive_amount = int(input('Введите количество необходимого реактива (только целое число): '))


print(f'Реактив {reactive_name} поступил на склад в количестве {reactive_amount} шт.')
f = open('C:/Users/Михаил Чайка/Documents/Python/Chaika_mp/projects_2/task_2_2/inventory.txt', "w", encoding="utf-8")
print(f'Реактив {reactive_name} поступил на склад в количестве {reactive_amount} шт.', file=f)
f.close()