import pickle
from collections import namedtuple
import random
import os
with open('output_topology.txt', 'r') as myfile: 
	data_1 = myfile.read()
data_2=data_1.split('\n')
for i in range(len(data_2)-1):
	data_3=data_2[i].split('\t')
	if data_3[0]=="start_path:":
		start_path=data_3[1]
	elif data_3[0]=="dimension:":
		dimension=data_3[1]
	elif data_3[0]=="router_type:":
		if (data_3[1]=="user_defined"):
			router_type = "user_defined"
		else:
			router_type=int(data_3[1])
	elif data_3[0]=="R:":
		R=data_3[1]
	elif data_3[0]=="size(row,column):":
		row=int(data_3[1])
		column=int(data_3[2])
	elif data_3[0]=="topology_type:":
		topology_type=data_3[1]
	elif data_3[0]=="traffic_type:":
		traffic_type=data_3[1]
	elif data_3[0]=="number_of_faults:":
		number_of_faults=int(data_3[1])
	elif data_3[0]=="threshold:":
		threshold=int(data_3[1])
with open("network.txt", "rb") as fp: 
	network = pickle.load(fp)
path = start_path+"/Router/saved_routers/saved_2D/"+str(R)+"/"
if dimension=="2D":
	if router_type=="user_defined":
		path = start_path+"/Router/user_defined_routers/user_defined_2D/"+str(R)+"/"
		strl1="cp "+path+"input_user_defined_2D.csv input_user_defined_2D.csv"
		strl2="python "+path+"router_user_defined_2D.py"
		os.system(strl1)
		os.system(strl2)
		with open("routes_user_defined_2D.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open("reliabilities_user_defined_2D.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open("data_loss_user_defined_2D.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_user_defined_2D.csv"
	if router_type==1:
		with open(path+"routes_1.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_1.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_1.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_1.csv"
	if router_type==2:
		with open(path+"routes_2.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_2.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_2.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_2.csv"
	if router_type==3:
		with open(path+"routes_3.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_3.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_3.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_3.csv"
	if router_type==4:
		with open(path+"routes_4.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_4.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_4.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_4.csv"
	if router_type==5:
		with open(path+"routes_5.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_5.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_5.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_5.csv"
	if router_type==6:
		with open(path+"routes_6.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_6.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_6.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_6.csv"
	if router_type==9:
		with open(path+"routes_9.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_9.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_9.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_9.csv"
MRs=[]
MicroRing = namedtuple("MicroRing", "number source dest")
with open(in_path) as fp:
	line = fp.readline()
	end_of_tuple=0
	while line:
		if line!='\n' and end_of_tuple==0:
			l1=line.split('\t')
			rec = MicroRing(l1[0],l1[4],l1[5])
			x=int(rec.number)
			rec=rec._replace(number=x)
			if rec.source=="None":
				rec=rec._replace(source=None)
			if rec.dest=="None":
				rec=rec._replace(dest=None)
			MRs.append(rec)
		else:
			end_of_tuple=1
		line = fp.readline()
if number_of_faults >0:
	#if number_of_faults>1:
	#	if (int(number_of_faults/(row*column))+1)<5:
	#		threshold = int(random.randrange(max(1,int(number_of_faults/(row*column))+1),min(5,number_of_faults)))
	#	else:
	#		threshold=5
	#else:
	#	threshold=1
	#print(threshold)
	if number_of_faults%threshold==0:
		faulty_routers_num=int(number_of_faults/threshold);
	else:
		faulty_routers_num=int(number_of_faults/threshold)+1;
	faulty_MRs_all=[random.randrange(len(MRs)) for i in range(number_of_faults)]
	faulty_routers_all=random.sample(range(1, column*row), faulty_routers_num)
	faulty_routers_row=[ int(y/column) for y in faulty_routers_all]
	faulty_routers_column=[ y%column for y in faulty_routers_all]
	faulty_MRs=[[] for y in range(faulty_routers_num)]
	for i in range(faulty_routers_num):
		if i == faulty_routers_num-1:
			faulty_MRs[i]=faulty_MRs_all[threshold*(i):]
		else:
			for j in range(threshold):
				faulty_MRs[i].append(faulty_MRs_all[threshold*i+j])
	#print(faulty_routers_row)
	#print(faulty_routers_column)
	#print(faulty_MRs)
if traffic_type=="uniform":
	with open('traffic_uniform.txt', 'r') as myfile:
		data_1 = myfile.read()
elif traffic_type=="hotspot":
	with open('traffic_hotspot.txt', 'r') as myfile:
		data_1 = myfile.read()
data_2=data_1.split('\n')
traffic_reliability=[]
traffic_data_loss=[[]]*(len(data_2)-1)
#########################################################################################
if dimension=="2D":
	routes_north_south=[]
	reliabilities_north_south=[]
	data_loss_north_south=[]
	routes_north_west=[]
	reliabilities_north_west=[]
	data_loss_north_west=[]
	routes_north_east=[]
	reliabilities_north_east=[]
	data_loss_north_east=[]
	routes_south_north=[]
	reliabilities_south_north=[]
	data_loss_south_north=[]
	routes_south_west=[]
	reliabilities_south_west=[]
	data_loss_south_west=[]
	routes_south_east=[]
	reliabilities_south_east=[]
	data_loss_south_east=[]
	routes_west_north=[]
	reliabilities_west_north=[]
	data_loss_west_north=[]
	routes_west_south=[]
	reliabilities_west_south=[]
	data_loss_west_south=[]
	routes_west_east=[]
	reliabilities_west_east=[]
	data_loss_west_east=[]
	routes_east_north=[]
	reliabilities_east_north=[]
	data_loss_east_north=[]
	routes_east_south=[]
	reliabilities_east_south=[]
	data_loss_east_south=[]
	routes_east_west=[]
	reliabilities_east_west=[]
	data_loss_east_west=[]
	for i in range(len(routes)):
		if MRs[routes[i][0][0]-1].source=="north":
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="south":
				routes_north_south.append(routes[i])
				reliabilities_north_south.append(reliabilities[i])
				data_loss_north_south.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="west":
				routes_north_west.append(routes[i])
				reliabilities_north_west.append(reliabilities[i])
				data_loss_north_west.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="east":
				routes_north_east.append(routes[i])
				reliabilities_north_east.append(reliabilities[i])
				data_loss_north_east.append(data_loss[i])
		if MRs[routes[i][0][0]-1].source=="south":
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="north":
				routes_south_north.append(routes[i])
				reliabilities_south_north.append(reliabilities[i])
				data_loss_south_north.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="west":
				routes_south_west.append(routes[i])
				reliabilities_south_west.append(reliabilities[i])
				data_loss_south_west.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="east":
				routes_south_east.append(routes[i])
				reliabilities_south_east.append(reliabilities[i])
				data_loss_south_east.append(data_loss[i])
		if MRs[routes[i][0][0]-1].source=="west":
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="north":
				routes_west_north.append(routes[i])
				reliabilities_west_north.append(reliabilities[i])
				data_loss_west_north.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="south":
				routes_west_south.append(routes[i])
				reliabilities_west_south.append(reliabilities[i])
				data_loss_west_south.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="east":
				routes_west_east.append(routes[i])
				reliabilities_west_east.append(reliabilities[i])
				data_loss_west_east.append(data_loss[i])
		if MRs[routes[i][0][0]-1].source=="east":
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="north":
				routes_east_north.append(routes[i])
				reliabilities_east_north.append(reliabilities[i])
				data_loss_east_north.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="south":
				routes_east_south.append(routes[i])
				reliabilities_east_south.append(reliabilities[i])
				data_loss_east_south.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="west":
				routes_east_west.append(routes[i])
				reliabilities_east_west.append(reliabilities[i])
				data_loss_east_west.append(data_loss[i])
	best_routes=[]
	best_routes.append(["north","south",routes_north_south[len(routes_north_south)-1],reliabilities_north_south[len(reliabilities_north_south)-1],data_loss_north_south[len(data_loss_north_south)-1]])
	best_routes.append(["north","west",routes_north_west[len(routes_north_west)-1],reliabilities_north_west[len(reliabilities_north_west)-1],data_loss_north_west[len(data_loss_north_west)-1]])
	best_routes.append(["north","east",routes_north_east[len(routes_north_east)-1],reliabilities_north_east[len(reliabilities_north_east)-1],data_loss_north_east[len(data_loss_north_east)-1]])
	best_routes.append(["south","north",routes_south_north[len(routes_south_north)-1],reliabilities_south_north[len(reliabilities_south_north)-1],data_loss_south_north[len(data_loss_south_north)-1]])
	best_routes.append(["south","west",routes_south_west[len(routes_south_west)-1],reliabilities_south_west[len(reliabilities_south_west)-1],data_loss_south_west[len(data_loss_south_west)-1]])
	best_routes.append(["south","east",routes_south_east[len(routes_south_east)-1],reliabilities_south_east[len(reliabilities_south_east)-1],data_loss_south_east[len(data_loss_south_east)-1]])

	best_routes.append(["west","north",routes_west_north[len(routes_west_north)-1],reliabilities_west_north[len(reliabilities_west_north)-1],data_loss_west_north[len(data_loss_west_north)-1]])
	best_routes.append(["west","south",routes_west_south[len(routes_west_south)-1],reliabilities_west_south[len(reliabilities_west_south)-1],data_loss_west_south[len(data_loss_west_south)-1]])
	best_routes.append(["west","east",routes_west_east[len(routes_west_east)-1],reliabilities_west_east[len(reliabilities_west_east)-1],data_loss_west_east[len(data_loss_west_east)-1]])
	best_routes.append(["east","north",routes_east_north[len(routes_east_north)-1],reliabilities_east_north[len(reliabilities_east_north)-1],data_loss_east_north[len(data_loss_east_north)-1]])
	best_routes.append(["east","south",routes_east_south[len(routes_east_south)-1],reliabilities_east_south[len(reliabilities_east_south)-1],data_loss_east_south[len(data_loss_east_south)-1]])
	best_routes.append(["east","west",routes_east_west[len(routes_east_west)-1],reliabilities_east_west[len(reliabilities_east_west)-1],data_loss_east_west[len(data_loss_east_west)-1]])
########################################################################################################################
	if number_of_faults > 0:
		faulty_routes=[[] for y in range(faulty_routers_num)]
		for k in range(faulty_routers_num):
			flag=0
			for i in range(len(routes_north_south)-1,0,-1):
				ok=1
				for j in routes_north_south[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["north","south",routes_north_south[i],reliabilities_north_south[i],data_loss_north_south[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["north","south",[],0,[]])
			flag=0
			for i in range(len(routes_north_west)-1,0,-1):
				ok=1
				for j in routes_north_west[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["north","west",routes_north_west[i],reliabilities_north_west[i],data_loss_north_west[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["north","west",[],0,[]])
			flag=0
			for i in range(len(routes_north_east)-1,0,-1):
				ok=1
				for j in routes_north_east[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["north","east",routes_north_east[i],reliabilities_north_east[i],data_loss_north_east[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["north","east",[],0,[]])
			flag=0
			for i in range(len(routes_south_north)-1,0,-1):
				ok=1
				for j in routes_south_north[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["south","north",routes_south_north[i],reliabilities_south_north[i],data_loss_south_north[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["south","north",[],0,[]])
			flag=0
			for i in range(len(routes_south_west)-1,0,-1):
				ok=1
				for j in routes_south_west[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["south","west",routes_south_west[i],reliabilities_south_west[i],data_loss_south_west[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["south","west",[],0,[]])
			flag=0
			for i in range(len(routes_south_east)-1,0,-1):
				ok=1
				for j in routes_south_east[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["south","east",routes_south_east[i],reliabilities_south_east[i],data_loss_south_east[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["south","east",[],0,[]])
			flag=0
			for i in range(len(routes_west_north)-1,0,-1):
				ok=1
				for j in routes_west_north[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["west","north",routes_west_north[i],reliabilities_west_north[i],data_loss_west_north[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["west","north",[],0,[]])
			flag=0
			for i in range(len(routes_west_south)-1,0,-1):
				ok=1
				for j in routes_west_south[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["west","south",routes_west_south[i],reliabilities_west_south[i],data_loss_west_south[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["west","south",[],0,[]])
			flag=0
			for i in range(len(routes_west_east)-1,0,-1):
				ok=1
				for j in routes_west_east[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["west","east",routes_west_east[i],reliabilities_west_east[i],data_loss_west_east[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["west","east",[],0,[]])
			flag=0
			for i in range(len(routes_east_north)-1,0,-1):
				ok=1
				for j in routes_east_north[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["east","north",routes_east_north[i],reliabilities_east_north[i],data_loss_east_north[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["east","north",[],0,[]])
			flag=0
			for i in range(len(routes_east_south)-1,0,-1):
				ok=1
				for j in routes_east_south[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["east","south",routes_east_south[i],reliabilities_east_south[i],data_loss_east_south[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["east","south",[],0,[]])
			flag=0
			for i in range(len(routes_east_west)-1,0,-1):
				ok=1
				for j in routes_east_west[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["east","west",routes_east_west[i],reliabilities_east_west[i],data_loss_east_west[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["east","west",[],0,[]])
########################################################################################################################		
	if topology_type=="mesh":
		for i in range(len(data_2)-1):
			data_3=data_2[i].split('\t')
			source_row=int(data_3[0])
			source_column=int(data_3[1])
			dest_row=int(data_3[2])
			dest_column=int(data_3[3])
			r=1
			dl_here=[]
			if dest_column > source_column and dest_row > source_row:
				for j in range(dest_column-source_column-1):
					r=r*best_routes[8][3]
					dl_here.append(best_routes[8][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[8][3]
							r=r*faulty_routes[k][8][3]
							dl_here.append(faulty_routes[k][8][4])
				r=r*best_routes[7][3]
				dl_here.append(best_routes[7][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[7][3]
							r=r*faulty_routes[k][7][3]
							dl_here.append(faulty_routes[k][7][4])
				for j in range(dest_row-source_row-1):
					r=r*best_routes[0][3]
					dl_here.append(best_routes[0][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[0][3]
							r=r*faulty_routes[k][0][3]
							dl_here.append(faulty_routes[k][0][4])
			if dest_column > source_column and dest_row < source_row:
				for j in range(dest_column-source_column-1):
					r=r*best_routes[8][3]
					dl_here.append(best_routes[8][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[8][3]
							r=r*faulty_routes[k][8][3]
							dl_here.append(faulty_routes[k][8][4])
				r=r*best_routes[6][3]
				dl_here.append(best_routes[6][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[6][3]
							r=r*faulty_routes[k][6][3]
							dl_here.append(faulty_routes[k][6][4])
				for j in range(source_row-dest_row-1):
					r=r*best_routes[3][3]
					dl_here.append(best_routes[3][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[3][3]
							r=r*faulty_routes[k][3][3]
							dl_here.append(faulty_routes[k][3][4])
			if dest_column < source_column and dest_row > source_row:
				for j in range(source_column-dest_column-1):
					r=r*best_routes[11][3]
					dl_here.append(best_routes[11][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >= dest_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[11][3]
							r=r*faulty_routes[k][11][3]
							dl_here.append(faulty_routes[k][11][4])
				r=r*best_routes[10][3]
				dl_here.append(best_routes[10][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[10][3]
							r=r*faulty_routes[k][10][3]
							dl_here.append(faulty_routes[k][10][4])
				for j in range(dest_row-source_row-1):
					r=r*best_routes[0][3]
					dl_here.append(best_routes[0][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[0][3]
							r=r*faulty_routes[k][0][3]
							dl_here.append(faulty_routes[k][0][4])
			if dest_column < source_column and dest_row < source_row:
				for j in range(source_column-dest_column-1):
					r=r*best_routes[11][3]
					dl_here.append(best_routes[11][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >= dest_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[11][3]
							r=r*faulty_routes[k][11][3]
							dl_here.append(faulty_routes[k][11][4])
				r=r*best_routes[9][3]
				dl_here.append(best_routes[9][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[9][3]
							r=r*faulty_routes[k][9][3]
							dl_here.append(faulty_routes[k][9][4])
				for j in range(source_row-dest_row-1):
					r=r*best_routes[3][3]
					dl_here.append(best_routes[3][4])
				if number_of_faults >0:
					for k in range(faulty_routers_num):
						if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
							if len(dl_here)>0:
								dl_here.pop()
							r=r/best_routes[3][3]
							r=r*faulty_routes[k][3][3]
							dl_here.append(faulty_routes[k][3][4])
			if dest_column == source_column:
				if dest_row < source_row:
					for j in range(source_row-dest_row-1):
						r=r*best_routes[3][3]
						dl_here.append(best_routes[3][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[3][3]
								r=r*faulty_routes[k][3][3]
								dl_here.append(faulty_routes[k][3][4])
				if dest_row > source_row:
					for j in range(dest_row-source_row-1):
						r=r*best_routes[0][3]
						dl_here.append(best_routes[0][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[0][3]
								r=r*faulty_routes[k][0][3]
								dl_here.append(faulty_routes[k][0][4])
			if dest_row == source_row:
				if dest_column < source_column:
					for j in range(source_column-dest_column-1):
						r=r*best_routes[11][3]
						dl_here.append(best_routes[11][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >= dest_column):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[11][3]
								r=r*faulty_routes[k][11][3]
								dl_here.append(faulty_routes[k][11][4])
				if dest_column > source_column:
					for j in range(dest_column-source_column-1):
						r=r*best_routes[8][3]
						dl_here.append(best_routes[8][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[8][3]
								r=r*faulty_routes[k][8][3]
								dl_here.append(faulty_routes[k][8][4])
			traffic_reliability.append(r)
			traffic_data_loss[i]=dl_here
#########################################################################################################################################
	elif topology_type=="torus":
		for i in range(len(data_2)-1):
			data_3=data_2[i].split('\t')
			source_row=int(data_3[0])
			source_column=int(data_3[1])
			dest_row=int(data_3[2])
			dest_column=int(data_3[3])
			r=1
			dl_here=[]
			if dest_column>source_column and dest_row > source_row:
				if abs(dest_column-source_column) < (abs(source_column + column-dest_column)):
					if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
						for j in range(dest_column-source_column-1):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[7][3]
						dl_here.append(best_routes[7][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[7][3]
									r=r*faulty_routes[k][7][3]
									dl_here.append(faulty_routes[k][7][4])
						for j in range(dest_row-source_row-1):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					elif abs(dest_row-source_row) > (abs(source_row + row-dest_row)):
						for j in range(dest_column-source_column-1):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[6][3]
						dl_here.append(best_routes[6][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[6][3]
									r=r*faulty_routes[k][6][3]
									dl_here.append(faulty_routes[k][6][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					else:
						for j in range(dest_column-source_column-1):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(dest_row-source_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				elif abs(dest_column-source_column) > (abs(source_column + column-dest_column)):
					if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[10][3]
						dl_here.append(best_routes[10][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[10][3]
									r=r*faulty_routes[k][10][3]
									dl_here.append(faulty_routes[k][10][4])
						for j in range(dest_row-source_row-1):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					elif abs(dest_row-source_row) > abs(source_row + row-dest_row):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[9][3]
						dl_here.append(best_routes[9][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[9][3]
									r=r*faulty_routes[k][9][3]
									dl_here.append(faulty_routes[k][9][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					else:
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(dest_row-source_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				else:
					r_temp_1=1
					r_temp_2=1
					for j in range(dest_column-source_column-1):
						r_temp_1=r_temp_1*best_routes[8][3]
					for j in range(abs(source_column + column-dest_column)):
						r_temp_2=r_temp_2*best_routes[11][3]
					if r_temp_2 >= r_temp_1:
						r=r*r_temp_2
						dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						if abs(dest_row-source_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							for j in range(abs(source_row + row-dest_row)):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							for j in range(dest_row-source_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(dest_row-source_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[9][3]
								dl_here.append(best_routes[9][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[9][3]
											r=r*faulty_routes[k][9][3]
											dl_here.append(faulty_routes[k][9][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[10][3]
								dl_here.append(best_routes[10][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[10][3]
											r=r*faulty_routes[k][10][3]
											dl_here.append(faulty_routes[k][10][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
					else:
						r=r*r_temp_1
						dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						if abs(dest_row-source_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							for j in range(abs(source_row) + row-dest_row):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							for j in range(dest_row-source_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(dest_row-source_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[6][3]
								dl_here.append(best_routes[6][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[6][3]
											r=r*faulty_routes[k][6][3]
											dl_here.append(faulty_routes[k][6][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[7][3]
								dl_here.append(best_routes[7][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[7][3]
											r=r*faulty_routes[k][7][3]
											dl_here.append(faulty_routes[k][7][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
#######################################################################################################################
			if dest_column > source_column and dest_row < source_row:
				if abs(dest_column-source_column) < (abs(source_column + column-dest_column)):
					if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
						for j in range(dest_column-source_column-1):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[6][3]
						dl_here.append(best_routes[6][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[6][3]
									r=r*faulty_routes[k][6][3]
									dl_here.append(faulty_routes[k][6][4])
						for j in range(source_row-dest_row-1):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					elif abs(source_row-dest_row) > (abs(source_row + row-dest_row)):
						for j in range(dest_column-source_column-1):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[7][3]
						dl_here.append(best_routes[7][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[7][3]
									r=r*faulty_routes[k][7][3]
									dl_here.append(faulty_routes[k][7][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					else:
						for j in range(dest_column-source_column-1):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(source_row-dest_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				elif abs(dest_column-source_column) > (abs(source_column + column-dest_column)):
					if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[9][3]
						dl_here.append(best_routes[9][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[9][3]
									r=r*faulty_routes[k][9][3]
									dl_here.append(faulty_routes[k][9][4])
						for j in range(source_row-dest_row-1):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					elif abs(source_row-dest_row) > abs(source_row + row-dest_row):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[10][3]
						dl_here.append(best_routes[10][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[10][3]
									r=r*faulty_routes[k][10][3]
									dl_here.append(faulty_routes[k][10][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					else:
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(source_row-dest_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				else:
					r_temp_1=1
					r_temp_2=1
					for j in range(dest_column-source_column-1):
						r_temp_1=r_temp_1*best_routes[8][3]
					for j in range(abs(source_row + row-dest_row)):
						r_temp_2=r_temp_2*best_routes[11][3]
					if r_temp_2 >= r_temp_1:
						r=r*r_temp_2
						dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						if abs(source_row-dest_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							for j in range(abs(source_row + row-dest_row)):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							for j in range(source_row-dest_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(source_row-dest_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[9][3]
								dl_here.append(best_routes[9][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[9][3]
											r=r*faulty_routes[k][9][3]
											dl_here.append(faulty_routes[k][9][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[10][3]
								dl_here.append(best_routes[10][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[10][3]
											r=r*faulty_routes[k][10][3]
											dl_here.append(faulty_routes[k][10][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
					else:
						r=r*r_temp_1
						dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						if abs(source_row-dest_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							for j in range(abs(source_row + row-dest_row)):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							for j in range(source_row-dest_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(source_row-dest_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[6][3]
								dl_here.append(best_routes[6][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[6][3]
											r=r*faulty_routes[k][6][3]
											dl_here.append(faulty_routes[k][6][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[7][3]
								dl_here.append(best_routes[7][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[7][3]
											r=r*faulty_routes[k][7][3]
											dl_here.append(faulty_routes[k][7][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
############################################################################################################################
			if dest_column<source_column and dest_row > source_row:
				if abs(source_column-dest_column) < (abs(source_column + column-dest_column)):
					if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
						for j in range(source_column-dest_column-1):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[10][3]
						dl_here.append(best_routes[10][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[10][3]
									r=r*faulty_routes[k][10][3]
									dl_here.append(faulty_routes[k][10][4])
						for j in range(dest_row-source_row-1):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					elif abs(dest_row-source_row) > (abs(source_row + row-dest_row)):
						for j in range(source_column-dest_column-1):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[9][3]
						dl_here.append(best_routes[9][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[9][3]
									r=r*faulty_routes[k][9][3]
									dl_here.append(faulty_routes[k][9][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					else:
						for j in range(source_column-dest_column-1):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(dest_row-source_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				elif abs(source_column-dest_column) > (abs(source_column + column-dest_column)):
					if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[7][3]
						dl_here.append(best_routes[7][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[7][3]
									r=r*faulty_routes[k][7][3]
									dl_here.append(faulty_routes[k][7][4])
						for j in range(dest_row-source_row-1):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					elif abs(dest_row-source_row) > (source_row + row-dest_row):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[6][3]
						dl_here.append(best_routes[6][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[6][3]
									r=r*faulty_routes[k][6][3]
									dl_here.append(faulty_routes[k][6][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					else:
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(dest_row-source_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				else:
					r_temp_1=1
					r_temp_2=1
					for j in range(source_column-dest_column-1):
						r_temp_1=r_temp_1*best_routes[8][3]
					for j in range(abs(source_row + row-dest_row)):
						r_temp_2=r_temp_2*best_routes[11][3]
					if r_temp_2 >= r_temp_1:
						r=r*r_temp_2
						dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						if abs(dest_row-source_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							for j in range(abs(source_row + row-dest_row)):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							for j in range(dest_row-source_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(dest_row-source_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[9][3]
								dl_here.append(best_routes[9][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[9][3]
											r=r*faulty_routes[k][9][3]
											dl_here.append(faulty_routes[k][9][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[10][3]
								dl_here.append(best_routes[10][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[10][3]
											r=r*faulty_routes[k][10][3]
											dl_here.append(faulty_routes[k][10][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
					else:
						r=r*r_temp_1
						dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						if abs(dest_row-source_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							for j in range(abs(source_row + row-dest_row)):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							for j in range(dest_row-source_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(dest_row-source_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[6][3]
								dl_here.append(best_routes[6][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[6][3]
											r=r*faulty_routes[k][6][3]
											dl_here.append(faulty_routes[k][6][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[7][3]
								dl_here.append(best_routes[7][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[7][3]
											r=r*faulty_routes[k][7][3]
											dl_here.append(faulty_routes[k][7][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
#############################################################################################################################
			if dest_column<source_column and dest_row < source_row:
				if abs(source_column-dest_column) < (abs(source_column + column-dest_column)):
					if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
						for j in range(source_column-dest_column-1):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[9][3]
						dl_here.append(best_routes[9][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[9][3]
									r=r*faulty_routes[k][9][3]
									dl_here.append(faulty_routes[k][9][4])
						for j in range(source_row-dest_row-1):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					elif abs(source_row-dest_row) > (abs(source_row + row-dest_row)):
						for j in range(source_column-dest_column-1):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r=r*best_routes[10][3]
						dl_here.append(best_routes[10][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[10][3]
									r=r*faulty_routes[k][10][3]
									dl_here.append(faulty_routes[k][10][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					else:
						for j in range(source_column-dest_column-1):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(source_row-dest_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				elif abs(source_column-dest_column) > (abs(source_column + column-dest_column)):
					if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[6][3]
						dl_here.append(best_routes[6][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[6][3]
									r=r*faulty_routes[k][6][3]
									dl_here.append(faulty_routes[k][6][4])
						for j in range(source_row-dest_row-1):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					elif abs(source_row-dest_row) > (source_row + row-dest_row):
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r=r*best_routes[7][3]
						dl_here.append(best_routes[7][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[7][3]
									r=r*faulty_routes[k][7][3]
									dl_here.append(faulty_routes[k][7][4])
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					else:
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						r_temp_1=1
						r_temp_2=1
						for j in range(source_row-dest_row-1):
							r_temp_1=r_temp_1*best_routes[0][3]
						for j in range(abs(source_row + row-dest_row)):
							r_temp_2=r_temp_2*best_routes[3][3]
						if r_temp_2 >= r_temp_1:
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							r=r*r_temp_2
							dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						else:
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							r=r*r_temp_1
							dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
				else:
					r_temp_1=1
					r_temp_2=1
					for j in range(source_column-dest_column-1):
						r_temp_1=r_temp_1*best_routes[8][3]
					for j in range(abs(source_row + row-dest_row)):
						r_temp_2=r_temp_2*best_routes[11][3]
					if r_temp_2 >= r_temp_1:
						r=r*r_temp_2
						dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						if abs(source_row-dest_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[9][3]
							dl_here.append(best_routes[9][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[9][3]
										r=r*faulty_routes[k][9][3]
										dl_here.append(faulty_routes[k][9][4])
							for j in range(abs(source_row + row-dest_row)):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[10][3]
							dl_here.append(best_routes[10][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[10][3]
										r=r*faulty_routes[k][10][3]
										dl_here.append(faulty_routes[k][10][4])
							for j in range(source_row-dest_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(source_row-dest_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[9][3]
								dl_here.append(best_routes[9][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[9][3]
											r=r*faulty_routes[k][9][3]
											dl_here.append(faulty_routes[k][9][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[10][3]
								dl_here.append(best_routes[10][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[10][3]
											r=r*faulty_routes[k][10][3]
											dl_here.append(faulty_routes[k][10][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
					else:
						r=r*r_temp_1
						dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
						if abs(source_row-dest_row) > (abs(source_row + row-dest_row)):
							r=r*best_routes[6][3]
							dl_here.append(best_routes[6][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[6][3]
										r=r*faulty_routes[k][6][3]
										dl_here.append(faulty_routes[k][6][4])
							for j in range(abs(source_row + row-dest_row)):
								r=r*best_routes[3][3]
								dl_here.append(best_routes[3][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[3][3]
										r=r*faulty_routes[k][3][3]
										dl_here.append(faulty_routes[k][3][4])
						if abs(source_row-dest_row) < (abs(source_row + row-dest_row)):
							r=r*best_routes[7][3]
							dl_here.append(best_routes[7][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[7][3]
										r=r*faulty_routes[k][7][3]
										dl_here.append(faulty_routes[k][7][4])
							for j in range(source_row-dest_row-1):
								r=r*best_routes[0][3]
								dl_here.append(best_routes[0][4])
							if number_of_faults >0:
								for k in range(faulty_routers_num):
									if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
										if len(dl_here)>0:
											dl_here.pop()
										r=r/best_routes[0][3]
										r=r*faulty_routes[k][0][3]
										dl_here.append(faulty_routes[k][0][4])
						else:
							r_temp_1_1=1
							r_temp_1_2=1
							for j in range(source_row-dest_row-1):
								r_temp_1_1=r_temp_1_1*best_routes[0][3]
							for j in range(abs(source_row + row-dest_row)):
								r_temp_1_2=r_temp_1_2*best_routes[3][3]
							if r_temp_1_2 >= r_temp_1_1:
								r=r*best_routes[6][3]
								dl_here.append(best_routes[6][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[6][3]
											r=r*faulty_routes[k][6][3]
											dl_here.append(faulty_routes[k][6][4])
								r=r*r_temp_1_2
								dl_here.append(best_routes[3][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[3][3]
											r=r*faulty_routes[k][3][3]
											dl_here.append(faulty_routes[k][3][4])
							else:
								r=r*best_routes[7][3]
								dl_here.append(best_routes[7][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_row[k]==source_row and faulty_routers_column[k] == dest_column):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[7][3]
											r=r*faulty_routes[k][7][3]
											dl_here.append(faulty_routes[k][7][4])
								r=r*r_temp_1_1
								dl_here.append(best_routes[0][4])
								if number_of_faults >0:
									for k in range(faulty_routers_num):
										if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
											if len(dl_here)>0:
												dl_here.pop()
											r=r/best_routes[0][3]
											r=r*faulty_routes[k][0][3]
											dl_here.append(faulty_routes[k][0][4])
#############################################################################################################################
			if dest_column == source_column:
				if dest_row < source_row:
					if abs(source_row-dest_row) < (abs(dest_row + row-source_row)):
						for j in range(source_row-dest_row):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
					else:
						for j in range(abs(dest_row + row-source_row)):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
				if dest_row > source_row:
					if abs(dest_row-source_row) < (abs(source_row + row-dest_row)):
						for j in range(dest_row-source_row):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					else:
						for j in range(abs(source_row + row-dest_row)):
							r=r*best_routes[3][3]
							dl_here.append(best_routes[3][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[3][3]
									r=r*faulty_routes[k][3][3]
									dl_here.append(faulty_routes[k][3][4])
			if dest_row == source_row:
				if dest_column < source_column:
					if abs(source_column-dest_column) < (abs(dest_column + column-source_column)):
						for j in range(source_column-dest_column):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
					else:
						for j in range(abs(dest_column + column-source_column)):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
				if dest_column > source_column:
					if abs(dest_column-source_column) < (abs(source_column + column-dest_column)):
						for j in range(dest_column-source_column):
							r=r*best_routes[8][3]
							dl_here.append(best_routes[8][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[8][3]
									r=r*faulty_routes[k][8][3]
									dl_here.append(faulty_routes[k][8][4])
					else:
						for j in range(abs(source_column + column-dest_column)):
							r=r*best_routes[11][3]
							dl_here.append(best_routes[11][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[11][3]
									r=r*faulty_routes[k][11][3]
									dl_here.append(faulty_routes[k][11][4])
						
			traffic_reliability.append(r)
			traffic_data_loss[i]=dl_here
#########################################################################################
print(traffic_reliability)
print("average:")
print(sum(traffic_reliability)/len(traffic_reliability))
