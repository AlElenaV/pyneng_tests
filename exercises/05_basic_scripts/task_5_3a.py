# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

int_mode = input("Введите режим работы интерфейса (access/trunk):\t")
n_int = input("Введите тип и номер интерфейса:\t")
print("="*50)
if int_mode == 'access':
    n_vlan = input("Введите номер VLAN:\t")
else:
    n_vlan = input("Введите разрешенные VLANы:\t")
print('Interface {}'.format(n_int))
if int_mode == 'access':
    print(''.join("""
    switchport mode access
    switchport access vlan {n_vlan}
    switchport nonegotiate
    spanning-tree portfast
    spanning-tree bpduguard enable""".format(n_vlan=n_vlan)))
else:
    print(''.join("""
    switchport trunk encapsulation dot1q
    switchport mode trunk
    switchport trunk allowed vlan {n_vlan}""".format(n_vlan=n_vlan)))
