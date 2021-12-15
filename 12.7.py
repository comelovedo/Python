per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Input amount of deposit: "))
deposit = [round(float(money * i / 100), 2) for i in list(per_cent.values())]
print(deposit)
print("Your deposit:", (money))
print("Maximum profit for your deposit", deposit)
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = float(input("Deposit amount:"))
# deposit = []
# for i in list(per_cent.values()):
#    deposit.append(float(money * i / 100))
# deposit = [round(float(money * i / 100), 2) for i in list(per_cent.values())]
#
# print("Your deposit is:", (money))
# print("Maximum profit for your deposit", deposit)
