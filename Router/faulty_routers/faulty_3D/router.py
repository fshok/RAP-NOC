from collections import namedtuple
import multiprocessing as mp
import numpy
import itertools
import copy
import csv
import ast
import pickle
import random
############################################################################################################################
#defining MRs

MicroRing = namedtuple("MicroRing", "number reliability type routs source dest neighber1 neighber2")

MRs = []
crossings=[]
bends=[]
Y_couplings=[]

with open("input.csv") as fp:
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
				b_1=b_1[0:len(b_1)-1]
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
	if current_direction == "injection":
		op_direction = "injection"
	if current_direction == "up":
		op_direction = "down"
	if current_direction == "down":
		op_direction = "up"
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
						if (MRs[current_MR].dest=="north" and MRs[road[0][0]-1].source!="north") or (MRs[current_MR].dest=="south" and MRs[road[0][0]-1].source!="south") or (MRs[current_MR].dest=="east" and MRs[road[0][0]-1].source!="east") or (MRs[current_MR].dest=="west" and MRs[road[0][0]-1].source!="west") or (MRs[current_MR].dest=="ejection" and MRs[road[0][0]-1].source!="injection") or (MRs[current_MR].dest=="up" and MRs[road[0][0]-1].source!="up") or (MRs[current_MR].dest=="down" and MRs[road[0][0]-1].source!="down"):
							roads.append(road_copy)
							calc_dloss_reli(road_copy)
					if len(set1)==3:
						road_finder(set1[0], set1[2])
					#else:
					#	if current_MR==2 and len(road)==1:
					#		road.pop()
					#		pp=1
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
						if (MRs[current_MR].dest=="north" and MRs[road[0][0]-1].source!="north") or (MRs[current_MR].dest=="south" and MRs[road[0][0]-1].source!="south") or (MRs[current_MR].dest=="east" and MRs[road[0][0]-1].source!="east") or (MRs[current_MR].dest=="west" and MRs[road[0][0]-1].source!="west") or (MRs[current_MR].dest=="ejection" and MRs[road[0][0]-1].source!="injection") or (MRs[current_MR].dest=="up" and MRs[road[0][0]-1].source!="up") or (MRs[current_MR].dest=="down" and MRs[road[0][0]-1].source!="down"):
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
			if (MRs[current_MR].dest=="north" and MRs[road[0][0]-1].source!="north") or (MRs[current_MR].dest=="south" and MRs[road[0][0]-1].source!="south") or (MRs[current_MR].dest=="east" and MRs[road[0][0]-1].source!="east") or (MRs[current_MR].dest=="west" and MRs[road[0][0]-1].source!="west") or (MRs[current_MR].dest=="ejection" and MRs[road[0][0]-1].source!="injection") or (MRs[current_MR].dest=="up" and MRs[road[0][0]-1].source!="up") or (MRs[current_MR].dest=="down" and MRs[road[0][0]-1].source!="down"):
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
		if op_direction == "injection":
			current_direction = "injection"
		if op_direction == "up":
			current_direction = "down"
		if op_direction == "down":
			current_direction = "up"
		current_MR=j.number-1
		road[:]=[]
		road_finder( current_direction, current_MR )

#############################################################################################
#fault_handling
number_of_faults = int(raw_input("Enter number of faults: "))
main_len=len(reliabilities)
if number_of_faults >0:
	faulty_MRs=random.sample(range(1, len(MRs)), number_of_faults)
	new_roads=[]
	new_reliabilities=[]
	new_data_loss=[]
	for i in range(len(roads)):
		ok=1
		for j in roads[i]:
			if j[0] in faulty_MRs:
				if j[1]=="on":
					ok=0
		if ok==1:
			new_roads.append(roads[i])
			new_reliabilities.append(reliabilities[i])
			new_data_loss.append(data_loss[i])
	roads = [x for x in new_roads]
	reliabilities = [x for x in new_reliabilities]
	data_loss = [x for x in new_data_loss]
#output
data_loss = [x for _,x in sorted(zip(reliabilities,data_loss))]
roads = [x for _,x in sorted(zip(reliabilities,roads))]
reliabilities.sort()
average_reliability=float(sum(reliabilities))/main_len
np_dl=numpy.asarray(data_loss)
average_data_loss=np_dl.mean(axis=0)
strl = "average_reliability:" + '\t' + str(average_reliability)
print(strl)
