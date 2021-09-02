import pickle
import random
traffic=[]
with open("network.txt", "rb") as fp: 
	network = pickle.load(fp)
my_probability=0
while my_probability<0.9:
	my_probability=random.random()
hotspot=int(random.random()*len(network))
hotspot_probability=0
while hotspot_probability<0.2 or hotspot_probability>0.3:
	hotspot_probability=random.random()
first_node=[x for x in network if random.random() < my_probability]

for i in range(len(first_node)):
	num_here=network[i][0]
	num_there=num_here
	while num_here == num_there:
		rand_here=random.random()
		if rand_here<hotspot_probability:
			second_node = hotspot
		else:
			second_node = int(rand_here*len(network))
		num_there=network[second_node][0]
	if len(first_node[i])==7:
		traffic.append([ first_node[i][1],first_node[i][2],network[second_node][1],network[second_node][2] ])
	elif len(first_node[i])==10:
		traffic.append([ first_node[i][1],first_node[i][2],first_node[i][3],network[second_node][1],network[second_node][2],network[second_node][3] ])
with open('traffic_hotspot.txt', 'w') as f:
	for i in range(len(traffic)):
		if len(traffic[i])==4:
			f.writelines(str(traffic[i][0]) + '\t' +  str(traffic[i][1]) + '\t' + str(traffic[i][2]) + '\t' + str(traffic[i][3]) + '\n')
		if len(traffic[i])==6:
			f.writelines(str(traffic[i][0]) + '\t' +  str(traffic[i][1]) + '\t' + str(traffic[i][2]) + '\t' + str(traffic[i][3]) + '\t' + str(traffic[i][4]) + '\t' + str(traffic[i][5]) + '\n')
