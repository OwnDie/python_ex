
access_template = ['switchport mode access',
				   'switchport access vlan {}',
				   'switchport nonegotiate',
				   'spannig-tree portfast',
				   'spannig-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
				  'switchport mode trunk',
				  'switchport trunk allowed vlan {}']

interface_mode_template = { 'access': access_template, 'trunk': trunk_template}
interface_mode_vlan = { 'access': 'Enter VLAN number: ', 'trunk': 'Enter allowed VLANs: '}

interface_mode = input('Enter interface mode (access/trunk): ')
interface_type_number = input('Enter interface type and number: ')
vlan = input(interface_mode_vlan.get(interface_mode))

print('\ninterface {}'.format(interface_type_number))
print("\n".join(interface_mode_template.get(interface_mode)).format(vlan))