import pickle
with open('input.txt', 'r') as myfile: 
	line = myfile.readline()
	while line:
		if line.find('start_path')>=0:
			data_1=line.split('=')
			start_path=data_1[1]
		if line.find('dimension')>=0:
			if line.find("2D")>=0:
				dimension="2D"
			if line.find("3D")>=0:
				dimension="3D"
		if line.find('router_type')>=0:
			if line.find('user_defined')>=0:
				router_type='user_defined'
			else:
				s = ''.join(x for x in line if x.isdigit())
				router_type=int(s)
		if line.find('R=')>=0:
			if line.find('0.9')>=0:
				R = 0.9
			if line.find('0.99')>=0:
				R = 0.99
			if line.find('0.999')>=0:
				R = 0.999
			if line.find('0.9999')>=0:
				R = 0.9999
			if line.find('0.99999')>=0:
				R = 0.99999
			if line.find('0.999999')>=0:
				R = 0.999999
			if line.find('0.9999999')>=0:
				R = 0.9999999
			if line.find('0.99999999')>=0:
				R = 0.99999999
			if line.find('0.999999999')>=0:
				R = 0.999999999
		if line.find('size')>=0:
			data_1=line.split(' ')
			if dimension == "2D":
				s = ''.join(x for x in data_1[0] if x.isdigit())
				row=int(s)
				s = ''.join(x for x in data_1[1] if x.isdigit())
				column=int(s)
			if dimension =="3D":
				s = ''.join(x for x in data_1[0] if x.isdigit())
				row=int(s)
				s = ''.join(x for x in data_1[1] if x.isdigit())
				column=int(s)
				s = ''.join(x for x in data_1[2] if x.isdigit())
				aisle=int(s)
		if line.find('topology')>=0:
			if line.find('mesh')>=0:
				topology_type="mesh"
			if line.find('torus')>=0:
				topology_type="torus"
		if line.find('traffic_type')>=0:
			if line.find('uniform')>=0:
				traffic_type="uniform"
			if line.find('hotspot')>=0:
				traffic_type="hotspot"
		if line.find('number_of_faults')>=0:
			s = ''.join(x for x in line if x.isdigit())
			number_of_faults=int(s)
		if line.find('threshold')>=0:
			s = ''.join(x for x in line if x.isdigit())
			threshold=int(s)
		line = myfile.readline()
network=[]
#########################################################################################
if topology_type=="mesh" and dimension =="2D":
	count=1
	for i in range(1,row+1):
		for j in range(1,column+1):
			#n1: north
			#n2: south
			#n3: west
			#n4: east
			n1=0
			n2=0
			n3=0
			n4=0
			if j>1:
				if count-1>=1 and count-1<=row*column:
					n3=count-1
			if j<column:
				if count+1>=1 and count+1<=row*column:
					n4=count+1
			if i>1:
				if count-column>=1 and count-column<=row*column:
					n1=count-column
			if i<row:
				if count+column>=1 and count+column<=row*column:
					n2=count+column
			network.append([count,i,j,n1,n2,n3,n4])
			count=count+1
	with open('output_topology.txt', 'w') as f:
		f.writelines("start_path:" + '\t' + str(start_path) + '\n')
		f.writelines("dimension:" + '\t' + str(dimension) + '\n')
		f.writelines("router_type:" + '\t' + str(router_type) + '\n')
		f.writelines("R:" + '\t' + str(R) + '\n')
		f.writelines("size(row,column):" + '\t' + str(row)+ '\t' + str(column)+ '\n')
		f.writelines("topology_type:" + '\t' + str(topology_type)+ '\n')
		f.writelines("traffic_type:" + '\t' + str(traffic_type) + '\n')
		f.writelines("number_of_faults:" + '\t' + str(number_of_faults) + '\n')
		f.writelines("threshold:" + '\t' + str(threshold) + '\n')
		f.writelines("network:" + '\n')
		f.writelines("router_num" + '\t' + "row(Y):" + '\t' + "column(X):" + '\t' + "north_nbr:" + '\t'+ "south_nbr:" + '\t'+ "west_nbr:" + '\t'+ "east_nbr:" + '\n')
		f.writelines('\t'.join(str(j) for j in i) + '\n' for i in network)
