#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/27

'''{'nic': {'status': True, 'data': {
    'eth0': {'up': True, 'hwaddr': '00:1c:42:a5:57:7a', 'ipaddrs': '10.211.55.4', 'netmask': '255.255.255.0'}},
         'error_msg': None}, 
    'disk': {'status': True, 'data': {
    '0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'},
    '1': {'slot': '1', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'},
    '2': {'slot': '2', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1SZNSAFA01085L     Samsung SSD 850 PRO 512GB               EXM01B6Q'},
    '3': {'slot': '3', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1AXNSAF912433K     Samsung SSD 840 PRO Series              DXM06B0Q'},
    '4': {'slot': '4', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1AXNSAF303909M     Samsung SSD 840 PRO Series              DXM05B0Q'},
    '5': {'slot': '5', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1AXNSAFB00549A     Samsung SSD 840 PRO Series              DXM06B0Q'}}, 'error_msg': None},
    'basic': {'status': True,
           'data': {'os_platform': 'linux', 'os_version': 'CentOS release 6.6 (Final)\nKernel \r on an \\m',
                    'hostname': 'c1.com'}, 'error_msg': None}, 
    'board': {'status': True, 'data': {
    'manufacturer': 'Parallels Software International Inc.', 'model': 'Parallels Virtual Platform',
    'sn': 'Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30'}, 'error_msg': None}, 
    'memory': {'status': True,
               'data': {
                   'DIMM #0': {
                       'capacity': 1024,
                       'slot': 'DIMM #0',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'},
                   'DIMM #1': {
                       'capacity': 0,
                       'slot': 'DIMM #1',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'},
                   'DIMM #2': {
                       'capacity': 0,
                       'slot': 'DIMM #2',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'},
                   'DIMM #3': {
                       'capacity': 0,
                       'slot': 'DIMM #3',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'},
                   'DIMM #4': {
                       'capacity': 0,
                       'slot': 'DIMM #4',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'},
                   'DIMM #5': {
                       'capacity': 0,
                       'slot': 'DIMM #5',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'},
                   'DIMM #6': {
                       'capacity': 0,
                       'slot': 'DIMM #6',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'},
                   'DIMM #7': {
                       'capacity': 0,
                       'slot': 'DIMM #7',
                       'model': 'DRAM',
                       'speed': '667 MHz',
                       'manufacturer': 'Not Specified',
                       'sn': 'Not Specified'}},
               'error_msg': None}}'''

# disk_set = {}
s = {
    '0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'},
    '1': {'slot': '1', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'},
    '2': {'slot': '2', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1SZNSAFA01085L     Samsung SSD 850 PRO 512GB               EXM01B6Q'},
    '3': {'slot': '3', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1AXNSAF912433K     Samsung SSD 840 PRO Series              DXM06B0Q'},
    '4': {'slot': '4', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1AXNSAF303909M     Samsung SSD 840 PRO Series              DXM05B0Q'},
    '5': {'slot': '5', 'pd_type': 'SATA', 'capacity': '476.939',
          'model': 'S1AXNSAFB00549A     Samsung SSD 840 PRO Series'}
}
# a = {{'slot': 1, 'model': 'xx', 'capacity': 'xxx', 'pd_type': 'xx'},
#      {'slot': 2, 'model': 'xx', 'capacity': 'xxx', 'pd_type': 'xx'},
#      {'slot': 3, 'model': 'xx', 'capacity': 'xxx', 'pd_type': 'xx'},
#      {'slot': 9, 'model': 'xx', 'capacity': 'xxx', 'pd_type': 'xx'}}
# li = []
old_disk_set = {1,2,3,9}
new_disk_set = set()
for i in range(len(s)):
    new_disk_set.add(int(s[str(i)].get('slot')))
print(new_disk_set-old_disk_set)
print(old_disk_set-new_disk_set)
print(new_disk_set&old_disk_set)