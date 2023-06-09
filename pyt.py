
sn_dict = {'11111': {'lan_ip': '1.1.1.1', 'oob_ip': '2.2.2.2'},
           '11112': {'lan_ip': '1.1.1.1', 'oob_ip': '2.2.2.2'}}

sn_dict.update({'11113': {'lan_ip': '1.1.1.1', 'oob_ip': '2.2.2.2'}})

for sn, ips in sn_dict.items():
    print(sn + "\t" + ips['lan_ip'] + "\t" + ips['oob_ip'])

data1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# filter
filtered = filter(lambda x: x > 50, data1)
data2 = list(filtered)
print(data2)

# map
maped = map(lambda x: x * 2, data1)
data3 = list(maped)
print(data3)

if __name__ == '__main__':
    print("hehe")