#########################################################################################
if topology_type=="torus" and dimension =="2D":
	count=1
	for i in range(1,row+1):
		for j in range(1,column+1):
			#n1: north
			#n2: south
			#n3: west
			#n4: east
			n1=0
			n2=0
			n3=0
			n4=0
			if j>1:
				if count-1>=1 and count-1<=row*column:
					n3=count-1
			if j<column:
				if count+1>=1 and count+1<=row*column:
					n4=count+1
			if i>1:
				if count-column>=1 and count-column<=row*column:
					n1=count-column
			if i<row:
				if count+column>=1 and count+column<=row*column:
					n2=count+column
			if j==1:
				n3=count+column-1
			if j==column:
				n4=count-column+1
			if i==1:
				n1=count+((row-1)*column)
			if i==row:
				n2=count-((row-1)*column)
			network.append([count,i,j,n1,n2,n3,n4])
			count=count+1
	with open('output_topology.txt', 'w') as f:
		f.writelines("start_path:" + '\t' + str(start_path) + '\n')
		f.writelines("dimension:" + '\t' + str(dimension) + '\n')
		f.writelines("router_type:" + '\t' + str(router_type) + '\n')
		f.writelines("R:" + '\t' + str(R) + '\n')
		f.writelines("size(row,column):" + '\t' + str(row)+ '\t' + str(column)+ '\n')
		f.writelines("topology_type:" + '\t' + str(topology_type)+ '\n')
		f.writelines("traffic_type:" + '\t' + str(traffic_type) + '\n')
		f.writelines("number_of_faults:" + '\t' + str(number_of_faults) + '\n')
		f.writelines("threshold:" + '\t' + str(threshold) + '\n')
		f.writelines("network:" + '\n')
		f.writelines("router_num" + '\t' + "row(Y):" + '\t' + "column(X):" + '\t' + "north_nbr:" + '\t'+ "south_nbr:" + '\t'+ "west_nbr:" + '\t'+ "east_nbr:" + '\n')
		f.writelines('\t'.join(str(j) for j in i) + '\n' for i in network)
#########################################################################################
if topology_type=="mesh" and dimension =="3D":
	count=1
	for k in range(1,aisle+1):
		count=1
		for i in range(1,row+1):
			for j in range(1,column+1):
				#n1: north
				#n2: south
				#n3: west
				#n4: east
				#n5: up
				#n6: down
				n1=0
				n2=0
				n3=0
				n4=0
				n5=0
				n6=0
				if j>1:
					if count-1>=1 and count-1<=aisle*row*column:
						n3=((k-1)*row*column)+count-1
				if j<column:
					if count+1>=1 and count+1<=aisle*row*column:
						n4=((k-1)*row*column)+count+1
				if i>1:
					if count-column>=1 and count-column<=aisle*row*column:
						n1=((k-1)*row*column)+count-column
				if i<row:
					if count+column>=1 and count+column<=aisle*row*column:
						n2=((k-1)*row*column)+count+column
				if k>1:
					if count+((k-1)*row*column)-column*row>=1 and count+((k-1)*row*column)-column*row<=row*column*aisle:
						n6=count+((k-1)*row*column)-column*row
				if k<aisle:
					if count+((k-1)*row*column)+column*row>=1 and count+((k-1)*row*column)+column*row<=row*column*aisle:
						n5=count+((k-1)*row*column)+column*row
				network.append([count+((k-1)*row*column),i,j,k,n1,n2,n3,n4,n5,n6])
				count=count+1
	with open('output_topology.txt', 'w') as f:
		f.writelines("start_path:" + '\t' + str(start_path) + '\n')
		f.writelines("dimension:" + '\t' + str(dimension) + '\n')
		f.writelines("router_type:" + '\t' + str(router_type) + '\n')
		f.writelines("R:" + '\t' + str(R) + '\n')
		f.writelines("size(row,column,aisle):" + '\t' + str(row)+ '\t' + str(column)+ '\t' + str(aisle)+ '\n')
		f.writelines("topology_type:" + '\t' + str(topology_type)+ '\n')
		f.writelines("traffic_type:" + '\t' + str(traffic_type) + '\n')
		f.writelines("number_of_faults:" + '\t' + str(number_of_faults) + '\n')
		f.writelines("threshold:" + '\t' + str(threshold) + '\n')
		f.writelines("network:" + '\n')
		f.writelines("router_num" + '\t' + "row(Y):" + '\t' + "column(X):" + '\t' + "aisle(Z):" + '\t' + "north_nbr:" + '\t'+ "south_nbr:" + '\t'+ "west_nbr:" + '\t'+ "east_nbr:" + '\t'+ "up_nbr:" + '\t'+"down_nbr:" + '\n')
		f.writelines('\t'.join(str(j) for j in i) + '\n' for i in network)
