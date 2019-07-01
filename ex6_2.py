
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for mac_address in mac:
	temp = mac_address.split(':')
	mac_cisco.append('.'.join(temp))

print(mac)
print(mac_cisco)