def check_decorator(func):
    def wrapper():
        print("\n" + "="*30)
        print(func(payment_amount, payment_method, for_payment, purchases, user))
        print("="*30 + "\n")
    return wrapper
@check_decorator
def check(pay_amo, pay_met, for_pay, pur, username):
    print('Спасибо за покупку в кафе "IT кафешка"! Вот ваш чек:')
    print(f'Username покупателя: {username}')
    print('Приобретённые товары:')
    global cofe
    global sandwich
    global double_sandwich
    global dobry_pepsy
    global pancakes
    cofe = pur.count(1)
    sandwich = pur.count(2)
    double_sandwich = pur.count(3)
    dobry_pepsy = pur.count(4)
    pancakes = pur.count(5)
    if cofe > 0:
        print(f'Кофе - {cofe} шт')
    if sandwich > 0:
        print(f'Бутеры - {sandwich} шт')
    if double_sandwich > 0:
        print(f'Двойные бутеры - {double_sandwich} шт')
    if dobry_pepsy > 0:
        print(f'Газировка "Добрый-пепси" - {dobry_pepsy} шт')
    if pancakes > 0:
        print(f'Блинчики - {pancakes} шт')
    if pay_met == 1:
        print(f'Метод оплаты: наличная')
        print(f'К оплате: {for_pay} монет')
        print(f'Отдано: {pay_amo} монет')
        print(f'Сдача: {pay_amo - for_pay} монет')
    elif pay_met == 2:
        print(f'Метод оплаты: безналичная (банковской картой)')
        print(f'Оплачено товаров на: {for_pay} монет')
    print(f'Номер чека: потом сделаю')
    print('Приходите ещё!')
user = input('Введите ваш username:')
products = {1:'кофе', 2:'бутер', 3:'двойной бутер', 4:'добрый-пепси', 5:'бличики'}
prices = {1:10, 2:10, 3:18, 4:14, 5:20}
purchases = []
choice = 0
print('Выберите продукты для покупки: 1 - Кофе (цена 10 монет)    2 - Бутер (цена 10 монет)    3 - Двойной бутер (цена 18 монет)    4 - Газировка "Добрый-пепси" (цена 14 монет)    5 - Бличики (цена 20 монет), для завершения выбора введите 0')
while True:
    try:
        choice = int(input('Номер товара:'))
        if choice == 0:
            break
        if choice > 5:
            a = 1/0
        purchases.append(choice)
    except:
        print("Ошибка ввода, повторите попытку")
for_payment = 0
for _ in purchases:
    for_payment += prices.get(_)
print('Выберите способ оплаты: 1 - наличная     2 - безналичная')
while True:
    try:
        payment_method = int(input('Номер метода оплаты:'))
        if payment_method == 1:
            payment_amount = int(input('Сколько отдать монет?:'))
            if payment_amount < for_payment:
                a = 1/0
        elif payment_method == 2:
            payment_amount = for_payment
        else:
            a = 1/0
        break
    except:
        print('Ошибка ввода, повторите попытку')
print(check())
with open("logs.txt", "a") as file:
    file.write(f'Username: {str(user)}')
    file.write(f'\nPayment method: {str(payment_method)}')
    file.write(f'\nFor payment: {str(for_payment)}')
    file.write(f'\nChange: {str(payment_amount - for_payment)}')
    file.write('\nGoods:')
    file.write(f'\nCofe {str(cofe)}')
    file.write(f'\nSandwich {str(sandwich)}')
    file.write(f'\nDouble sandwich {str(double_sandwich)}')
    file.write(f'\ndobry_pepsy {str(dobry_pepsy)}')
    file.write(f'\nPancakes {str(pancakes)}')
    file.write('\n')
    file.write('\n')