#########################################################################################
if topology_type=="torus" and dimension =="3D":
	count=1
	for k in range(1,aisle+1):
		count=1
		for i in range(1,row+1):
			for j in range(1,column+1):
				#n1: north
				#n2: south
				#n3: west
				#n4: east
				#n5: up
				#n6: down
				n1=0
				n2=0
				n3=0
				n4=0
				n5=0
				n6=0
				if j>1:
					if count-1>=1 and count-1<=aisle*row*column:
						n3=((k-1)*row*column)+count-1
				if j<column:
					if count+1>=1 and count+1<=aisle*row*column:
						n4=((k-1)*row*column)+count+1
				if i>1:
					if count-column>=1 and count-column<=aisle*row*column:
						n1=((k-1)*row*column)+count-column
				if i<row:
					if count+column>=1 and count+column<=aisle*row*column:
						n2=((k-1)*row*column)+count+column
				if k>1:
					if count+((k-1)*row*column)-column*row>=1 and count+((k-1)*row*column)-column*row<=row*column*aisle:
						n6=count+((k-1)*row*column)-column*row
				if k<aisle:
					if count+((k-1)*row*column)+column*row>=1 and count+((k-1)*row*column)+column*row<=row*column*aisle:
						n5=count+((k-1)*row*column)+column*row
				if j==1:
					n3=count+column-1
				if j==column:
					n4=count-column+1
				if i==1:
					n1=count+((row-1)*column)
				if i==row:
					n2=count-((row-1)*column)
				if k==1:
					n6=count+((k-1)*row*column)+((aisle-1)*row*column)
				if k==aisle:
					n5=count+((k-1)*row*column)-((aisle-1)*row*column)
				network.append([count+((k-1)*row*column),i,j,k,n1,n2,n3,n4,n5,n6])
				count=count+1
	with open('output_topology.txt', 'w') as f:
		f.writelines("start_path:" + '\t' + str(start_path) + '\n')
		f.writelines("dimension:" + '\t' + str(dimension) + '\n')
		f.writelines("router_type:" + '\t' + str(router_type) + '\n')
		f.writelines("R:" + '\t' + str(R) + '\n')
		f.writelines("size(row,column,aisle):" + '\t' + str(row)+ '\t' + str(column)+ '\t' + str(aisle)+ '\n')
		f.writelines("topology_type:" + '\t' + str(topology_type)+ '\n')
		f.writelines("traffic_type:" + '\t' + str(traffic_type) + '\n')
		f.writelines("number_of_faults:" + '\t' + str(number_of_faults) + '\n')
		f.writelines("threshold:" + '\t' + str(threshold) + '\n')
		f.writelines("network:" + '\n')
		f.writelines("router_num" + '\t' + "row(Y):" + '\t' + "column(X):" + '\t'+ "aisle(Z):" + '\t' + "north_nbr:" + '\t'+ "south_nbr:" + '\t'+ "west_nbr:" + '\t'+ "east_nbr:" + '\t'+ "up_nbr:" + '\t'+"down_nbr:" + '\n')
		f.writelines('\t'.join(str(j) for j in i) + '\n' for i in network)
#########################################################################################
with open("network.txt", "wb") as fp:
	pickle.dump(network, fp)
