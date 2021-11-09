# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ipaddr = input("Input IP address in format 10.0.1.1\n")
oct1 = int(ipaddr.split(".")[0])

if oct1 in range(1, 224):
    print(f'{ipaddr} is unicast')
elif oct1 in range(224, 240):
    print(f'{ipaddr} is multicast')
elif ipaddr == "255.255.255.255":
    print(f'{ipaddr} is broadcast')
elif ipaddr == "0.0.0.0":
    print(f'{ipaddr} is unassigned')
else:
    print(f'{ipaddr} is unused')
