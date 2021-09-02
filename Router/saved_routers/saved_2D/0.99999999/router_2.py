from collections import namedtuple
import multiprocessing as mp
import numpy
import itertools
import copy
import csv
import ast
import pickle
############################################################################################################################
#defining MRs

MicroRing = namedtuple("MicroRing", "number reliability type routs source dest neighber1 neighber2")

MRs = []
crossings=[]
bends=[]
Y_couplings=[]

with open("input_2.csv") as fp:
	line = fp.readline()
	end_of_tuple=0
	while line:
		if line!='\n' and end_of_tuple==0:
			l1=line.split('\t')
			l1_cp=copy.deepcopy(l1[7])
			l17=l1_cp.split()
			l1[7]="".join(l17)
			rec = MicroRing(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7])
			x=int(rec.number)
			rec=rec._replace(number=x)
			x=float(rec.reliability)
			rec=rec._replace(reliability=x)
			list_string=rec.routs
			l2=ast.literal_eval(list_string)
			rec=rec._replace(routs=l2)
			if rec.source=="None":
				rec=rec._replace(source=None)
			if rec.dest=="None":
				rec=rec._replace(dest=None)
			if rec.neighber1!="None":
				x=int(rec.neighber1)
				rec=rec._replace(neighber1=x)
			else:
				rec=rec._replace(neighber1=None)
			if rec.neighber2!="None":
				x=int(rec.neighber2)
				rec=rec._replace(neighber2=x)
			else:
				rec=rec._replace(neighber2=None)
			MRs.append(rec)
		else:
			end_of_tuple=1
			l1=line.split('\t')
			if l1[0]=="crossing":
				c_1=int(l1[1])
				c_2=int(l1[2])
				c_3=int(l1[3])
				c_4=int(l1[4])
				crossings.append([c_1,c_2,c_3,c_4])
			if l1[0]=="bend":
				b_1=int(l1[1])
				b_2=int(l1[2])
				b_3=int(l1[3])
				bends.append([b_1,b_2,b_3])
			if l1[0]=="Y_coupling":
				b_1=l1[1]
				Y_couplings.append(b_1)
		line = fp.readline()

##############################################################################################################################
########### data_loss
#1st = crossing
#2st = bend
#3st = Y_coupling
#4st = CPSE,on
#5st = CPSE,off
#6st = PPSE,on
#7st = PPSE,off
######################
data_loss=[]
roads=[]
road=[]
reliabilities=[]
##############################################################################################################################
#helping functions
def calc_dloss_reli(Road):
	reli=1
	app=1
	crossing_possible=0
	bend_possible=0
	y_coupling_possible=0
	ind1=[]
	ind2=-1
	ind3=[]
	ind4=-1
	dl_here=[0,0,0,0,0,0,0]
	for j in range(len(Road)):
		reli=reli*MRs[Road[j][0]-1].reliability
		if j==len(Road)-1:
			for k in range(len(Y_couplings)):
				if Y_couplings[k]==MRs[Road[j][0]-1].dest:
					dl_here[2]=dl_here[2]+1
		if MRs[Road[j][0]-1].type=="CPSE":
			if Road[j][1]=="on":
				dl_here[3]=dl_here[3]+1
			else:
				dl_here[4]=dl_here[4]+1
		else:
			if Road[j][1]=="on":
				dl_here[5]=dl_here[5]+1
			else:
				dl_here[6]=dl_here[6]+1
		for k in range(len(crossings)):
			if crossing_possible==0:
				if (Road[j][0]==crossings[k][1] and crossings[k][0]==0 and j==0) or (Road[j][0]==crossings[k][3] and crossings[k][2]==0 and j==0) or (Road[j][0]==crossings[k][0] and crossings[k][1]==0 and j==len(Road)-1) or (Road[j][0]==crossings[k][2] and crossings[k][3]==0 and j==len(Road)-1):
					dl_here[0]=dl_here[0]+1
					crossing_possible=0
				elif Road[j][0]==crossings[k][0]:
					crossing_possible=1
					ind1.append(k)
					ind2=j
				elif Road[j][0]==crossings[k][2]:
					crossing_possible=2
					ind1.append(k)
					ind2=j
			else:
				if j==ind2+1:	
					for n in range(len(ind1)):
						if Road[j][0]==crossings[k][1]:
							if crossing_possible==1 and k==ind1[n]:
								dl_here[0]=dl_here[0]+1
								crossing_possible=0
								ind2=-1
						elif Road[j][0]==crossings[k][3]:
							if crossing_possible==2 and k==ind1[n]:
								dl_here[0]=dl_here[0]+1
								crossing_possible=0
								ind2=-1
				elif j>ind2+1:
					crossing_possible=0
					ind1=[]
					ind2=-1
		for m in range(len(bends)):
			if bend_possible==0:
				if (Road[j][0]==bends[m][1] and bends[m][0]==0 and j==0) or (Road[j][0]==bends[m][0] and bends[m][1]==0 and j==len(Road)-1):
					dl_here[1]=dl_here[1]+1
					bend_possible=0
					ind4=-1
				elif Road[j][0]==bends[m][0]:
					bend_possible=1
					ind3.append(m)
					ind4=j
			else:
				if j==ind4+1:
					for q in range(len(ind3)):
						if Road[j][0]==bends[m][1]:
							if m==ind3[q]:
								dl_here[1]=dl_here[1]+bends[m][2]
								bend_possible=0
								ind4=-1
				elif j>ind4+1:
					bend_possible=0
					ind3=[]
					ind4=-1
	data_loss.append(dl_here)
	reliabilities.append(reli)

