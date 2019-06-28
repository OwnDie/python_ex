


ip_address = input('Please input network and mask (example 10.1.1.0/24): ')

ip_address_out = ip_address.split('/')
network = ip_address_out[0].split('.')
mask_decimial = int(ip_address_out[1])

network[0] = int(network[0])
network[1] = int(network[1])
network[2] = int(network[2])
network[3] = int(network[3])

print('''Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}\n'''.format(network[0],network[1],network[2],network[3]))

mask = '1' * mask_decimial + '0' * (32 - mask_decimial)
mask_list = [int(mask[0:8],2),int(mask[8:16],2),int(mask[16:24],2),int(mask[24:32],2)]

print('''Mask:
/{0}
{1:<8d}  {2:<8d}  {3:<8d}  {4:<8d}
{1:<08b}  {2:<08b}  {3:<08b}  {4:<08b}\n'''.format(mask_decimial,mask_list[0],mask_list[1],mask_list[2],mask_list[3])
	)