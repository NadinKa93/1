
price_all = 0
while True:
    try:
        ticket_number = int(input('Введите количество билетов:\n'))
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age = (int(input('Введите возраст посетителя:\n')))
            if age < 18:
                print('Билет бесплатный')
            elif 18 <= age < 25:
                price_all += 990
                print('Стоимость билета: 990 рублей')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 рублей')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} рублей с учётом скидки 10% на полную стоимость заказа больше 3-х человек')
else:
    print(f'Сумма к оплате {price_all} рублей')