##############################################################################################################################
#recursive function
def road_finder( current_direction, current_MR ):
	pp=0
	op_direction=None
	if current_direction == "north":
		op_direction = "south"
	if current_direction == "south":
		op_direction = "north"
	if current_direction == "west":
		op_direction = "east"
	if current_direction == "east":
		op_direction = "west"
	if current_direction == "local":
		op_direction = "local"
	set1=[]
	set2=[]
	for k in range(len(MRs[current_MR].routs)):
		if k<len(MRs[current_MR].routs):
			i=MRs[current_MR].routs[k]
			if i[0]==op_direction:
				if len(MRs[current_MR].routs)<=2:
					if k==0:
						set1.append(i[1])
						set1.append(i[2])
					elif k==1:
						set2.append(i[1])
						set2.append(i[2])
				else:
					if k<2:
						set1.append(i[1])
						set1.append(i[2])
					else:
						set2.append(i[1])
						set2.append(i[2])
				if len(MRs[current_MR].routs)<=2:
					if k==0:
						if MRs[current_MR].neighber1 !=None:
							set1.append(MRs[current_MR].neighber1-1)
					elif k==1:
						if MRs[current_MR].neighber2 !=None:
							set2.append(MRs[current_MR].neighber2-1)
				else:
					if k<2:
						if MRs[current_MR].neighber1 !=None:
							set1.append(MRs[current_MR].neighber1-1)
					else:
						if MRs[current_MR].neighber2 !=None:
							set2.append(MRs[current_MR].neighber2-1)
	if len(set1)>3:
		t=[]
		t.append(set1.pop())
		t.append(set1.pop())
		t.append(set1.pop())
		set2.append(t.pop())
		set2.append(t.pop())
		set2.append(t.pop())
	if len(set1)>1 or len(set2)>1:
		app=0
		if len(set1)>1:
			if set1[1]!=None:
				ok=1
				for l in range(len(road)):
					if road[l][0]==current_MR+1:
						if road[l][1]=="on":
							if l==len(road)-1:
								road.pop()
							else:
								ok=0
						else:
							if set1[1]=="on":
								if l==len(road)-1:
									road.pop()
								else:
									ok=0
				if ok==1:
					road.append([current_MR+1, set1[1]])
					road_copy=road[:]
					if MRs[current_MR].dest !=None and len(set1)<3 and app==0:
						if (MRs[current_MR].dest=="north" and MRs[road[0][0]-1].source!="north") or (MRs[current_MR].dest=="south" and MRs[road[0][0]-1].source!="south") or (MRs[current_MR].dest=="east" and MRs[road[0][0]-1].source!="east") or (MRs[current_MR].dest=="west" and MRs[road[0][0]-1].source!="west") or (MRs[current_MR].dest=="local" and MRs[road[0][0]-1].source!="local"):
							roads.append(road_copy)
							calc_dloss_reli(road_copy)
					if len(set1)==3:
						road_finder(set1[0], set1[2])
				else:
					if len(road)>1:
						road.pop()
						pp=1
					if len(road)>0:
						return
		if len(set2)>1:
			if set2[1]!=None:
				ok=1
				for l in range(len(road)):
					if road[l][0]==current_MR+1:
						if road[l][1]=="on":
							if l==len(road)-1:
								road.pop()
							else:
								ok=0
						else:
							if set2[1]=="on":
								if l==len(road)-1:
									road.pop()
								else:
									ok=0
				if ok==1:
					road.append([current_MR+1, set2[1]])
					road_copy=road[:]
					if MRs[current_MR].dest !=None and len(set2)<3 and app==0:
						if (MRs[current_MR].dest=="north" and MRs[road[0][0]-1].source!="north") or (MRs[current_MR].dest=="south" and MRs[road[0][0]-1].source!="south") or (MRs[current_MR].dest=="east" and MRs[road[0][0]-1].source!="east") or (MRs[current_MR].dest=="west" and MRs[road[0][0]-1].source!="west") or (MRs[current_MR].dest=="local" and MRs[road[0][0]-1].source!="local"):
							roads.append(road_copy)
							calc_dloss_reli(road_copy)
					if len(set2)==3:
						road_finder(set2[0], set2[2])
				else:
					if len(road)>1:
						road.pop()
						pp=1
	elif MRs[current_MR].dest !=None:
		if len(road)>0:
			if (MRs[current_MR].dest=="north" and MRs[road[0][0]-1].source!="north") or (MRs[current_MR].dest=="south" and MRs[road[0][0]-1].source!="south") or (MRs[current_MR].dest=="east" and MRs[road[0][0]-1].source!="east") or (MRs[current_MR].dest=="west" and MRs[road[0][0]-1].source!="west") or (MRs[current_MR].dest=="local" and MRs[road[0][0]-1].source!="local"):
				roads.append(road)
				calc_dloss_reli(road)
			if len(road)>1 and pp==0:
				road.pop()
				pp=1
			return
	if len(road)>1 and pp==0:
		road.pop()

