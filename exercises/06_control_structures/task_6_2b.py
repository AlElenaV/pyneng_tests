# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ipaddr = input("Input IP address in format 10.0.1.1\n")
    try:
        list_ip = ipaddr.split(".")
        assert len(list_ip) == 4
        oct1 = int(ipaddr.split(".")[0])
        oct2 = int(ipaddr.split(".")[1])
        oct3 = int(ipaddr.split(".")[2])
        oct4 = int(ipaddr.split(".")[3])
        assert oct1 in range(0, 256)
        assert oct2 in range(0, 256)
        assert oct3 in range(0, 256)
        assert oct4 in range(0, 256)
    except:
        print("It is not IP address")
    else:
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
        break