###############################################################################################################################
#main

for j in MRs:
	if j.source != None:
		op_direction = j.source
		current_direction = j.source
		if op_direction == "north":
			current_direction = "south"
		if op_direction == "south":
			current_direction = "north"
		if op_direction == "west":
			current_direction = "east"
		if op_direction == "east":
			current_direction = "west"
		if op_direction == "local":
			current_direction = "local"
		current_MR=j.number-1
		road[:]=[]
		road_finder( current_direction, current_MR )

#############################################################################################
#output
data_loss = [x for _,x in sorted(zip(reliabilities,data_loss))]
roads = [x for _,x in sorted(zip(reliabilities,roads))]
reliabilities.sort()
average_reliability=float(sum(reliabilities))/len(reliabilities)
np_dl=numpy.asarray(data_loss)
average_data_loss=np_dl.mean(axis=0)
with open('output2.csv', 'w') as f:
	f.writelines(' '.join(str(j) for j in i) + '\t' + ''.join(str(reliabilities[roads.index(i)])) + '\t' +''.join(str(data_loss[roads.index(i)])) + '\n' for i in roads)
with open("routes_2.txt", "wb") as fp:
	pickle.dump(roads, fp)
with open("reliabilities_2.txt", "wb") as fp:
	pickle.dump(reliabilities, fp)
with open("data_loss_2.txt", "wb") as fp:
	pickle.dump(data_loss, fp)

######################################################################################################################
#finding two simultaneous routes
a = range(len(roads))
b = range(len(roads))
ok=1
def two_sim(params):
	a=params[0]
	b=params[1]
	ok=1
	if roads[b]!= roads[a]:
		for k in range(len(roads[a])):
			for l in range(len(roads[b])):
				if k==0 and l==0:
					if roads[a][k][0]==roads[b][l][0]:
						ok=0
				if roads[a][k][1]=="on":
					if roads[a][k][0]==roads[b][l][0]:
						ok=0
				if roads[a][k][1]=="off":
					if roads[a][k][0]==roads[b][l][0] and roads[b][l][1]=="on":
						ok=0
				if ok==0:
					break
			if ok==0:
				break
		if ok==1:
			return [ [roads[a], roads[b]] ,reliabilities[a]*reliabilities[b], [data_loss[a], data_loss[b]] ]

paramlist = list(itertools.product(a,b))
pool = mp.Pool(mp.cpu_count())
result = pool.map(two_sim,paramlist)
res = list(filter(None, result)) 
two_simultaneous_routes=[i[0] for i in res]
rels1=[i[1] for i in res]
dls1=[i[2] for i in res]
two_simultaneous_routes = [x for _,x in sorted(zip(rels1,two_simultaneous_routes))]
dls1 = [x for _,x in sorted(zip(rels1,dls1))]
rels1.sort()

################################################################################################################################
#finding three simultaneous routes
a = range(len(two_simultaneous_routes))
b = range(len(roads))
ok=1
def three_sim(params):
	a=params[0]
	b=params[1]
	ok=1
	if roads[b]!= two_simultaneous_routes[a][0] and roads[b]!= two_simultaneous_routes[a][1]:
		for k in range(len(two_simultaneous_routes[a])):
			for m in range(len(two_simultaneous_routes[a][k])):
				for l in range(len(roads[b])):
					if m==0 and l==0:
						if two_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if two_simultaneous_routes[a][k][m][1]=="on":
						if two_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if two_simultaneous_routes[a][k][m][1]=="off":
						if two_simultaneous_routes[a][k][m][0]==roads[b][l][0] and roads[b][l][1]=="on":
							ok=0
					if ok==0:
						break
				if ok==0:
					break
			if ok==0:
				break
		if ok==1:
			return [[two_simultaneous_routes[a][0],two_simultaneous_routes[a][1],roads[b]],rels1[a]*reliabilities[b],[dls1[a][0],dls1[a][1],data_loss[b]]]
paramlist = list(itertools.product(a,b))
pool = mp.Pool(mp.cpu_count())
result = pool.map(three_sim,paramlist)
res = list(filter(None, result)) 
three_simultaneous_routes=[i[0] for i in res]
rels2=[i[1] for i in res]
dls2=[i[2] for i in res]
three_simultaneous_routes = [x for _,x in sorted(zip(rels2,three_simultaneous_routes))]
dls2 = [x for _,x in sorted(zip(rels2,dls2))]
rels2.sort()

##########################################################################################################################
#finding four simultaneous routes
a = range(len(three_simultaneous_routes))
b = range(len(roads))
ok=1
def four_sim(params):
	a=params[0]
	b=params[1]
	ok=1
	if roads[b]!=three_simultaneous_routes[a][0] and roads[b]!=three_simultaneous_routes[a][1] and roads[b]!=three_simultaneous_routes[a][2]:
		for k in range(len(three_simultaneous_routes[a])):
			for m in range(len(three_simultaneous_routes[a][k])):
				for l in range(len(roads[b])):
					if m==0 and l==0:
						if three_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if three_simultaneous_routes[a][k][m][1]=="on":
						if three_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if three_simultaneous_routes[a][k][m][1]=="off":
						if three_simultaneous_routes[a][k][m][0]==roads[b][l][0] and roads[b][l][1]=="on":
							ok=0
					if ok==0:
						break
				if ok==0:
					break
			if ok==0:
				break
		if ok==1:
			return [[three_simultaneous_routes[a][0],three_simultaneous_routes[a][1],three_simultaneous_routes[a][2], roads[b]],rels2[a]*reliabilities[b], [dls2[a][0],dls2[a][1],dls2[a][2],data_loss[b]]]
paramlist = list(itertools.product(a,b))
pool = mp.Pool(mp.cpu_count())
result = pool.map(four_sim,paramlist)
res = list(filter(None, result)) 
four_simultaneous_routes=[i[0] for i in res]
rels3=[i[1] for i in res]
dls3=[i[2] for i in res]
four_simultaneous_routes = [x for _,x in sorted(zip(rels3,four_simultaneous_routes))]
dls3 = [x for _,x in sorted(zip(rels3,dls3))]
rels3.sort()

##############################################################################################################################
#finding five simultaneous routes
a = range(len(four_simultaneous_routes))
b = range(len(roads))
ok=1
def five_sim(params):
	a=params[0]
	b=params[1]
	ok=1
	if roads[b]!=four_simultaneous_routes[a][0] and roads[b]!=four_simultaneous_routes[a][1] and roads[b]!=four_simultaneous_routes[a][2] and roads[b]!=four_simultaneous_routes[a][3]:
		for k in range(len(four_simultaneous_routes[a])):
			for m in range(len(four_simultaneous_routes[a][k])):
				for l in range(len(roads[b])):
					if m==0 and l==0:
						if four_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if four_simultaneous_routes[a][k][m][1]=="on":
						if four_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if four_simultaneous_routes[a][k][m][1]=="off":
						if four_simultaneous_routes[a][k][m][0]==roads[b][l][0] and roads[b][l][1]=="on":
							ok=0
					if ok==0:
						break
				if ok==0:
					break
			if ok==0:
				break
		if ok==1:
			return [[four_simultaneous_routes[a][0],four_simultaneous_routes[a][1],four_simultaneous_routes[a][2],four_simultaneous_routes[a][3], roads[b]],rels3[a]*reliabilities[b], [dls3[a][0],dls3[a][1],dls3[a][2],dls3[a][3],data_loss[b]]]
paramlist = list(itertools.product(a,b))
pool = mp.Pool(mp.cpu_count())
result = pool.map(five_sim,paramlist)
res = list(filter(None, result)) 
five_simultaneous_routes=[i[0] for i in res]
rels4=[i[1] for i in res]
dls4=[i[2] for i in res]
five_simultaneous_routes = [x for _,x in sorted(zip(rels4,five_simultaneous_routes))]
dls4 = [x for _,x in sorted(zip(rels4,dls4))]
rels4.sort()

############################################################################################################################
#finding six simultaneous routes
a = range(len(five_simultaneous_routes))
b = range(len(roads))
ok=1
def six_sim(params):
	a=params[0]
	b=params[1]
	ok=1
	if roads[b]!=five_simultaneous_routes[a][0] and roads[b]!=five_simultaneous_routes[a][1] and roads[b]!=five_simultaneous_routes[a][2] and roads[b]!=five_simultaneous_routes[a][3] and roads[b]!=five_simultaneous_routes[a][4]:
		for k in range(len(five_simultaneous_routes[a])):
			for m in range(len(five_simultaneous_routes[a][k])):
				for l in range(len(roads[b])):
					if m==0 and l==0:
						if five_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if five_simultaneous_routes[a][k][m][1]=="on":
						if five_simultaneous_routes[a][k][m][0]==roads[b][l][0]:
							ok=0
					if five_simultaneous_routes[a][k][m][1]=="off":
						if five_simultaneous_routes[a][k][m][0]==roads[b][l][0] and roads[b][l][1]=="on":
							ok=0
					if ok==0:
						break
				if ok==0:
					break
			if ok==0:
				break
		if ok==1:
			return [[five_simultaneous_routes[a][0],five_simultaneous_routes[a][1],five_simultaneous_routes[a][2],five_simultaneous_routes[a][3],five_simultaneous_routes[a][4], roads[b]],rels4[a]*reliabilities[b], [dls4[a][0],dls4[a][1],dls4[a][2],dls4[a][3],dls4[a][4],data_loss[b]]]
paramlist = list(itertools.product(a,b))
pool = mp.Pool(mp.cpu_count())
result = pool.map(six_sim,paramlist)
res = list(filter(None, result)) 
six_simultaneous_routes=[i[0] for i in res]
rels5=[i[1] for i in res]
dls5=[i[2] for i in res]
six_simultaneous_routes = [x for _,x in sorted(zip(rels5,six_simultaneous_routes))]
dls5 = [x for _,x in sorted(zip(rels5,dls5))]
rels5.sort()
###############################################################################################################
with open('ot2.txt', 'w') as f:
	f.writelines("worstcase_reliability:" + '\t' + str(reliabilities[0]) + '\n' + "average_reliability:" + '\t' + str(average_reliability) + '\n' + "worstcase [crossing , bend , Y_coupling , CPSE,on , CPSE,off , PPSE,on , PPSE,off]"  + '\t' + str(data_loss[0]) + '\n' + "average [crossing , bend , Y_coupling , CPSE,on , CPSE,off , PPSE,on , PPSE,off]" + '\t' + str(average_data_loss) + '\n')
	if len(rels1):
		f.writelines("two_sim_routes:" + '\t' + str(rels1[0]) + '\t' + str(dls1[0]) + '\n')
	if len(rels2):
		f.writelines("three_sim_routes:" + '\t' + str(rels2[0]) + '\t' + str(dls2[0]) + '\n')
	if len(rels3):
		f.writelines("four_sim_routes:" + '\t' + str(rels3[0]) + '\t' + str(dls3[0]) + '\n')
	if len(rels4):
		f.writelines("five_sim_routes:" + '\t' + str(rels4[0]) + '\t' + str(dls4[0]) + '\n')
	if len(rels5):
		f.writelines("six_sim_routes:" + '\t' + str(rels5[0]) + '\t' + str(dls5[0]) + '\n')
