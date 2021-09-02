import pickle
from collections import namedtuple
import random
import os
###############################################################

def fun1(dc,sc,dr,sr,da,sa):
	r_1=1;
	dl_here_1=[]
	for i in range(dc-sc-1):
		r_1=r_1*best_routes[12][3]
		dl_here_1.append(best_routes[12][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0 and sr>=0 and sa>=0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_1)>0:
						dl_here_1.pop()
					r_1=r_1/best_routes[12][3]
					r_1=r_1*faulty_routes[k][12][3]
					dl_here_1.append(faulty_routes[k][12][4])
		if(sc>=0 and sr>=0 and sa<0):
			if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
				if len(dl_here_1)>0:
					dl_here_1.pop()
				r_1=r_1/best_routes[12][3]
				r_1=r_1*faulty_routes[k][12][3]
				dl_here_1.append(faulty_routes[k][12][4])
		if(sc>=0 and sr<0 and sa>=0):
			if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
				if len(dl_here_1)>0:
					dl_here_1.pop()
				r_1=r_1/best_routes[12][3]
				r_1=r_1*faulty_routes[k][12][3]
				dl_here_1.append(faulty_routes[k][12][4])
		if(sc>=0 and sr<0 and sa<0):
			if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
				if len(dl_here_1)>0:
					dl_here_1.pop()
				r_1=r_1/best_routes[12][3]
				r_1=r_1*faulty_routes[k][12][3]
				dl_here_1.append(faulty_routes[k][12][4])
		if(sc<0 and sr>=0 and sa>=0):
			if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
				if len(dl_here_1)>0:
					dl_here_1.pop()
				r_1=r_1/best_routes[12][3]
				r_1=r_1*faulty_routes[k][12][3]
				dl_here_1.append(faulty_routes[k][12][4])
		if(sc<0 and sr>=0 and sa<0):
			if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
				if len(dl_here_1)>0:
					dl_here_1.pop()
				r_1=r_1/best_routes[12][3]
				r_1=r_1*faulty_routes[k][12][3]
				dl_here_1.append(faulty_routes[k][12][4])
		if(sc<0 and sr<0 and sa>=0):
			if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
				if len(dl_here_1)>0:
					dl_here_1.pop()
				r_1=r_1/best_routes[12][3]
				r_1=r_1*faulty_routes[k][12][3]
				dl_here_1.append(faulty_routes[k][12][4])
		if(sc<0 and sr<0 and sa<0):
			if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
				if len(dl_here_1)>0:
					dl_here_1.pop()
				r_1=r_1/best_routes[12][3]
				r_1=r_1*faulty_routes[k][12][3]
				dl_here_1.append(faulty_routes[k][12][4])
	r_1=r_1*best_routes[11][3]
	dl_here_1.append(best_routes[11][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc:
				if(sr>=0 and sa>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == sa):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[11][3]
						r_1=r_1*faulty_routes[k][11][3]
						dl_here_1.append(faulty_routes[k][11][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[11][3]
						r_1=r_1*faulty_routes[k][11][3]
						dl_here_1.append(faulty_routes[k][11][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == sa):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[11][3]
						r_1=r_1*faulty_routes[k][11][3]
						dl_here_1.append(faulty_routes[k][11][4])
				if(sr<0 and sa<0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[11][3]
						r_1=r_1*faulty_routes[k][11][3]
						dl_here_1.append(faulty_routes[k][11][4])
	for i in range(dr-sr-1):
		r_1=r_1*best_routes[0][3]
		dl_here_1.append(best_routes[0][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc):
				if(sr>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[0][3]
						r_1=r_1*faulty_routes[k][0][3]
						dl_here_1.append(faulty_routes[k][0][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[0][3]
						r_1=r_1*faulty_routes[k][0][3]
						dl_here_1.append(faulty_routes[k][0][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[0][3]
						r_1=r_1*faulty_routes[k][0][3]
						dl_here_1.append(faulty_routes[k][0][4])
				if(sr<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[0][3]
						r_1=r_1*faulty_routes[k][0][3]
						dl_here_1.append(faulty_routes[k][0][4])
	r_1=r_1*best_routes[3][3]
	dl_here_1.append(best_routes[3][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc and faulty_routers_row[k]==dr:
				if(sa>=0):
					if (faulty_routers_aisle[k] == sa):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[3][3]
						r_1=r_1*faulty_routes[k][3][3]
						dl_here_1.append(faulty_routes[k][3][4])
				if(sa<0):
					if (faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[3][3]
						r_1=r_1*faulty_routes[k][3][3]
						dl_here_1.append(faulty_routes[k][3][4])
	for i in range(da-sa-1):
		r_1=r_1*best_routes[29][3]
		dl_here_1.append(best_routes[29][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc and faulty_routers_row[k]==dr):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[29][3]
						r_1=r_1*faulty_routes[k][29][3]
						dl_here_1.append(faulty_routes[k][29][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_1=r_1/best_routes[29][3]
						r_1=r_1*faulty_routes[k][29][3]
						dl_here_1.append(faulty_routes[k][29][4])
	return [r_1, dl_here_1]
def fun2(dc,sc,dr,sr,da,sa):
	r_2=1;
	dl_here_2=[]
	for i in range(dc-sc-1):
		r_2=r_2*best_routes[12][3]
		dl_here_2.append(best_routes[12][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0 and sa>=0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_2)>0:
						dl_here_2.pop()
					r_2=r_2/best_routes[12][3]
					r_2=r_2*faulty_routes[k][12][3]
					dl_here_2.append(faulty_routes[k][12][4])
			if(sc>=0 and sa<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_2)>0:
						dl_here_2.pop()
					r_2=r_2/best_routes[12][3]
					r_2=r_2*faulty_routes[k][12][3]
					dl_here_2.append(faulty_routes[k][12][4])
			if(sc<0 and sa>=0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_2)>0:
						dl_here_2.pop()
					r_2=r_2/best_routes[12][3]
					r_2=r_2*faulty_routes[k][12][3]
					dl_here_2.append(faulty_routes[k][12][4])
			if(sc<0 and sa<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_2)>0:
						dl_here_2.pop()
					r_2=r_2/best_routes[12][3]
					r_2=r_2*faulty_routes[k][12][3]
					dl_here_2.append(faulty_routes[k][12][4])
	r_2=r_2*best_routes[10][3]
	dl_here_2.append(best_routes[10][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc:
				if(sa>=0):
					if (faulty_routers_row[k]==dr and faulty_routers_aisle[k] == sa):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[10][3]
						r_2=r_2*faulty_routes[k][10][3]
						dl_here_2.append(faulty_routes[k][10][4])
				if(sa<0):
					if (faulty_routers_row[k]==dr and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[10][3]
						r_2=r_2*faulty_routes[k][10][3]
						dl_here_2.append(faulty_routes[k][10][4])
	for i in range(dr-sr-1):
		r_2=r_2*best_routes[5][3]
		dl_here_2.append(best_routes[5][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc):
				if(sr>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[5][3]
						r_2=r_2*faulty_routes[k][5][3]
						dl_here_2.append(faulty_routes[k][5][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[5][3]
						r_2=r_2*faulty_routes[k][5][3]
						dl_here_2.append(faulty_routes[k][5][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[5][3]
						r_2=r_2*faulty_routes[k][5][3]
						dl_here_2.append(faulty_routes[k][5][4])
				if(sr<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[5][3]
						r_2=r_2*faulty_routes[k][5][3]
						dl_here_2.append(faulty_routes[k][5][4])
	r_2=r_2*best_routes[8][3]
	dl_here_2.append(best_routes[8][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc:
				if(sr>=0 and sa>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == sa):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[8][3]
						r_2=r_2*faulty_routes[k][8][3]
						dl_here_2.append(faulty_routes[k][8][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == sa):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[8][3]
						r_2=r_2*faulty_routes[k][8][3]
						dl_here_2.append(faulty_routes[k][8][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[8][3]
						r_2=r_2*faulty_routes[k][8][3]
						dl_here_2.append(faulty_routes[k][8][4])
				if(sr<0 and sa<0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[8][3]
						r_2=r_2*faulty_routes[k][8][3]
						dl_here_2.append(faulty_routes[k][8][4])
	for i in range(da-sa-1):
		r_2=r_2*best_routes[29][3]
		dl_here_2.append(best_routes[29][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc):
				if(sr>=0 and sa>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[29][3]
						r_2=r_2*faulty_routes[k][29][3]
						dl_here_2.append(faulty_routes[k][29][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[29][3]
						r_2=r_2*faulty_routes[k][29][3]
						dl_here_2.append(faulty_routes[k][29][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_row[k]==sr and (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa))):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[29][3]
						r_2=r_2*faulty_routes[k][29][3]
						dl_here_2.append(faulty_routes[k][29][4])
				if(sr<0 and sa<0):
					if (faulty_routers_row[k]==(sr+row) and (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa))):
						if len(dl_here_2)>0:
							dl_here_2.pop()
						r_2=r_2/best_routes[29][3]
						r_2=r_2*faulty_routes[k][29][3]
						dl_here_2.append(faulty_routes[k][29][4])
	return [r_2, dl_here_2]
def fun3(dc,sc,dr,sr,da,sa):
	r_3=1;
	dl_here_3=[]
	for i in range(dc-sc-1):
		r_3=r_3*best_routes[17][3]
		dl_here_3.append(best_routes[17][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0 and sr>=0 and sa>=0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
			if(sc>=0 and sr>=0 and sa<0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
			if(sc>=0 and sr<0 and sa>=0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
			if(sc>=0 and sr<0 and sa<0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
			if(sc<0 and sr>=0 and sa>=0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
			if(sc<0 and sr>=0 and sa<0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
			if(sc<0 and sr<0 and sa>=0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
			if(sc<0 and sr<0 and sa<0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_3)>0:
						dl_here_3.pop()
					r_3=r_3/best_routes[17][3]
					r_3=r_3*faulty_routes[k][17][3]
					dl_here_3.append(faulty_routes[k][17][4])
	r_3=r_3*best_routes[16][3]
	dl_here_3.append(best_routes[16][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column)):
				if(sr>=0 and sa>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == sa):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[16][3]
						r_3=r_3*faulty_routes[k][16][3]
						dl_here_3.append(faulty_routes[k][16][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[16][3]
						r_3=r_3*faulty_routes[k][16][3]
						dl_here_3.append(faulty_routes[k][16][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == sa):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[16][3]
						r_3=r_3*faulty_routes[k][16][3]
						dl_here_3.append(faulty_routes[k][16][4])
				if(sr<0 and sa<0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[16][3]
						r_3=r_3*faulty_routes[k][16][3]
						dl_here_3.append(faulty_routes[k][16][4])
	for i in range(dr-sr-1):
		r_3=r_3*best_routes[0][3]
		dl_here_3.append(best_routes[0][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column)):
				if(sr>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[0][3]
						r_3=r_3*faulty_routes[k][0][3]
						dl_here_3.append(faulty_routes[k][0][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[0][3]
						r_3=r_3*faulty_routes[k][0][3]
						dl_here_3.append(faulty_routes[k][0][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[0][3]
						r_3=r_3*faulty_routes[k][0][3]
						dl_here_3.append(faulty_routes[k][0][4])
				if(sr<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[0][3]
						r_3=r_3*faulty_routes[k][0][3]
						dl_here_3.append(faulty_routes[k][0][4])
	r_3=r_3*best_routes[3][3]
	dl_here_3.append(best_routes[3][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_row[k]==dr:
				if(sa>=0):
					if (faulty_routers_aisle[k] == sa):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[3][3]
						r_3=r_3*faulty_routes[k][3][3]
						dl_here_3.append(faulty_routes[k][3][4])
				if(sa<0):
					if (faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[3][3]
						r_3=r_3*faulty_routes[k][3][3]
						dl_here_3.append(faulty_routes[k][3][4])
	for i in range(da-sa-1):
		r_3=r_3*best_routes[29][3]
		dl_here_3.append(best_routes[29][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_row[k]==dr):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[29][3]
						r_3=r_3*faulty_routes[k][29][3]
						dl_here_3.append(faulty_routes[k][29][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_3)>0:
							dl_here_3.pop()
						r_3=r_3/best_routes[29][3]
						r_3=r_3*faulty_routes[k][29][3]
						dl_here_3.append(faulty_routes[k][29][4])
	return [r_3, dl_here_3]
def fun4(dc,sc,dr,sr,da,sa):
	r_4=1;
	dl_here_4=[]
	for i in range(dc-sc-1):
		r_4=r_4*best_routes[17][3]
		dl_here_4.append(best_routes[17][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0 and sa>=0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_4)>0:
						dl_here_4.pop()
					r_4=r_4/best_routes[17][3]
					r_4=r_4*faulty_routes[k][17][3]
					dl_here_4.append(faulty_routes[k][17][4])
			if(sc>=0 and sa<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_4)>0:
						dl_here_4.pop()
					r_4=r_4/best_routes[17][3]
					r_4=r_4*faulty_routes[k][17][3]
					dl_here_4.append(faulty_routes[k][17][4])
			if(sc<0 and sa>=0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_4)>0:
						dl_here_4.pop()
					r_4=r_4/best_routes[17][3]
					r_4=r_4*faulty_routes[k][17][3]
					dl_here_4.append(faulty_routes[k][17][4])
			if(sc<0 and sa<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_4)>0:
						dl_here_4.pop()
					r_4=r_4/best_routes[17][3]
					r_4=r_4*faulty_routes[k][17][3]
					dl_here_4.append(faulty_routes[k][17][4])
	r_4=r_4*best_routes[15][3]
	dl_here_4.append(best_routes[15][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) :
				if(sr>=0 and sa>=0):
					if (faulty_routers_row[k]==dr and faulty_routers_aisle[k] == sa):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[15][3]
						r_4=r_4*faulty_routes[k][15][3]
						dl_here_4.append(faulty_routes[k][15][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_row[k]==dr and faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[15][3]
						r_4=r_4*faulty_routes[k][15][3]
						dl_here_4.append(faulty_routes[k][15][4])
	for i in range(dr-sr-1):
		r_4=r_4*best_routes[5][3]
		dl_here_4.append(best_routes[5][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))):
				if(sr>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[5][3]
						r_4=r_4*faulty_routes[k][5][3]
						dl_here_4.append(faulty_routes[k][5][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[5][3]
						r_4=r_4*faulty_routes[k][5][3]
						dl_here_4.append(faulty_routes[k][5][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[5][3]
						r_4=r_4*faulty_routes[k][5][3]
						dl_here_4.append(faulty_routes[k][5][4])
				if(sr<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[5][3]
						r_4=r_4*faulty_routes[k][5][3]
						dl_here_4.append(faulty_routes[k][5][4])
	r_4=r_4*best_routes[8][3]
	dl_here_4.append(best_routes[8][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))):
				if(sa>=0):
					if (faulty_routers_aisle[k] == sa):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[8][3]
						r_4=r_4*faulty_routes[k][8][3]
						dl_here_4.append(faulty_routes[k][8][4])
				if(sa<0):
					if (faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[8][3]
						r_4=r_4*faulty_routes[k][8][3]
						dl_here_4.append(faulty_routes[k][8][4])
	for i in range(da-sa-1):
		r_4=r_4*best_routes[29][3]
		dl_here_4.append(best_routes[29][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[29][3]
						r_4=r_4*faulty_routes[k][29][3]
						dl_here_4.append(faulty_routes[k][29][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_4)>0:
							dl_here_4.pop()
						r_4=r_4/best_routes[29][3]
						r_4=r_4*faulty_routes[k][29][3]
						dl_here_4.append(faulty_routes[k][29][4])
	return [r_4, dl_here_4]
def fun5(dc,sc,dr,sr,da,sa):
	r_5=1;
	dl_here_5=[]
	for i in range(dc-sc-1):
		r_5=r_5*best_routes[12][3]
		dl_here_5.append(best_routes[12][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0 and sr>=0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_5)>0:
						dl_here_5.pop()
					r_5=r_5/best_routes[12][3]
					r_5=r_5*faulty_routes[k][12][3]
					dl_here_5.append(faulty_routes[k][12][4])
			if(sc>=0 and sr<0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_5)>0:
						dl_here_5.pop()
					r_5=r_5/best_routes[12][3]
					r_5=r_5*faulty_routes[k][12][3]
					dl_here_5.append(faulty_routes[k][12][4])
			if(sc<0 and sr>=0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_5)>0:
						dl_here_5.pop()
					r_5=r_5/best_routes[12][3]
					r_5=r_5*faulty_routes[k][12][3]
					dl_here_5.append(faulty_routes[k][12][4])
			if(sc<0 and sr<0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_5)>0:
						dl_here_5.pop()
					r_5=r_5/best_routes[12][3]
					r_5=r_5*faulty_routes[k][12][3]
					dl_here_5.append(faulty_routes[k][12][4])
	r_5=r_5*best_routes[11][3]
	dl_here_5.append(best_routes[11][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc:
				if(sr>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == da):
						if len(dl_here_5)>0:
							dl_here_5.pop()
						r_5=r_5/best_routes[11][3]
						r_5=r_5*faulty_routes[k][11][3]
						dl_here_5.append(faulty_routes[k][11][4])
				if(sr<0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == da):
						if len(dl_here_5)>0:
							dl_here_5.pop()
						r_5=r_5/best_routes[11][3]
						r_5=r_5*faulty_routes[k][11][3]
						dl_here_5.append(faulty_routes[k][11][4])
	for i in range(dr-sr-1):
		r_5=r_5*best_routes[0][3]
		dl_here_5.append(best_routes[0][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc):
				if(sr>=0):
					if (faulty_routers_aisle[k]==da and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_5)>0:
							dl_here_5.pop()
						r_5=r_5/best_routes[0][3]
						r_5=r_5*faulty_routes[k][0][3]
						dl_here_5.append(faulty_routes[k][0][4])
				if(sr<0):
					if (faulty_routers_aisle[k]==da and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_5)>0:
							dl_here_5.pop()
						r_5=r_5/best_routes[0][3]
						r_5=r_5*faulty_routes[k][0][3]
						dl_here_5.append(faulty_routes[k][0][4])
	r_5=r_5*best_routes[4][3]
	dl_here_5.append(best_routes[4][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc and faulty_routers_row[k]==dr:
				if (faulty_routers_aisle[k] == da):
					if len(dl_here_5)>0:
						dl_here_5.pop()
					r_5=r_5/best_routes[4][3]
					r_5=r_5*faulty_routes[k][4][3]
					dl_here_5.append(faulty_routes[k][4][4])
	for i in range(da-sa-1):
		r_5=r_5*best_routes[24][3]
		dl_here_5.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc and faulty_routers_row[k]==dr):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_5)>0:
							dl_here_5.pop()
						r_5=r_5/best_routes[24][3]
						r_5=r_5*faulty_routes[k][24][3]
						dl_here_5.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_5)>0:
							dl_here_5.pop()
						r_5=r_5/best_routes[24][3]
						r_5=r_5*faulty_routes[k][24][3]
						dl_here_5.append(faulty_routes[k][24][4])
	return [r_5, dl_here_5]
def fun6(dc,sc,dr,sr,da,sa):
	r_6=1;
	dl_here_6=[]
	for i in range(dc-sc-1):
		r_6=r_6*best_routes[12][3]
		dl_here_6.append(best_routes[12][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_6)>0:
						dl_here_6.pop()
					r_6=r_6/best_routes[12][3]
					r_6=r_6*faulty_routes[k][12][3]
					dl_here_6.append(faulty_routes[k][12][4])
			if(sc<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_6)>0:
						dl_here_6.pop()
					r_6=r_6/best_routes[12][3]
					r_6=r_6*faulty_routes[k][12][3]
					dl_here_6.append(faulty_routes[k][12][4])
	r_6=r_6*best_routes[10][3]
	dl_here_6.append(best_routes[10][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc:
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k] == da):
					if len(dl_here_6)>0:
						dl_here_6.pop()
					r_6=r_6/best_routes[10][3]
					r_6=r_6*faulty_routes[k][10][3]
					dl_here_6.append(faulty_routes[k][10][4])
	for i in range(dr-sr-1):
		r_6=r_6*best_routes[5][3]
		dl_here_6.append(best_routes[5][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc):
				if(sr>=0):
					if (faulty_routers_aisle[k]==da and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_6)>0:
							dl_here_6.pop()
						r_6=r_6/best_routes[5][3]
						r_6=r_6*faulty_routes[k][5][3]
						dl_here_6.append(faulty_routes[k][5][4])
				if(sr<0):
					if (faulty_routers_aisle[k]==da and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_6)>0:
							dl_here_6.pop()
						r_6=r_6/best_routes[5][3]
						r_6=r_6*faulty_routes[k][5][3]
						dl_here_6.append(faulty_routes[k][5][4])
	r_6=r_6*best_routes[9][3]
	dl_here_6.append(best_routes[9][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k] == dc) and ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))):
				if (faulty_routers_aisle[k] == da):
					if len(dl_here_6)>0:
						dl_here_6.pop()
					r_6=r_6/best_routes[9][3]
					r_6=r_6*faulty_routes[k][9][3]
					dl_here_6.append(faulty_routes[k][9][4])
	for i in range(da-sa-1):
		r_6=r_6*best_routes[24][3]
		dl_here_6.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc) and ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_6)>0:
							dl_here_6.pop()
						r_6=r_6/best_routes[24][3]
						r_6=r_6*faulty_routes[k][24][3]
						dl_here_6.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_6)>0:
							dl_here_6.pop()
						r_6=r_6/best_routes[24][3]
						r_6=r_6*faulty_routes[k][24][3]
						dl_here_6.append(faulty_routes[k][24][4])
	return [r_6, dl_here_6]
def fun7(dc,sc,dr,sr,da,sa):
	r_7=1;
	dl_here_7=[]
	for i in range(dc-sc-1):
		r_7=r_7*best_routes[17][3]
		dl_here_7.append(best_routes[17][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0 and sr>=0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_7)>0:
						dl_here_7.pop()
					r_7=r_7/best_routes[17][3]
					r_7=r_7*faulty_routes[k][17][3]
					dl_here_7.append(faulty_routes[k][17][4])
			if(sc>=0 and sr<0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_7)>0:
						dl_here_7.pop()
					r_7=r_7/best_routes[17][3]
					r_7=r_7*faulty_routes[k][17][3]
					dl_here_7.append(faulty_routes[k][17][4])
			if(sc<0 and sr>=0):
				if (faulty_routers_row[k]==sr and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_7)>0:
						dl_here_7.pop()
					r_7=r_7/best_routes[17][3]
					r_7=r_7*faulty_routes[k][17][3]
					dl_here_7.append(faulty_routes[k][17][4])
			if(sc<0 and sr<0):
				if (faulty_routers_row[k]==(row+sr) and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_7)>0:
						dl_here_7.pop()
					r_7=r_7/best_routes[17][3]
					r_7=r_7*faulty_routes[k][17][3]
					dl_here_7.append(faulty_routes[k][17][4])
	r_7=r_7*best_routes[16][3]
	dl_here_7.append(best_routes[16][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if  ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) :
				if(sr>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_aisle[k] == da):
						if len(dl_here_7)>0:
							dl_here_7.pop()
						r_7=r_7/best_routes[16][3]
						r_7=r_7*faulty_routes[k][16][3]
						dl_here_7.append(faulty_routes[k][16][4])
				if(sr<0):
					if (faulty_routers_row[k]==(sr+row) and faulty_routers_aisle[k] == da):
						if len(dl_here_7)>0:
							dl_here_7.pop()
						r_7=r_7/best_routes[16][3]
						r_7=r_7*faulty_routes[k][16][3]
						dl_here_7.append(faulty_routes[k][16][4])
	for i in range(dr-sr-1):
		r_7=r_7*best_routes[0][3]
		dl_here_7.append(best_routes[0][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))):
				if(sr>=0):
					if (faulty_routers_aisle[k]==da and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_7)>0:
							dl_here_7.pop()
						r_7=r_7/best_routes[0][3]
						r_7=r_7*faulty_routes[k][0][3]
						dl_here_7.append(faulty_routes[k][0][4])
				if(sr<0):
					if (faulty_routers_aisle[k]==da and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_7)>0:
							dl_here_7.pop()
						r_7=r_7/best_routes[0][3]
						r_7=r_7*faulty_routes[k][0][3]
						dl_here_7.append(faulty_routes[k][0][4])
	r_7=r_7*best_routes[4][3]
	dl_here_7.append(best_routes[4][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_row[k]==dr:
				if (faulty_routers_aisle[k] == da):
					if len(dl_here_7)>0:
						dl_here_7.pop()
					r_7=r_7/best_routes[4][3]
					r_7=r_7*faulty_routes[k][4][3]
					dl_here_7.append(faulty_routes[k][4][4])
	for i in range(da-sa-1):
		r_7=r_7*best_routes[24][3]
		dl_here_7.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if  ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_row[k]==dr:
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_7)>0:
							dl_here_7.pop()
						r_7=r_7/best_routes[24][3]
						r_7=r_7*faulty_routes[k][24][3]
						dl_here_7.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_7)>0:
							dl_here_7.pop()
						r_7=r_7/best_routes[24][3]
						r_7=r_7*faulty_routes[k][24][3]
						dl_here_7.append(faulty_routes[k][24][4])
	return [r_7, dl_here_7]
def fun8(dc,sc,dr,sr,da,sa):
	r_8=1;
	dl_here_8=[]
	for i in range(dc-sc-1):
		r_8=r_8*best_routes[17][3]
		dl_here_8.append(best_routes[17][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_8)>0:
						dl_here_8.pop()
					r_8=r_8/best_routes[17][3]
					r_8=r_8*faulty_routes[k][17][3]
					dl_here_8.append(faulty_routes[k][17][4])
			if(sc<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_8)>0:
						dl_here_8.pop()
					r_8=r_8/best_routes[17][3]
					r_8=r_8*faulty_routes[k][17][3]
					dl_here_8.append(faulty_routes[k][17][4])
	r_8=r_8*best_routes[15][3]
	dl_here_8.append(best_routes[15][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k] == da):
					if len(dl_here_8)>0:
						dl_here_8.pop()
					r_8=r_8/best_routes[15][3]
					r_8=r_8*faulty_routes[k][15][3]
					dl_here_8.append(faulty_routes[k][15][4])
	for i in range(dr-sr-1):
		r_8=r_8*best_routes[5][3]
		dl_here_8.append(best_routes[5][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))):
				if(sr>=0):
					if (faulty_routers_aisle[k]==da and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_8)>0:
							dl_here_8.pop()
						r_8=r_8/best_routes[5][3]
						r_8=r_8*faulty_routes[k][5][3]
						dl_here_8.append(faulty_routes[k][5][4])
				if(sr<0):
					if (faulty_routers_aisle[k]==da and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_8)>0:
							dl_here_8.pop()
						r_8=r_8/best_routes[5][3]
						r_8=r_8*faulty_routes[k][5][3]
						dl_here_8.append(faulty_routes[k][5][4])
	r_8=r_8*best_routes[9][3]
	dl_here_8.append(best_routes[9][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and ((sr>=0 and faulty_routers_row[k] == sr) or (sr<0 and faulty_routers_row[k] == (sr+row))):
				if(sa>=0):
					if (faulty_routers_aisle[k] == da):
						if len(dl_here_8)>0:
							dl_here_8.pop()
						r_8=r_8/best_routes[9][3]
						r_8=r_8*faulty_routes[k][9][3]
						dl_here_8.append(faulty_routes[k][9][4])
	for i in range(da-sa-1):
		r_8=r_8*best_routes[24][3]
		dl_here_8.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and ((sr>=0 and faulty_routers_row[k] == sr) or (sr<0 and faulty_routers_row[k] == (sr+row))):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_8)>0:
							dl_here_8.pop()
						r_8=r_8/best_routes[24][3]
						r_8=r_8*faulty_routes[k][24][3]
						dl_here_8.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_8)>0:
							dl_here_8.pop()
						r_8=r_8/best_routes[24][3]
						r_8=r_8*faulty_routes[k][24][3]
						dl_here_8.append(faulty_routes[k][24][4])
	return [r_8, dl_here_8]
##########################################################################################
def fun9(dc,sc,dr,sr,da):
	r_9=1;
	dl_here_9=[]
	for i in range(dc-sc-1):
		r_9=r_9*best_routes[12][3]
		dl_here_9.append(best_routes[12][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_aisle[k]==da:
				if(sc>=0 and sr>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[12][3]
						r_9=r_9*faulty_routes[k][12][3]
						dl_here_9.append(faulty_routes[k][12][4])
				if(sc>=0 and sr<0):
					if (faulty_routers_row[k]==(row+sr) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[12][3]
						r_9=r_9*faulty_routes[k][12][3]
						dl_here_9.append(faulty_routes[k][12][4])
				if(sc<0 and sr>=0):
					if (faulty_routers_row[k]==sr and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[12][3]
						r_9=r_9*faulty_routes[k][12][3]
						dl_here_9.append(faulty_routes[k][12][4])
				if(sc<0 and sr<0):
					if (faulty_routers_row[k]==(row+sr) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[12][3]
						r_9=r_9*faulty_routes[k][12][3]
						dl_here_9.append(faulty_routes[k][12][4])
	r_9=r_9*best_routes[11][3]
	dl_here_9.append(best_routes[11][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc and faulty_routers_aisle[k]==da:
				if(sr>=0):
					if (faulty_routers_row[k]==sr):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[11][3]
						r_9=r_9*faulty_routes[k][11][3]
						dl_here_9.append(faulty_routes[k][11][4])
				if(sr<0):
					if (faulty_routers_row[k]==(sr+row)):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[11][3]
						r_9=r_9*faulty_routes[k][11][3]
						dl_here_9.append(faulty_routes[k][11][4])
	for i in range(dr-sr-1):
		r_9=r_9*best_routes[0][3]
		dl_here_9.append(best_routes[0][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc) and faulty_routers_aisle[k]==da:
				if(sr>=0):
					if (faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[0][3]
						r_9=r_9*faulty_routes[k][0][3]
						dl_here_9.append(faulty_routes[k][0][4])
				if(sr<0):
					if (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr)):
						if len(dl_here_9)>0:
							dl_here_9.pop()
						r_9=r_9/best_routes[0][3]
						r_9=r_9*faulty_routes[k][0][3]
						dl_here_9.append(faulty_routes[k][0][4])
	return [r_9, dl_here_9]
def fun10(dc,sc,dr,sr,da):
	r_10=1;
	dl_here_10=[]
	for i in range(dc-sc-1):
		r_10=r_10*best_routes[12][3]
		dl_here_10.append(best_routes[12][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_aisle[k]==da:
				if(sc>=0):
					if (faulty_routers_row[k]==dr and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_10)>0:
							dl_here_10.pop()
						r_10=r_10/best_routes[12][3]
						r_10=r_10*faulty_routes[k][12][3]
						dl_here_10.append(faulty_routes[k][12][4])
				if(sc<0):
					if (faulty_routers_row[k]==dr and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_10)>0:
							dl_here_10.pop()
						r_10=r_10/best_routes[12][3]
						r_10=r_10*faulty_routes[k][12][3]
						dl_here_10.append(faulty_routes[k][12][4])
	r_10=r_10*best_routes[10][3]
	dl_here_10.append(best_routes[10][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if faulty_routers_column[k] == dc and faulty_routers_aisle[k]==da:
				if (faulty_routers_row[k]==dr):
					if len(dl_here_10)>0:
						dl_here_10.pop()
					r_10=r_10/best_routes[10][3]
					r_10=r_10*faulty_routes[k][10][3]
					dl_here_10.append(faulty_routes[k][10][4])
	for i in range(dr-sr-1):
		r_10=r_10*best_routes[5][3]
		dl_here_10.append(best_routes[5][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc) and faulty_routers_aisle[k]==da:
				if(sr>=0):
					if (faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_10)>0:
							dl_here_10.pop()
						r_10=r_10/best_routes[5][3]
						r_10=r_10*faulty_routes[k][5][3]
						dl_here_10.append(faulty_routes[k][5][4])
				if(sr<0):
					if (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr)):
						if len(dl_here_10)>0:
							dl_here_10.pop()
						r_10=r_10/best_routes[5][3]
						r_10=r_10*faulty_routes[k][5][3]
						dl_here_10.append(faulty_routes[k][5][4])
	return [r_10, dl_here_10]
def fun11(dc,sc,dr,sr,da):
	r_11=1;
	dl_here_11=[]
	for i in range(dc-sc-1):
		r_11=r_11*best_routes[17][3]
		dl_here_11.append(best_routes[17][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if faulty_routers_aisle[k]==da:
				if(sc>=0 and sr>=0):
					if (faulty_routers_row[k]==sr and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[17][3]
						r_11=r_11*faulty_routes[k][17][3]
						dl_here_11.append(faulty_routes[k][17][4])
				if(sc>=0 and sr<0):
					if (faulty_routers_row[k]==(row+sr) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[17][3]
						r_11=r_11*faulty_routes[k][17][3]
						dl_here_11.append(faulty_routes[k][17][4])
				if(sc<0 and sr>=0):
					if (faulty_routers_row[k]==sr and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[17][3]
						r_11=r_11*faulty_routes[k][17][3]
						dl_here_11.append(faulty_routes[k][17][4])
				if(sc<0 and sr<0):
					if (faulty_routers_row[k]==(row+sr) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[17][3]
						r_11=r_11*faulty_routes[k][17][3]
						dl_here_11.append(faulty_routes[k][17][4])
	r_11=r_11*best_routes[16][3]
	dl_here_11.append(best_routes[16][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_aisle[k]==da:
				if(sr>=0):
					if (faulty_routers_row[k]==sr):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[16][3]
						r_11=r_11*faulty_routes[k][16][3]
						dl_here_11.append(faulty_routes[k][16][4])
				if(sr<0):
					if (faulty_routers_row[k]==(sr+row)):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[16][3]
						r_11=r_11*faulty_routes[k][16][3]
						dl_here_11.append(faulty_routes[k][16][4])
	for i in range(dr-sr-1):
		r_11=r_11*best_routes[0][3]
		dl_here_11.append(best_routes[0][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_aisle[k]==da:
				if(sr>=0):
					if (faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[0][3]
						r_11=r_11*faulty_routes[k][0][3]
						dl_here_11.append(faulty_routes[k][0][4])
				if(sr<0):
					if (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr)):
						if len(dl_here_11)>0:
							dl_here_11.pop()
						r_11=r_11/best_routes[0][3]
						r_11=r_11*faulty_routes[k][0][3]
						dl_here_11.append(faulty_routes[k][0][4])
	return [r_11, dl_here_11]
def fun12(dc,sc,dr,sr,da):
	r_12=1;
	dl_here_12=[]
	for i in range(dc-sc-1):
		r_12=r_12*best_routes[17][3]
		dl_here_12.append(best_routes[17][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_aisle[k]==da:
				if(sc>=0):
					if (faulty_routers_row[k]==dr and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_12)>0:
							dl_here_12.pop()
						r_12=r_12/best_routes[17][3]
						r_12=r_12*faulty_routes[k][17][3]
						dl_here_12.append(faulty_routes[k][17][4])
				if(sc<0):
					if (faulty_routers_row[k]==dr and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_12)>0:
							dl_here_12.pop()
						r_12=r_12/best_routes[17][3]
						r_12=r_12*faulty_routes[k][17][3]
						dl_here_12.append(faulty_routes[k][17][4])
	r_12=r_12*best_routes[15][3]
	dl_here_12.append(best_routes[15][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_aisle[k]==da:
				if (faulty_routers_row[k]==dr):
					if len(dl_here_12)>0:
						dl_here_12.pop()
					r_12=r_12/best_routes[15][3]
					r_12=r_12*faulty_routes[k][15][3]
					dl_here_12.append(faulty_routes[k][15][4])
	for i in range(dr-sr-1):
		r_12=r_12*best_routes[5][3]
		dl_here_12.append(best_routes[5][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column))) and faulty_routers_aisle[k]==da:
				if(sr>=0):
					if (faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_12)>0:
							dl_here_12.pop()
						r_12=r_12/best_routes[5][3]
						r_12=r_12*faulty_routes[k][5][3]
						dl_here_12.append(faulty_routes[k][5][4])
				if(sr<0):
					if (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr)):
						if len(dl_here_12)>0:
							dl_here_12.pop()
						r_12=r_12/best_routes[5][3]
						r_12=r_12*faulty_routes[k][5][3]
						dl_here_12.append(faulty_routes[k][5][4])
	return [r_12, dl_here_12]
def fun13(dc,dr,sr,da,sa):
	r_13=1;
	dl_here_13=[]
	for i in range(dr-sr-1):
		r_13=r_13*best_routes[0][3]
		dl_here_13.append(best_routes[0][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k]==dc:
				if(sr>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[0][3]
						r_13=r_13*faulty_routes[k][0][3]
						dl_here_13.append(faulty_routes[k][0][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[0][3]
						r_13=r_13*faulty_routes[k][0][3]
						dl_here_13.append(faulty_routes[k][0][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[0][3]
						r_13=r_13*faulty_routes[k][0][3]
						dl_here_13.append(faulty_routes[k][0][4])
				if(sr<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[0][3]
						r_13=r_13*faulty_routes[k][0][3]
						dl_here_13.append(faulty_routes[k][0][4])
	r_13=r_13*best_routes[3][3]
	dl_here_13.append(best_routes[3][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_row[k]==dr and faulty_routers_column[k]==dc:
				if(sa>=0):
					if (faulty_routers_aisle[k] == sa):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[3][3]
						r_13=r_13*faulty_routes[k][3][3]
						dl_here_13.append(faulty_routes[k][3][4])
				if(sa<0):
					if (faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[3][3]
						r_13=r_13*faulty_routes[k][3][3]
						dl_here_13.append(faulty_routes[k][3][4])
	for i in range(da-sa-1):
		r_13=r_13*best_routes[29][3]
		dl_here_13.append(best_routes[29][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_row[k]==dr) and faulty_routers_column[k]==dc:
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[29][3]
						r_13=r_13*faulty_routes[k][29][3]
						dl_here_13.append(faulty_routes[k][29][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_13)>0:
							dl_here_13.pop()
						r_13=r_13/best_routes[29][3]
						r_13=r_13*faulty_routes[k][29][3]
						dl_here_13.append(faulty_routes[k][29][4])
	return [r_13, dl_here_13]
def fun14(dc,dr,sr,da,sa):
	r_14=1;
	dl_here_14=[]
	for i in range(dr-sr-1):
		r_14=r_14*best_routes[5][3]
		dl_here_14.append(best_routes[5][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k]==dc:
				if(sr>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[5][3]
						r_14=r_14*faulty_routes[k][5][3]
						dl_here_1.append(faulty_routes[k][5][4])
				if(sr>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[5][3]
						r_14=r_14*faulty_routes[k][5][3]
						dl_here_1.append(faulty_routes[k][5][4])
				if(sr<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[5][3]
						r_14=r_14*faulty_routes[k][5][3]
						dl_here_1.append(faulty_routes[k][5][4])
				if(sr<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[5][3]
						r_14=r_14*faulty_routes[k][5][3]
						dl_here_1.append(faulty_routes[k][5][4])
	r_14=r_14*best_routes[8][3]
	dl_here_14.append(best_routes[8][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))) and faulty_routers_column[k]==dc:
				if(sa>=0):
					if (faulty_routers_aisle[k] == sa):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[8][3]
						r_14=r_14*faulty_routes[k][8][3]
						dl_here_1.append(faulty_routes[k][8][4])
				if(sa<0):
					if (faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[8][3]
						r_14=r_14*faulty_routes[k][8][3]
						dl_here_1.append(faulty_routes[k][8][4])
	for i in range(da-sa-1):
		r_14=r_14*best_routes[29][3]
		dl_here_14.append(best_routes[29][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))) and faulty_routers_column[k]==dc:
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[29][3]
						r_14=r_14*faulty_routes[k][29][3]
						dl_here_1.append(faulty_routes[k][29][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_1)>0:
							dl_here_1.pop()
						r_14=r_14/best_routes[29][3]
						r_14=r_14*faulty_routes[k][29][3]
						dl_here_1.append(faulty_routes[k][29][4])
	return [r_14, dl_here_14]
def fun15(dc,dr,sr,da,sa):
	r_15=1;
	dl_here_15=[]
	for i in range(dr-sr-1):
		r_15=r_15*best_routes[0][3]
		dl_here_15.append(best_routes[0][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k]==dc:
				if(sr>=0):
					if (faulty_routers_aisle[k]==da and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_15)>0:
							dl_here_15.pop()
						r_15=r_15/best_routes[0][3]
						r_15=r_15*faulty_routes[k][0][3]
						dl_here_15.append(faulty_routes[k][0][4])
				if(sr<0):
					if (faulty_routers_aisle[k]==da and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_15)>0:
							dl_here_15.pop()
						r_15=r_15/best_routes[0][3]
						r_15=r_15*faulty_routes[k][0][3]
						dl_here_15.append(faulty_routes[k][0][4])
	r_15=r_15*best_routes[4][3]
	dl_here_15.append(best_routes[4][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_row[k]==dr and faulty_routers_column[k]==dc:
				if (faulty_routers_aisle[k] == da):
					if len(dl_here_15)>0:
						dl_here_15.pop()
					r_15=r_15/best_routes[4][3]
					r_15=r_15*faulty_routes[k][4][3]
					dl_here_15.append(faulty_routes[k][4][4])
	for i in range(da-sa-1):
		r_15=r_15*best_routes[24][3]
		dl_here_15.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_row[k]==dr) and faulty_routers_column[k]==dc:
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_15)>0:
							dl_here_15.pop()
						r_15=r_15/best_routes[24][3]
						r_15=r_15*faulty_routes[k][24][3]
						dl_here_15.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_15)>0:
							dl_here_15.pop()
						r_15=r_15/best_routes[24][3]
						r_15=r_15*faulty_routes[k][24][3]
						dl_here_15.append(faulty_routes[k][24][4])
	return [r_15, dl_here_15]
def fun16(dc,dr,sr,da,sa):
	r_16=1;
	dl_here_16=[]
	for i in range(dr-sr-1):
		r_16=r_16*best_routes[5][3]
		dl_here_16.append(best_routes[5][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_column[k]==dc:
				if(sr>=0):
					if (faulty_routers_aisle[k]==da and faulty_routers_row[k] <= dr and faulty_routers_row[k] >=sr):
						if len(dl_here_16)>0:
							dl_here_16.pop()
						r_16=r_16/best_routes[5][3]
						r_16=r_16*faulty_routes[k][5][3]
						dl_here_16.append(faulty_routes[k][5][4])
				if(sr<0):
					if (faulty_routers_aisle[k]==da and (faulty_routers_row[k] <= dr or faulty_routers_row[k] >=(row+sr))):
						if len(dl_here_16)>0:
							dl_here_16.pop()
						r_16=r_16/best_routes[5][3]
						r_16=r_16*faulty_routes[k][5][3]
						dl_here_16.append(faulty_routes[k][5][4])
	r_16=r_16*best_routes[9][3]
	dl_here_16.append(best_routes[9][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))) and faulty_routers_column[k]==dc:
				if (faulty_routers_aisle[k] == da):
					if len(dl_here_16)>0:
						dl_here_16.pop()
					r_16=r_16/best_routes[9][3]
					r_16=r_16*faulty_routes[k][9][3]
					dl_here_16.append(faulty_routes[k][9][4])
	for i in range(da-sa-1):
		r_16=r_16*best_routes[24][3]
		dl_here_16.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if ((sr>=0 and faulty_routers_row[k]==sr) or (sr<0 and faulty_routers_row[k]==(sr+row))) and faulty_routers_column[k]==dc:
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_16)>0:
							dl_here_16.pop()
						r_16=r_16/best_routes[24][3]
						r_16=r_16*faulty_routes[k][24][3]
						dl_here_16.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_16)>0:
							dl_here_16.pop()
						r_16=r_16/best_routes[24][3]
						r_16=r_16*faulty_routes[k][24][3]
						dl_here_16.append(faulty_routes[k][24][4])
	return [r_16, dl_here_16]
def fun17(dc,sc,dr,da,sa):
	r_17=1;
	dl_here_17=[]
	for i in range(dc-sc-1):
		r_17=r_17*best_routes[12][3]
		dl_here_17.append(best_routes[12][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if faulty_routers_row[k]==dr:
				if(sc>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[12][3]
						r_17=r_17*faulty_routes[k][12][3]
						dl_here_17.append(faulty_routes[k][12][4])
				if(sc>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[12][3]
						r_17=r_17*faulty_routes[k][12][3]
						dl_here_17.append(faulty_routes[k][12][4])
				if(sc<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[12][3]
						r_17=r_17*faulty_routes[k][12][3]
						dl_here_17.append(faulty_routes[k][12][4])
				if(sc<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[12][3]
						r_17=r_17*faulty_routes[k][12][3]
						dl_here_17.append(faulty_routes[k][12][4])
	r_17=r_17*best_routes[13][3]
	dl_here_17.append(best_routes[13][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k] == dc) and faulty_routers_row[k]==dr:
				if(sa>=0):
					if (faulty_routers_aisle[k] == sa):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[13][3]
						r_17=r_17*faulty_routes[k][13][3]
						dl_here_17.append(faulty_routes[k][13][4])
				if(sa<0):
					if (faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[13][3]
						r_17=r_17*faulty_routes[k][13][3]
						dl_here_17.append(faulty_routes[k][13][4])
	for i in range(da-sa-1):
		r_17=r_17*best_routes[29][3]
		dl_here_17.append(best_routes[29][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if (faulty_routers_column[k]==dc) and faulty_routers_row[k]==dr:
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[29][3]
						r_17=r_17*faulty_routes[k][29][3]
						dl_here_17.append(faulty_routes[k][29][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_17)>0:
							dl_here_17.pop()
						r_17=r_17/best_routes[29][3]
						r_17=r_17*faulty_routes[k][29][3]
						dl_here_17.append(faulty_routes[k][29][4])
	return [r_17, dl_here_17]
def fun18(dc,sc,dr,da,sa):
	r_18=1;
	dl_here_18=[]
	for i in range(dc-sc-1):
		r_18=r_18*best_routes[17][3]
		dl_here_18.append(best_routes[17][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_row[k]==dr:
				if(sc>=0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[17][3]
						r_18=r_18*faulty_routes[k][17][3]
						dl_here_18.append(faulty_routes[k][17][4])
				if(sc>=0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[17][3]
						r_18=r_18*faulty_routes[k][17][3]
						dl_here_18.append(faulty_routes[k][17][4])
				if(sc<0 and sa>=0):
					if (faulty_routers_aisle[k]==sa and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[17][3]
						r_18=r_18*faulty_routes[k][17][3]
						dl_here_18.append(faulty_routes[k][17][4])
				if(sc<0 and sa<0):
					if (faulty_routers_aisle[k]==(aisle+sa) and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[17][3]
						r_18=r_18*faulty_routes[k][17][3]
						dl_here_18.append(faulty_routes[k][17][4])
	r_18=r_18*best_routes[18][3]
	dl_here_18.append(best_routes[18][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if faulty_routers_row[k]==dr and (sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column)):
				if(sa>=0):
					if (faulty_routers_aisle[k] == sa):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[18][3]
						r_18=r_18*faulty_routes[k][18][3]
						dl_here_18.append(faulty_routes[k][18][4])
				if(sa<0):
					if (faulty_routers_aisle[k] == (aisle+sa)):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[18][3]
						r_18=r_18*faulty_routes[k][18][3]
						dl_here_18.append(faulty_routes[k][18][4])
	for i in range(da-sa-1):
		r_18=r_18*best_routes[29][3]
		dl_here_18.append(best_routes[29][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if (sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column)) and faulty_routers_row[k]==dr:
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[29][3]
						r_18=r_18*faulty_routes[k][29][3]
						dl_here_18.append(faulty_routes[k][29][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_18)>0:
							dl_here_18.pop()
						r_18=r_18/best_routes[29][3]
						r_18=r_18*faulty_routes[k][29][3]
						dl_here_18.append(faulty_routes[k][29][4])
	return [r_18, dl_here_18]
def fun19(dc,sc,dr,da,sa):
	r_19=1;
	dl_here_19=[]
	for i in range(dc-sc-1):
		r_19=r_19*best_routes[12][3]
		dl_here_19.append(best_routes[12][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if(sc>=0):
				if ( faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_19)>0:
						dl_here_19.pop()
					r_19=r_19/best_routes[12][3]
					r_19=r_19*faulty_routes[k][12][3]
					dl_here_19.append(faulty_routes[k][12][4])
			if(sc<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_19)>0:
						dl_here_19.pop()
					r_19=r_19/best_routes[12][3]
					r_19=r_19*faulty_routes[k][12][3]
					dl_here_19.append(faulty_routes[k][12][4])
	r_19=r_19*best_routes[14][3]
	dl_here_19.append(best_routes[14][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_row[k]==dr and faulty_routers_column[k] == dc):
				if (faulty_routers_aisle[k] == da):
					if len(dl_here_19)>0:
						dl_here_19.pop()
					r_19=r_19/best_routes[14][3]
					r_19=r_19*faulty_routes[k][14][3]
					dl_here_19.append(faulty_routes[k][14][4])
	for i in range(da-sa-1):
		r_19=r_19*best_routes[24][3]
		dl_here_19.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if (faulty_routers_row[k]==dr and faulty_routers_column[k]==dc):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_19)>0:
							dl_here_19.pop()
						r_19=r_19/best_routes[24][3]
						r_19=r_19*faulty_routes[k][24][3]
						dl_here_19.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_19)>0:
							dl_here_19.pop()
						r_19=r_19/best_routes[24][3]
						r_19=r_19*faulty_routes[k][24][3]
						dl_here_19.append(faulty_routes[k][24][4])
	return [r_19, dl_here_19]
def fun20(dc,sc,dr,da,sa):
	r_20=1;
	dl_here_20=[]
	for i in range(dc-sc-1):
		r_20=r_20*best_routes[17][3]
		dl_here_20.append(best_routes[17][4])
	if number_of_faults >0 :
		for k in range(faulty_routers_num):
			if(sc>=0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and faulty_routers_column[k] <= dc and faulty_routers_column[k] >=sc):
					if len(dl_here_20)>0:
						dl_here_20.pop()
					r_20=r_20/best_routes[17][3]
					r_20=r_20*faulty_routes[k][17][3]
					dl_here_20.append(faulty_routes[k][17][4])
			if(sc<0):
				if (faulty_routers_row[k]==dr and faulty_routers_aisle[k]==da and (faulty_routers_column[k] <= dc or faulty_routers_column[k]>=(column+sc))):
					if len(dl_here_20)>0:
						dl_here_20.pop()
					r_20=r_20/best_routes[17][3]
					r_20=r_20*faulty_routes[k][17][3]
					dl_here_20.append(faulty_routes[k][17][4])
	r_20=r_20*best_routes[19][3]
	dl_here_20.append(best_routes[19][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_row[k]==dr and (sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column)):
				if (faulty_routers_aisle[k] == da):
					if len(dl_here_20)>0:
						dl_here_20.pop()
					r_20=r_20/best_routes[19][3]
					r_20=r_20*faulty_routes[k][19][3]
					dl_here_20.append(faulty_routes[k][19][4])
	for i in range(da-sa-1):
		r_20=r_20*best_routes[24][3]
		dl_here_20.append(best_routes[24][4])
	if number_of_faults >0:
		for k in range(faulty_routers_num):
			if faulty_routers_row[k]==dr and (sc>=0 and faulty_routers_column[k] == sc) or (sc<0 and faulty_routers_column[k] == (sc+column)):
				if(sa>=0):
					if (faulty_routers_aisle[k] <= da and faulty_routers_aisle[k] >=sa):
						if len(dl_here_20)>0:
							dl_here_20.pop()
						r_20=r_20/best_routes[24][3]
						r_20=r_20*faulty_routes[k][24][3]
						dl_here_20.append(faulty_routes[k][24][4])
				if(sa<0):
					if (faulty_routers_aisle[k] <= da or faulty_routers_aisle[k] >=(aisle+sa)):
						if len(dl_here_20)>0:
							dl_here_20.pop()
						r_20=r_20/best_routes[24][3]
						r_20=r_20*faulty_routes[k][24][3]
						dl_here_20.append(faulty_routes[k][24][4])
	return [r_20, dl_here_20]

#########################################################
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
	elif data_3[0]=="size(row,column,aisle):":
		row=int(data_3[1])
		column=int(data_3[2])
		aisle=int(data_3[3])
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
path = start_path+"/Router/saved_routers/saved_3D/"+str(R)+"/"
if dimension=="3D":
	if router_type=="user_defined":
		path = start_path+"/Router/user_defined_routers/user_defined_3D/"+str(R)+"/"
		strl1="cp "+path+"input_user_defined_3D.csv input_user_defined_3D.csv"
		strl2="python "+path+"router_user_defined_3D.py"
		os.system(strl1)
		os.system(strl2)
		with open("routes_user_defined_3D.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open("reliabilities_user_defined_3D.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open("data_loss_user_defined_3D.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_user_defined_3D.csv"
	if router_type==7:
		with open(path+"routes_7.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_7.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_7.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_7.csv"
	if router_type==8:
		with open(path+"routes_8.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_8.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_8.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_8.csv"
	if router_type==10:
		with open(path+"routes_10.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_10.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_10.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_10.csv"
	if router_type==11:
		with open(path+"routes_11.txt", "rb") as fp: 
			routes = pickle.load(fp)
		with open(path+"reliabilities_11.txt", "rb") as fp:
			reliabilities = pickle.load(fp)
		with open(path+"data_loss_11.txt", "rb") as fp:
			data_loss = pickle.load(fp)
		in_path=path+"input_11.csv"
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
	faulty_routers_all=random.sample(range(1, (column*row*aisle)), faulty_routers_num)
	faulty_routers_row=[ int((y%(row*column))/column) for y in faulty_routers_all]
	faulty_routers_column=[ int((y%(row*column))%column) for y in faulty_routers_all]
	faulty_routers_aisle=[ int(y/(column*row)) for y in faulty_routers_all]
	faulty_MRs=[[] for y in range(faulty_routers_num)]
	for i in range(faulty_routers_num):
		if i == faulty_routers_num-1:
			faulty_MRs[i]=faulty_MRs_all[threshold*(i):]
		else:
			for j in range(threshold):
				faulty_MRs[i].append(faulty_MRs_all[threshold*i+j])
	#print(faulty_routers_row)
	#print(faulty_routers_column)
	#print(faulty_routers_aisle)
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
if dimension=="3D":
	routes_north_south=[]
	reliabilities_north_south=[]
	data_loss_north_south=[]
	routes_north_west=[]
	reliabilities_north_west=[]
	data_loss_north_west=[]
	routes_north_east=[]
	reliabilities_north_east=[]
	data_loss_north_east=[]
	routes_north_up=[]
	reliabilities_north_up=[]
	data_loss_north_up=[]
	routes_north_down=[]
	reliabilities_north_down=[]
	data_loss_north_down=[]

	routes_south_north=[]
	reliabilities_south_north=[]
	data_loss_south_north=[]
	routes_south_west=[]
	reliabilities_south_west=[]
	data_loss_south_west=[]
	routes_south_east=[]
	reliabilities_south_east=[]
	data_loss_south_east=[]
	routes_south_up=[]
	reliabilities_south_up=[]
	data_loss_south_up=[]
	routes_south_down=[]
	reliabilities_south_down=[]
	data_loss_south_down=[]

	routes_west_north=[]
	reliabilities_west_north=[]
	data_loss_west_north=[]
	routes_west_south=[]
	reliabilities_west_south=[]
	data_loss_west_south=[]
	routes_west_east=[]
	reliabilities_west_east=[]
	data_loss_west_east=[]
	routes_west_up=[]
	reliabilities_west_up=[]
	data_loss_west_up=[]
	routes_west_down=[]
	reliabilities_west_down=[]
	data_loss_west_down=[]

	routes_east_north=[]
	reliabilities_east_north=[]
	data_loss_east_north=[]
	routes_east_south=[]
	reliabilities_east_south=[]
	data_loss_east_south=[]
	routes_east_west=[]
	reliabilities_east_west=[]
	data_loss_east_west=[]
	routes_east_up=[]
	reliabilities_east_up=[]
	data_loss_east_up=[]
	routes_east_down=[]
	reliabilities_east_down=[]
	data_loss_east_down=[]

	routes_up_north=[]
	reliabilities_up_north=[]
	data_loss_up_north=[]
	routes_up_south=[]
	reliabilities_up_south=[]
	data_loss_up_south=[]
	routes_up_west=[]
	reliabilities_up_west=[]
	data_loss_up_west=[]
	routes_up_east=[]
	reliabilities_up_east=[]
	data_loss_up_east=[]
	routes_up_down=[]
	reliabilities_up_down=[]
	data_loss_up_down=[]

	routes_down_north=[]
	reliabilities_down_north=[]
	data_loss_down_north=[]
	routes_down_south=[]
	reliabilities_down_south=[]
	data_loss_down_south=[]
	routes_down_west=[]
	reliabilities_down_west=[]
	data_loss_down_west=[]
	routes_down_east=[]
	reliabilities_down_east=[]
	data_loss_down_east=[]
	routes_down_up=[]
	reliabilities_down_up=[]
	data_loss_down_up=[]

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
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="up":
				routes_north_up.append(routes[i])
				reliabilities_north_up.append(reliabilities[i])
				data_loss_north_up.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="down":
				routes_north_down.append(routes[i])
				reliabilities_north_down.append(reliabilities[i])
				data_loss_north_down.append(data_loss[i])
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
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="up":
				routes_south_up.append(routes[i])
				reliabilities_south_up.append(reliabilities[i])
				data_loss_south_up.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="down":
				routes_south_down.append(routes[i])
				reliabilities_south_down.append(reliabilities[i])
				data_loss_south_down.append(data_loss[i])
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
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="up":
				routes_west_up.append(routes[i])
				reliabilities_west_up.append(reliabilities[i])
				data_loss_west_up.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="down":
				routes_west_down.append(routes[i])
				reliabilities_west_down.append(reliabilities[i])
				data_loss_west_down.append(data_loss[i])
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
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="up":
				routes_east_up.append(routes[i])
				reliabilities_east_up.append(reliabilities[i])
				data_loss_east_up.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="down":
				routes_east_down.append(routes[i])
				reliabilities_east_down.append(reliabilities[i])
				data_loss_east_down.append(data_loss[i])
		if MRs[routes[i][0][0]-1].source=="up":
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="north":
				routes_up_north.append(routes[i])
				reliabilities_up_north.append(reliabilities[i])
				data_loss_up_north.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="south":
				routes_up_south.append(routes[i])
				reliabilities_up_south.append(reliabilities[i])
				data_loss_up_south.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="west":
				routes_up_west.append(routes[i])
				reliabilities_up_west.append(reliabilities[i])
				data_loss_up_west.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="east":
				routes_up_east.append(routes[i])
				reliabilities_up_east.append(reliabilities[i])
				data_loss_up_east.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="down":
				routes_up_down.append(routes[i])
				reliabilities_up_down.append(reliabilities[i])
				data_loss_up_down.append(data_loss[i])
		if MRs[routes[i][0][0]-1].source=="down":
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="north":
				routes_down_north.append(routes[i])
				reliabilities_down_north.append(reliabilities[i])
				data_loss_down_north.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="south":
				routes_down_south.append(routes[i])
				reliabilities_down_south.append(reliabilities[i])
				data_loss_down_south.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="west":
				routes_down_west.append(routes[i])
				reliabilities_down_west.append(reliabilities[i])
				data_loss_down_west.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="east":
				routes_down_east.append(routes[i])
				reliabilities_down_east.append(reliabilities[i])
				data_loss_down_east.append(data_loss[i])
			if MRs[routes[i][len(routes[i])-1][0]-1].dest=="up":
				routes_down_up.append(routes[i])
				reliabilities_down_up.append(reliabilities[i])
				data_loss_down_up.append(data_loss[i])
	best_routes=[]
	best_routes.append(["north","south",routes_north_south[len(routes_north_south)-1],reliabilities_north_south[len(reliabilities_north_south)-1],data_loss_north_south[len(data_loss_north_south)-1]])
	best_routes.append(["north","west",routes_north_west[len(routes_north_west)-1],reliabilities_north_west[len(reliabilities_north_west)-1],data_loss_north_west[len(data_loss_north_west)-1]])
	best_routes.append(["north","east",routes_north_east[len(routes_north_east)-1],reliabilities_north_east[len(reliabilities_north_east)-1],data_loss_north_east[len(data_loss_north_east)-1]])
	best_routes.append(["north","up",routes_north_up[len(routes_north_up)-1],reliabilities_north_up[len(reliabilities_north_up)-1],data_loss_north_up[len(data_loss_north_up)-1]])
	best_routes.append(["north","down",routes_north_down[len(routes_north_down)-1],reliabilities_north_down[len(reliabilities_north_down)-1],data_loss_north_down[len(data_loss_north_down)-1]])

	best_routes.append(["south","north",routes_south_north[len(routes_south_north)-1],reliabilities_south_north[len(reliabilities_south_north)-1],data_loss_south_north[len(data_loss_south_north)-1]])
	best_routes.append(["south","west",routes_south_west[len(routes_south_west)-1],reliabilities_south_west[len(reliabilities_south_west)-1],data_loss_south_west[len(data_loss_south_west)-1]])
	best_routes.append(["south","east",routes_south_east[len(routes_south_east)-1],reliabilities_south_east[len(reliabilities_south_east)-1],data_loss_south_east[len(data_loss_south_east)-1]])
	best_routes.append(["south","up",routes_south_up[len(routes_south_up)-1],reliabilities_south_up[len(reliabilities_south_up)-1],data_loss_south_up[len(data_loss_south_up)-1]])
	best_routes.append(["south","down",routes_south_down[len(routes_south_down)-1],reliabilities_south_down[len(reliabilities_south_down)-1],data_loss_south_down[len(data_loss_south_down)-1]])

	best_routes.append(["west","north",routes_west_north[len(routes_west_north)-1],reliabilities_west_north[len(reliabilities_west_north)-1],data_loss_west_north[len(data_loss_west_north)-1]])
	best_routes.append(["west","south",routes_west_south[len(routes_west_south)-1],reliabilities_west_south[len(reliabilities_west_south)-1],data_loss_west_south[len(data_loss_west_south)-1]])
	best_routes.append(["west","east",routes_west_east[len(routes_west_east)-1],reliabilities_west_east[len(reliabilities_west_east)-1],data_loss_west_east[len(data_loss_west_east)-1]])
	best_routes.append(["west","up",routes_west_up[len(routes_west_up)-1],reliabilities_west_up[len(reliabilities_west_up)-1],data_loss_west_up[len(data_loss_west_up)-1]])
	best_routes.append(["west","down",routes_west_down[len(routes_west_down)-1],reliabilities_west_down[len(reliabilities_west_down)-1],data_loss_west_down[len(data_loss_west_down)-1]])

	best_routes.append(["east","north",routes_east_north[len(routes_east_north)-1],reliabilities_east_north[len(reliabilities_east_north)-1],data_loss_east_north[len(data_loss_east_north)-1]])
	best_routes.append(["east","south",routes_east_south[len(routes_east_south)-1],reliabilities_east_south[len(reliabilities_east_south)-1],data_loss_east_south[len(data_loss_east_south)-1]])
	best_routes.append(["east","west",routes_east_west[len(routes_east_west)-1],reliabilities_east_west[len(reliabilities_east_west)-1],data_loss_east_west[len(data_loss_east_west)-1]])
	best_routes.append(["east","up",routes_east_up[len(routes_east_up)-1],reliabilities_east_up[len(reliabilities_east_up)-1],data_loss_east_up[len(data_loss_east_up)-1]])
	best_routes.append(["east","down",routes_east_down[len(routes_east_down)-1],reliabilities_east_down[len(reliabilities_east_down)-1],data_loss_east_down[len(data_loss_east_down)-1]])

	best_routes.append(["up","north",routes_up_north[len(routes_up_north)-1],reliabilities_up_north[len(reliabilities_up_north)-1],data_loss_up_north[len(data_loss_up_north)-1]])
	best_routes.append(["up","south",routes_up_south[len(routes_up_south)-1],reliabilities_up_south[len(reliabilities_up_south)-1],data_loss_up_south[len(data_loss_up_south)-1]])
	best_routes.append(["up","west",routes_up_west[len(routes_up_west)-1],reliabilities_up_west[len(reliabilities_up_west)-1],data_loss_up_west[len(data_loss_up_west)-1]])
	best_routes.append(["up","east",routes_up_east[len(routes_up_east)-1],reliabilities_up_east[len(reliabilities_up_east)-1],data_loss_up_east[len(data_loss_up_east)-1]])
	best_routes.append(["up","down",routes_up_down[len(routes_up_down)-1],reliabilities_up_down[len(reliabilities_up_down)-1],data_loss_up_down[len(data_loss_up_down)-1]])

	best_routes.append(["down","north",routes_down_north[len(routes_down_north)-1],reliabilities_down_north[len(reliabilities_down_north)-1],data_loss_down_north[len(data_loss_down_north)-1]])
	best_routes.append(["down","south",routes_down_south[len(routes_down_south)-1],reliabilities_down_south[len(reliabilities_down_south)-1],data_loss_down_south[len(data_loss_down_south)-1]])
	best_routes.append(["down","west",routes_down_west[len(routes_down_west)-1],reliabilities_down_west[len(reliabilities_down_west)-1],data_loss_down_west[len(data_loss_down_west)-1]])
	best_routes.append(["down","east",routes_down_east[len(routes_down_east)-1],reliabilities_down_east[len(reliabilities_down_east)-1],data_loss_down_east[len(data_loss_down_east)-1]])
	best_routes.append(["down","up",routes_down_up[len(routes_down_up)-1],reliabilities_down_up[len(reliabilities_down_up)-1],data_loss_down_up[len(data_loss_down_up)-1]])
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
			for i in range(len(routes_north_up)-1,0,-1):
				ok=1
				for j in routes_north_up[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["north","up",routes_north_up[i],reliabilities_north_up[i],data_loss_north_up[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["north","up",[],0,[]])
			flag=0
			for i in range(len(routes_north_down)-1,0,-1):
				ok=1
				for j in routes_north_down[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["north","down",routes_north_down[i],reliabilities_north_down[i],data_loss_north_down[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["north","down",[],0,[]])
	#######################################################################
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
			for i in range(len(routes_south_up)-1,0,-1):
				ok=1
				for j in routes_south_up[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["south","up",routes_south_up[i],reliabilities_south_up[i],data_loss_south_up[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["south","up",[],0,[]])
			flag=0
			for i in range(len(routes_south_down)-1,0,-1):
				ok=1
				for j in routes_south_down[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["south","down",routes_south_down[i],reliabilities_south_down[i],data_loss_south_down[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["south","down",[],0,[]])
	#######################################################################
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
			for i in range(len(routes_west_up)-1,0,-1):
				ok=1
				for j in routes_west_up[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["west","up",routes_west_up[i],reliabilities_west_up[i],data_loss_west_up[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["west","up",[],0,[]])
			flag=0
			for i in range(len(routes_west_down)-1,0,-1):
				ok=1
				for j in routes_west_down[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["west","down",routes_west_down[i],reliabilities_west_down[i],data_loss_west_down[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["west","down",[],0,[]])
	######################################################################
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
			flag=0
			for i in range(len(routes_east_up)-1,0,-1):
				ok=1
				for j in routes_east_up[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["east","up",routes_east_up[i],reliabilities_east_up[i],data_loss_east_up[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["east","up",[],0,[]])
			flag=0
			for i in range(len(routes_east_down)-1,0,-1):
				ok=1
				for j in routes_east_down[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["east","down",routes_east_down[i],reliabilities_east_down[i],data_loss_east_down[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["east","down",[],0,[]])
	######################################################################
			flag=0
			for i in range(len(routes_up_north)-1,0,-1):
				ok=1
				for j in routes_up_north[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["up","north",routes_up_north[i],reliabilities_up_north[i],data_loss_up_north[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["up","north",[],0,[]])
			flag=0
			for i in range(len(routes_up_south)-1,0,-1):
				ok=1
				for j in routes_up_south[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["up","south",routes_up_south[i],reliabilities_up_south[i],data_loss_up_south[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["up","south",[],0,[]])
			flag=0
			for i in range(len(routes_up_west)-1,0,-1):
				ok=1
				for j in routes_up_west[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["up","west",routes_up_west[i],reliabilities_up_west[i],data_loss_up_west[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["up","west",[],0,[]])
			flag=0
			for i in range(len(routes_up_east)-1,0,-1):
				ok=1
				for j in routes_up_east[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["up","east",routes_up_east[i],reliabilities_up_east[i],data_loss_up_east[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["up","east",[],0,[]])
			flag=0
			for i in range(len(routes_up_down)-1,0,-1):
				ok=1
				for j in routes_up_down[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["up","down",routes_up_down[i],reliabilities_up_down[i],data_loss_up_down[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["up","down",[],0,[]])
	######################################################################
			flag=0
			for i in range(len(routes_down_north)-1,0,-1):
				ok=1
				for j in routes_down_north[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["down","north",routes_down_north[i],reliabilities_down_north[i],data_loss_down_north[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["down","north",[],0,[]])
			flag=0
			for i in range(len(routes_down_south)-1,0,-1):
				ok=1
				for j in routes_down_south[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["down","south",routes_down_south[i],reliabilities_down_south[i],data_loss_down_south[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["down","south",[],0,[]])
			flag=0
			for i in range(len(routes_down_west)-1,0,-1):
				ok=1
				for j in routes_down_west[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["down","west",routes_down_west[i],reliabilities_down_west[i],data_loss_down_west[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["down","west",[],0,[]])
			flag=0
			for i in range(len(routes_down_east)-1,0,-1):
				ok=1
				for j in routes_down_east[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["down","east",routes_down_east[i],reliabilities_down_east[i],data_loss_down_east[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["down","east",[],0,[]])
			flag=0
			for i in range(len(routes_down_up)-1,0,-1):
				ok=1
				for j in routes_down_up[i]:
					if j[0] in faulty_MRs[k]:
						if j[1]=="on":
							ok=0
				if ok==1:
					faulty_routes[k].append(["down","up",routes_down_up[i],reliabilities_down_up[i],data_loss_down_up[i]])
					flag=1
					break
			if flag ==0:
				faulty_routes[k].append(["down","up",[],0,[]])
		#for i in best_routes:
		#	print(i)
		#print("############################################################")
		#for i in faulty_routes[k]:
		#	print(i)
########################################################################################################################
	if topology_type=="mesh":
		for i in range(len(data_2)-1):
			data_3=data_2[i].split('\t')
			source_row=int(data_3[0])
			source_column=int(data_3[1])
			source_aisle=int(data_3[2])
			dest_row=int(data_3[3])
			dest_column=int(data_3[4])
			dest_aisle=int(data_3[5])
			r=1
			dl_here=[]
			if dest_aisle > source_aisle:
				if dest_column > source_column and dest_row > source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column > source_column and dest_row < source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle)
					r=r*r_here
					dl_here.append(dl_here_1) 
				if dest_column < source_column and dest_row > source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column < source_column and dest_row < source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column == source_column:
					if dest_row < source_row:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun14(dest_column,source_row,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					if dest_row > source_row:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun13(dest_column,dest_row,source_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
				if dest_row == source_row:
					if dest_column < source_column:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun18(source_column,dest_column,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					if dest_column > source_column:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun17(dest_column,source_column,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
				if dest_row == source_row and dest_column == source_column:
					for j in range(dest_aisle-source_aisle-1):
						r=r*best_routes[29][3]
						dl_here.append(best_routes[29][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and faulty_routers_aisle[k] <= dest_aisle and faulty_routers_aisle[k] >=source_aisle):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[29][3]
								r=r*faulty_routes[k][29][3]
								dl_here.append(faulty_routes[k][29][4])
			elif dest_aisle < source_aisle:
				if dest_column > source_column and dest_row > source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column > source_column and dest_row < source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row,source_aisle,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column < source_column and dest_row > source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column < source_column and dest_row < source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column == source_column:
					if dest_row < source_row:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun16(dest_column,source_row,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					if dest_row > source_row:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun15(dest_column,dest_row,source_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
				if dest_row == source_row:
					if dest_column < source_column:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun20(source_column,dest_column,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					if dest_column > source_column:
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun19(dest_column,source_column,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
				if dest_row == source_row and dest_column == source_column:
					for j in range(source_aisle-dest_aisle-1):
						r=r*best_routes[24][3]
						dl_here.append(best_routes[24][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and faulty_routers_aisle[k] <= source_aisle and faulty_routers_aisle[k] >=dest_aisle):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[24][3]
								r=r*faulty_routes[k][24][3]
								dl_here.append(faulty_routes[k][24][4])
			else:
				if dest_column > source_column and dest_row > source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun9(dest_column,source_column,dest_row,source_row,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column > source_column and dest_row < source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun10(dest_column,source_column,source_row,dest_row,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column < source_column and dest_row > source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun11(source_column,dest_column,dest_row,source_row,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column < source_column and dest_row < source_row:
					r_here=0
					dl_here_1 = []
					[r_here,dl_here_1] = fun12(source_column,dest_column,source_row,dest_row,dest_aisle)
					r=r*r_here
					dl_here.append(dl_here_1)
				if dest_column == source_column:
					if dest_row < source_row:
						for j in range(source_row-dest_row-1):
							r=r*best_routes[5][3]
							dl_here.append(best_routes[5][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[5][3]
									r=r*faulty_routes[k][5][3]
									dl_here.append(faulty_routes[k][5][4])
					if dest_row > source_row:
						for j in range(dest_row-source_row-1):
							r=r*best_routes[0][3]
							dl_here.append(best_routes[0][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
				if dest_row == source_row:
					if dest_column < source_column:
						for j in range(source_column-dest_column-1):
							r=r*best_routes[17][3]
							dl_here.append(best_routes[17][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[17][3]
									r=r*faulty_routes[k][17][3]
									dl_here.append(faulty_routes[k][17][4])
					if dest_column > source_column:
						for j in range(dest_column-source_column-1):
							r=r*best_routes[12][3]
							dl_here.append(best_routes[12][4])
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[12][3]
									r=r*faulty_routes[k][12][3]
									dl_here.append(faulty_routes[k][12][4])
			traffic_reliability.append(r)
			traffic_data_loss[i]=dl_here
#########################################################################################################
	if topology_type=="torus":
		for i in range(len(data_2)-1):
			data_3=data_2[i].split('\t')
			source_row=int(data_3[0])
			source_column=int(data_3[1])
			source_aisle=int(data_3[2])
			dest_row=int(data_3[3])
			dest_column=int(data_3[4])
			dest_aisle=int(data_3[5])
			r=1
			dl_here=[]
			#########################---------------1-----------------#####################			
			if dest_aisle>source_aisle and dest_column>source_column and dest_row>source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#1 - 12,11,0,3,29
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#2 - 12,10,5,8,29
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#3 - 17,16,0,3,29
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#4 - 17,15,5,8,29
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#5 - 12,11,0,4,24
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#6 - 12,10,5,9,24
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#7 - 17,16,0,4,24
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#8 - 17,15,5,9,24
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)						
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			##################--------------2-----------------####################						
			if dest_aisle>source_aisle and dest_column>source_column and dest_row<source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#2
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1) 
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#1 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#4
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#3 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] =  fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#6
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#5
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#8
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#7 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] =  fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			######################------------3--------------####################						
			if dest_aisle>source_aisle and dest_column<source_column and dest_row>source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#3 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#4
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#1
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#2 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#7 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#8 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#5 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#6
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)						
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle-aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			###################------------4-----------------####################						
			if dest_aisle>source_aisle and dest_column<source_column and dest_row<source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#4
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#3
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#2
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#1
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#8
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#7
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#6
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#5
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)						
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			######################------------5--------------####################						
			if dest_aisle<source_aisle and dest_column>source_column and dest_row>source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#5 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#6 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#7
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#8 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#1
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#2
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#3
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#4 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun2(dest_column,source_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun3(source_column,dest_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun4(source_column,dest_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun5(dest_column,source_column,dest_row,source_row,source_aisle,dest_aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun7(source_column,dest_column-column,dest_row,source_row,source_aisle,dest_aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun8(source_column,dest_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			###################------------6-----------------####################						
			if dest_aisle<source_aisle and dest_column>source_column and dest_row<source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#6
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#5 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#8
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#7 
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] =  fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#2
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1) 
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#1
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#4
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#3
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1) 
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] =  fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun2(dest_column,source_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun1(dest_column,source_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun4(source_column,dest_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun3(source_column,dest_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun6(dest_column,source_column,source_row,dest_row-row,source_aisle,dest_aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun5(dest_column,source_column,dest_row,source_row-row,source_aisle,dest_aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun8(source_column,dest_column-column,source_row,dest_row,source_aisle,dest_aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun7(source_column,dest_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			#####################---------------7-------------####################						
			if dest_aisle<source_aisle and dest_column<source_column and dest_row>source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#7
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#8
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#5
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#6
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#3
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#4
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (dest_row-source_row) < (source_row + row-dest_row):
							#1
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (dest_row-source_row) > (source_row + row-dest_row):
							#2
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun4(source_column,dest_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun1(dest_column,source_column-column,dest_row,source_row,dest_aisle,source_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun2(dest_column,source_column-column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun7(source_column,dest_column,dest_row,source_row,source_aisle,dest_aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun8(source_column,dest_column,source_row,dest_row-row,source_aisle,dest_aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun5(dest_column,source_column-column,dest_row,source_row,source_aisle,dest_aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun6(dest_column,source_column-column,source_row,dest_row-row,source_aisle,dest_aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			####################-------------8-----------------####################						
			if dest_aisle<source_aisle and dest_column<source_column and dest_row<source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#8
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#7
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#6
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#5
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if(source_column-dest_column) < (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#4
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#3
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						if (source_row-dest_row) < (dest_row + row-source_row):
							#2
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						elif (source_row-dest_row) > (dest_row + row-source_row):
							#1
							r_here=0
							dl_here_1 = []
							[r_here,dl_here_1] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							r=r*r_here
							dl_here.append(dl_here_1)
						else:
							r_here_1=0
							dl_here_1 = []
							[r_here_1,dl_here_1] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
							r_here_2=0
							dl_here_2 = []
							[r_here_2,dl_here_2] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
							if r_here_1 <= r_here_2:
								r=r*r_here_1
								dl_here.append(dl_here_1)
							else:
								r=r*r_here_2
								dl_here.append(dl_here_2)
					else:
						mini=0
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
						mini=r_here_1
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
						if r_here_2<= r_here_1:
							mini =r_here_2
						r_here_3=0
						dl_here_3 = []
						[r_here_3,dl_here_3] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
						if r_here_3<= mini:
							mini =r_here_3
						r_here_4=0
						dl_here_4 = []
						[r_here_4,dl_here_4] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
						if r_here_4<= mini:
							mini =r_here_4
						if mini==r_here_1:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						elif mini==r_here_2:
							r=r*r_here_2
							dl_here.append(dl_here_2)
						elif mini==r_here_3:
							r=r*r_here_3
							dl_here.append(dl_here_3)
						elif mini==r_here_4:
							r=r*r_here_4
							dl_here.append(dl_here_4)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun4(source_column,dest_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun3(source_column,dest_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun2(dest_column,source_column-column,source_row,dest_row,dest_aisle,source_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun1(dest_column,source_column-column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					r_here_5=0
					dl_here_5 = []
					[r_here_5,dl_here_5] = fun8(source_column,dest_column,source_row,dest_row,source_aisle,dest_aisle)
					if r_here_5<= mini:
						mini =r_here_5
					r_here_6=0
					dl_here_6 = []
					[r_here_6,dl_here_6] = fun7(source_column,dest_column,dest_row,source_row-row,source_aisle,dest_aisle)
					if r_here_6<= mini:
						mini =r_here_6
					r_here_7=0
					dl_here_7 = []
					[r_here_7,dl_here_7] = fun6(dest_column,source_column-column,source_row,dest_row,source_aisle,dest_aisle)
					if r_here_7<= mini:
						mini =r_here_7
					r_here_8=0
					dl_here_8 = []
					[r_here_8,dl_here_8] = fun5(dest_column,source_column-column,dest_row,source_row-row,source_aisle,dest_aisle)
					if r_here_8<= mini:
						mini =r_here_8
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
					elif mini==r_here_5:
						r=r*r_here_5
						dl_here.append(dl_here_5)
					elif mini==r_here_6:
						r=r*r_here_6
						dl_here.append(dl_here_6)
					elif mini==r_here_7:
						r=r*r_here_7
						dl_here.append(dl_here_7)
					elif mini==r_here_8:
						r=r*r_here_8
						dl_here.append(dl_here_8)
			######################-------------9--------------####################						
			if dest_aisle==source_aisle and dest_column>source_column and dest_row>source_row:
				if (dest_column-source_column) < (source_column + column-dest_column):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#9 - 12,11,0
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun9(dest_column,source_column,dest_row,source_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#10 - 12,10,5
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun10(dest_column,source_column,source_row,dest_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun9(dest_column,source_column,source_row,dest_row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun10(dest_column,source_column,source_row,dest_row-row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (dest_column-source_column) > (source_column + column-dest_column):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#11 - 17,16,0
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun11(source_column,dest_column-column,dest_row,source_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#12 - 17,15,5
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun12(source_column,dest_column-column,source_row,dest_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun11(source_column,dest_column-column,dest_row,source_row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun12(source_column,dest_column-column,source_row,dest_row-row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun9(dest_column,source_column,dest_row,source_row,dest_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun10(dest_column,source_column,source_row,dest_row-row,dest_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun11(source_column,dest_column-column,dest_row,source_row,dest_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun12(source_column,dest_column-column,source_row,dest_row-row,dest_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			######################-------------10--------------####################						
			if dest_aisle==source_aisle and dest_column>source_column and dest_row<source_row:
				if (dest_column-source_column) < (source_column + column-dest_column):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#10
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun10(dest_column,source_column,source_row,dest_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#9
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun9(dest_column,source_column,dest_row,source_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun9(dest_column,source_column,dest_row,source_row-row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun10(dest_column,source_column,source_row,dest_row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (dest_column-source_column) > (source_column + column-dest_column):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#12
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun12(source_column,dest_column-column,source_row,dest_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#11
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun11(source_column,dest_column-column,dest_row,source_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun12(source_column,dest_column-column,source_row,dest_row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun11(source_column,dest_column-column,dest_row,source_row-row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun9(dest_column,source_column,dest_row,source_row-row,dest_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun10(dest_column,source_column,source_row,dest_row,dest_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun12(source_column,dest_column-column,source_row,dest_row,dest_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun11(source_column,dest_column-column,dest_row,source_row-row,dest_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			######################--------------11-------------####################						
			if dest_aisle==source_aisle and dest_column<source_column and dest_row>source_row:
				if (source_column-dest_column) < (dest_column + column-source_column):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#11
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun11(source_column,dest_column,dest_row,source_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#12
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun12(source_column,dest_column,source_row,dest_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun11(source_column,dest_column,dest_row,source_row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun12(source_column,dest_column,source_row,dest_row-row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (source_column-dest_column) > (dest_column + column-source_column):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#9
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun9(dest_column,source_column-column,dest_row,source_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#10
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun10(dest_column,source_column-column,source_row,dest_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun9(dest_column,source_column-column,source_row,dest_row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun10(dest_column,source_column-column,source_row,dest_row-row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun9(dest_column,source_column-column,dest_row,source_row,dest_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun10(dest_column,source_column-column,source_row,dest_row-row,dest_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun11(source_column,dest_column,dest_row,source_row,dest_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun12(source_column,dest_column,source_row,dest_row-row,dest_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			#######################---------------12-----------####################						
			if dest_aisle==source_aisle and dest_column<source_column and dest_row<source_row:
				if (source_column-dest_column) < (dest_column + column-source_column):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#12
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun12(source_column,dest_column,source_row,dest_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#11
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun11(source_column,dest_column,dest_row,source_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun12(source_column,dest_column,source_row,dest_row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun11(source_column,dest_column,dest_row,source_row-row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif(source_column-dest_column) > (dest_column + column-source_column):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#10
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun10(dest_column,source_column-column,source_row,dest_row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#9
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun9(dest_column,source_column-column,dest_row,source_row-row,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun9(dest_column,source_column-column,dest_row,source_row-row,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun10(dest_column,source_column-column,source_row,dest_row,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun9(dest_column,source_column-column,dest_row,source_row-row,dest_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun10(dest_column,source_column-column,source_row,dest_row,dest_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun12(source_column,dest_column,source_row,dest_row,dest_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun11(source_column,dest_column,dest_row,source_row-row,dest_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			#####################---------------13-------------####################						
			if dest_aisle>source_aisle and dest_column==source_column and dest_row>source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#13 - 0,3,29
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun13(dest_column,dest_row,source_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#14 - 5,8,29
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun14(dest_column,source_row,dest_row-row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun13(dest_column,dest_row,source_row,dest_aisle,source_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun14(dest_column,source_row,dest_row-row,dest_aisle,source_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#15 - 0,4,24
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun15(dest_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#16 - 5,9,24
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun16(dest_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun15(dest_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun16(dest_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun13(dest_column,dest_row,source_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun14(dest_column,source_row,dest_row-row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun15(dest_column,dest_row,source_row,source_aisle,dest_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun16(dest_column,source_row,dest_row-row,source_aisle,dest_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			###################---------------14--------------####################						
			if dest_aisle>source_aisle and dest_column==source_column and dest_row<source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#14
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun14(dest_column,source_row,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#13
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun13(dest_column,dest_row,source_row-row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun14(dest_column,source_row,dest_row,dest_aisle,source_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun13(dest_column,dest_row,source_row-row,dest_aisle,source_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#16
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun16(dest_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#15
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun15(dest_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun16(dest_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun15(dest_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun14(dest_column,source_row,dest_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun13(dest_column,dest_row,source_row-row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun16(dest_column,source_row,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun15(dest_column,dest_row,source_row-row,source_aisle,dest_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			################---------------15-----------------####################						
			if dest_aisle<source_aisle and dest_column==source_column and dest_row>source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#15
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun15(dest_column,dest_row,source_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#16
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun16(dest_column,source_row,dest_row-row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun15(dest_column,dest_row,source_row,source_aisle,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun16(dest_column,source_row,dest_row-row,source_aisle,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if (dest_row-source_row) < (source_row + row-dest_row):
						#13
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun13(dest_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_row-source_row) > (source_row + row-dest_row):
						#14
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun14(dest_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun13(dest_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun14(dest_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun15(dest_column,dest_row,source_row,source_aisle,dest_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun16(dest_column,source_row,dest_row-row,source_aisle,dest_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun13(dest_column,dest_row,source_row,dest_aisle,source_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun14(dest_column,source_row,dest_row-row,dest_aisle,source_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			################---------------16-----------------####################						
			if dest_aisle<source_aisle and dest_column==source_column and dest_row<source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#16
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun16(dest_column,source_row,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#15
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun15(dest_column,dest_row,source_row-row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun16(dest_column,source_row,dest_row,source_aisle,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun15(dest_column,dest_row,source_row-row,source_aisle,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if (source_row-dest_row) < (dest_row + row-source_row):
						#14
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun14(dest_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_row-dest_row) > (dest_row + row-source_row):
						#13
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun13(dest_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun14(dest_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun13(dest_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun14(dest_column,source_row,dest_row,dest_aisle,source_aisle-aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun13(dest_column,dest_row,source_row-row,dest_aisle,source_aisle-aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun16(dest_column,source_row,dest_row,source_aisle,dest_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun15(dest_column,dest_row,source_row-row,source_aisle,dest_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			#################---------------17-----------------####################						
			if dest_aisle>source_aisle and dest_column>source_column and dest_row==source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						#17 - 12,13,29
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun17(dest_column,source_column,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						#18 - 17,18,29
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun18(source_column,dest_column-column,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun17(dest_column,source_column,dest_row,dest_aisle,source_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun18(source_column,dest_column-column,dest_row,dest_aisle,source_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						#19 - 12,14,24
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun19(dest_column,source_column,dest_row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						#20 - 17,19,24
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun20(source_column,dest_column-column,dest_row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun19(dest_column,source_column,dest_row,source_aisle,dest_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun20(source_column,dest_column-column,dest_row,source_aisle,dest_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun17(dest_column,source_column,dest_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun18(source_column,dest_column-column,dest_row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun19(dest_column,source_column,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun20(source_column,dest_column-column,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			#################---------------18-----------------####################						
			if dest_aisle>source_aisle and dest_column<source_column and dest_row==source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						#18
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun18(source_column,dest_column,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						#17
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun17(dest_column,source_column-column,dest_row,dest_aisle,source_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun18(source_column,dest_column,dest_row,dest_aisle,source_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun17(dest_column,source_column-column,dest_row,dest_aisle,source_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						#20
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun20(source_column,dest_column,dest_row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						#19
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun19(dest_column,source_column-column,dest_row,source_aisle,dest_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun20(source_column,dest_column,dest_row,source_aisle,dest_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun19(dest_column,source_column-column,dest_row,source_aisle,dest_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun18(source_column,dest_column,dest_row,dest_aisle,source_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun17(dest_column,source_column-column,dest_row,dest_aisle,source_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun20(source_column,dest_column,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun19(dest_column,source_column-column,dest_row,source_aisle,dest_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			#################---------------19-----------------####################						
			if dest_aisle<source_aisle and dest_column>source_column and dest_row==source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						#19
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun19(dest_column,source_column,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						#20
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun20(source_column,dest_column-column,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun19(dest_column,source_column,dest_row,source_aisle,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun20(source_column,dest_column-column,dest_row,source_aisle,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if (dest_column-source_column) < (source_column + column-dest_column):
						#17
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun17(dest_column,source_column,dest_row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (dest_column-source_column) > (source_column + column-dest_column):
						#18
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun18(source_column,dest_column-column,dest_row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun17(dest_column,source_column,dest_row,dest_aisle,source_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun18(source_column,dest_column-column,dest_row,dest_aisle,source_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun19(dest_column,source_column,dest_row,source_aisle,dest_aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun20(source_column,dest_column-column,dest_row,source_aisle,dest_aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun17(dest_column,source_column,dest_row,dest_aisle,source_aisle-aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun18(source_column,dest_column-column,dest_row,dest_aisle,source_aisle-aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			#################---------------20-----------------####################						
			if dest_aisle<source_aisle and dest_column<source_column and dest_row==source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						#20
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun20(source_column,dest_column,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						#19
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun19(dest_column,source_column-column,dest_row,source_aisle,dest_aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun20(source_column,dest_column,dest_row,source_aisle,dest_aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun19(dest_column,source_column-column,dest_row,source_aisle,dest_aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					if (source_column-dest_column) < (dest_column + column-source_column):
						#18
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun18(source_column,dest_column,dest_row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					elif (source_column-dest_column) > (dest_column + column-source_column):
						#17
						r_here=0
						dl_here_1 = []
						[r_here,dl_here_1] = fun17(dest_column,source_column-column,dest_row,dest_aisle,source_aisle-aisle)
						r=r*r_here
						dl_here.append(dl_here_1)
					else:
						r_here_1=0
						dl_here_1 = []
						[r_here_1,dl_here_1] = fun18(source_column,dest_column,dest_row,dest_aisle,source_aisle-aisle)
						r_here_2=0
						dl_here_2 = []
						[r_here_2,dl_here_2] = fun17(dest_column,source_column-column,dest_row,dest_aisle,source_aisle-aisle)
						if r_here_1 <= r_here_2:
							r=r*r_here_1
							dl_here.append(dl_here_1)
						else:
							r=r*r_here_2
							dl_here.append(dl_here_2)
				else:
					mini=0
					r_here_1=0
					dl_here_1 = []
					[r_here_1,dl_here_1] = fun18(source_column,dest_column,dest_row,dest_aisle,source_aisle-aisle)
					mini=r_here_1
					r_here_2=0
					dl_here_2 = []
					[r_here_2,dl_here_2] = fun17(dest_column,source_column-column,dest_row,dest_aisle,source_aisle-aisle)
					if r_here_2<= r_here_1:
						mini =r_here_2
					r_here_3=0
					dl_here_3 = []
					[r_here_3,dl_here_3] = fun20(source_column,dest_column,dest_row,source_aisle,dest_aisle)
					if r_here_3<= mini:
						mini =r_here_3
					r_here_4=0
					dl_here_4 = []
					[r_here_4,dl_here_4] = fun19(dest_column,source_column-column,dest_row,source_aisle,dest_aisle)
					if r_here_4<= mini:
						mini =r_here_4
					if mini==r_here_1:
						r=r*r_here_1
						dl_here.append(dl_here_1)
					elif mini==r_here_2:
						r=r*r_here_2
						dl_here.append(dl_here_2)
					elif mini==r_here_3:
						r=r*r_here_3
						dl_here.append(dl_here_3)
					elif mini==r_here_4:
						r=r*r_here_4
						dl_here.append(dl_here_4)
			################---------------21-----------------####################						
			if dest_aisle==source_aisle and dest_column==source_column and dest_row>source_row:
				if (dest_row-source_row) < (source_row + row-dest_row):
					for i in range(dest_row-source_row-1):
						r=r*best_routes[0][3]
						dl_here.append(best_routes[0][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[0][3]
								r=r*faulty_routes[k][0][3]
								dl_here.append(faulty_routes[k][0][4])
				elif (dest_row-source_row) > (source_row + row-dest_row):
					for i in range(source_row + row-dest_row-1):
						r=r*best_routes[5][3]
						dl_here.append(best_routes[5][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[5][3]
								r=r*faulty_routes[k][5][3]
								dl_here.append(faulty_routes[k][5][4])
				else:
					r1=1
					r2=1
					dl_here_1=[]
					dl_here_2=[]
					for i in range(dest_row-source_row-1):
						r1=r1*best_routes[0][3]
						dl_here_1.append(best_routes[0][4])
					for i in range(source_row + row-dest_row-1):
						r2=r2*best_routes[5][3]
						dl_here_2.append(best_routes[5][4])
					if r1<=r2:
						r=r*r1
						dl_here.append(dl_here_1)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and faulty_routers_row[k] <= dest_row and faulty_routers_row[k] >=source_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
					else:
						r=r*r2
						dl_here.append(dl_here_2)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_row[k] <= source_row or faulty_routers_row[k] >=dest_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[5][3]
									r=r*faulty_routes[k][5][3]
									dl_here.append(faulty_routes[k][5][4])
			################---------------22-----------------####################						
			if dest_aisle==source_aisle and dest_column==source_column and dest_row<source_row:
				if (source_row-dest_row) < (dest_row + row-source_row):
					for i in range(source_row-dest_row-1):
						r=r*best_routes[5][3]
						dl_here.append(best_routes[5][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[5][3]
								r=r*faulty_routes[k][5][3]
								dl_here.append(faulty_routes[k][5][4])
				elif (source_row-dest_row) > (dest_row + row-source_row):
					for i in range(dest_row + row-source_row-1):
						r=r*best_routes[0][3]
						dl_here.append(best_routes[0][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[0][3]
								r=r*faulty_routes[k][0][3]
								dl_here.append(faulty_routes[k][0][4])
				else:
					r1=1
					r2=1
					dl_here_1=[]
					dl_here_2=[]
					for i in range(source_row-dest_row-1):
						r1=r1*best_routes[5][3]
						dl_here_1.append(best_routes[5][4])
					for i in range(dest_row + row-source_row-1):
						r2=r2*best_routes[0][3]
						dl_here_2.append(best_routes[0][4])
					if r1<=r2:
						r=r*r1
						dl_here.append(dl_here_1)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and faulty_routers_row[k] <= source_row and faulty_routers_row[k] >=dest_row):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[5][3]
									r=r*faulty_routes[k][5][3]
									dl_here.append(faulty_routes[k][5][4])
					else:
						r=r*r2
						dl_here.append(dl_here_2)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_column[k]==dest_column and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_row[k] <= dest_row or faulty_routers_row[k] >=source_row)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[0][3]
									r=r*faulty_routes[k][0][3]
									dl_here.append(faulty_routes[k][0][4])
			#################---------------23-----------------####################						
			if dest_aisle==source_aisle and dest_column>source_column and dest_row==source_row:
				if (dest_column-source_column) < (source_column + column-dest_column):
					for i in range(dest_column-source_column-1):
						r=r*best_routes[12][3]
						dl_here.append(best_routes[12][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[12][3]
								r=r*faulty_routes[k][12][3]
								dl_here.append(faulty_routes[k][12][4])
				elif (dest_column-source_column) > (source_column + column-dest_column):
					for i in range(source_column + column-dest_column-1):
						r=r*best_routes[17][3]
						dl_here.append(best_routes[17][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[17][3]
								r=r*faulty_routes[k][17][3]
								dl_here.append(faulty_routes[k][17][4])
				else:
					r1=1
					r2=1
					dl_here_1=[]
					dl_here_2=[]
					for i in range(dest_column-source_column-1):
						r1=r1*best_routes[12][3]
						dl_here_1.append(best_routes[12][4])
					for i in range(source_column + column-dest_column-1):
						r2=r2*best_routes[17][3]
						dl_here_2.append(best_routes[17][4])
					if r1<=r2:
						r=r*r1
						dl_here.append(dl_here_1)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and faulty_routers_column[k] <= dest_column and faulty_routers_column[k] >=source_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[12][3]
									r=r*faulty_routes[k][12][3]
									dl_here.append(faulty_routes[k][12][4])
					else:
						r=r*r2
						dl_here.append(dl_here_2)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_column[k] <= source_column or faulty_routers_column[k] >=dest_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[17][3]
									r=r*faulty_routes[k][17][3]
									dl_here.append(faulty_routes[k][17][4])
			#################---------------24-----------------####################						
			if dest_aisle==source_aisle and dest_column<source_column and dest_row==source_row:
				if (source_column-dest_column) < (dest_column + column-source_column):
					for i in range(source_column-dest_column-1):
						r=r*best_routes[17][3]
						dl_here.append(best_routes[17][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[17][3]
								r=r*faulty_routes[k][17][3]
								dl_here.append(faulty_routes[k][17][4])
				elif (source_column-dest_column) > (dest_column + column-source_column):
					for i in range(dest_column + column-source_column-1):
						r=r*best_routes[12][3]
						dl_here.append(best_routes[12][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[12][3]
								r=r*faulty_routes[k][12][3]
								dl_here.append(faulty_routes[k][12][4])
				else:
					r1=1
					r2=1
					dl_here_1=[]
					dl_here_2=[]
					for i in range(source_column-dest_column-1):
						r1=r1*best_routes[17][3]
						dl_here_1.append(best_routes[17][4])
					for i in range(dest_column + column-source_column-1):
						r2=r2*best_routes[12][3]
						dl_here_2.append(best_routes[12][4])
					if r1<=r2:
						r=r*r1
						dl_here.append(dl_here_1)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and faulty_routers_column[k] <= source_column and faulty_routers_column[k] >=dest_column):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[17][3]
									r=r*faulty_routes[k][17][3]
									dl_here.append(faulty_routes[k][17][4])
					else:
						r=r*r2
						dl_here.append(dl_here_2)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_aisle[k]==dest_aisle and (faulty_routers_column[k] <= dest_column or faulty_routers_column[k] >=source_column)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[12][3]
									r=r*faulty_routes[k][12][3]
									dl_here.append(faulty_routes[k][12][4])
			#################---------------25-----------------####################						
			if dest_aisle>source_aisle and dest_column==source_column and dest_row==source_row:
				if (dest_aisle-source_aisle) < (source_aisle + aisle-dest_aisle):
					for i in range(dest_aisle-source_aisle-1):
						r=r*best_routes[29][3]
						dl_here.append(best_routes[29][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and faulty_routers_aisle[k] <= dest_aisle and faulty_routers_aisle[k] >=source_aisle):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[29][3]
								r=r*faulty_routes[k][29][3]
								dl_here.append(faulty_routes[k][29][4])
				elif (dest_aisle-source_aisle) > (source_aisle + aisle-dest_aisle):
					for i in range(source_aisle + aisle-dest_aisle-1):
						r=r*best_routes[24][3]
						dl_here.append(best_routes[24][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and (faulty_routers_aisle[k] <= source_aisle or faulty_routers_aisle[k] >=dest_aisle)):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[24][3]
								r=r*faulty_routes[k][24][3]
								dl_here.append(faulty_routes[k][24][4])
				else:
					r1=1
					r2=1
					dl_here_1=[]
					dl_here_2=[]
					for i in range(dest_aisle-source_aisle-1):
						r1=r1*best_routes[29][3]
						dl_here_1.append(best_routes[29][4])
					for i in range(source_aisle + aisle-dest_aisle-1):
						r2=r2*best_routes[24][3]
						dl_here_2.append(best_routes[24][4])
					if r1<=r2:
						r=r*r1
						dl_here.append(dl_here_1)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and faulty_routers_aisle[k] <= dest_aisle and faulty_routers_aisle[k] >=source_aisle):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[29][3]
									r=r*faulty_routes[k][29][3]
									dl_here.append(faulty_routes[k][29][4])
					else:
						r=r*r2
						dl_here.append(dl_here_2)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and (faulty_routers_aisle[k] <= source_aisle or faulty_routers_aisle[k] >=dest_aisle)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[24][3]
									r=r*faulty_routes[k][24][3]
									dl_here.append(faulty_routes[k][24][4])
			#################---------------26-----------------####################						
			if dest_aisle<source_aisle and dest_column==source_column and dest_row==source_row:
				if (source_aisle-dest_aisle) < (dest_aisle + aisle-source_aisle):
					for i in range(source_aisle-dest_aisle-1):
						r=r*best_routes[24][3]
						dl_here.append(best_routes[24][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and faulty_routers_aisle[k] <= source_aisle and faulty_routers_aisle[k] >=dest_aisle):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[24][3]
								r=r*faulty_routes[k][24][3]
								dl_here.append(faulty_routes[k][24][4])
				elif (source_aisle-dest_aisle) > (dest_aisle + aisle-source_aisle):
					for i in range(dest_aisle + aisle-source_aisle-1):
						r=r*best_routes[29][3]
						dl_here.append(best_routes[29][4])
					if number_of_faults >0:
						for k in range(faulty_routers_num):
							if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and (faulty_routers_aisle[k] <= dest_aisle or faulty_routers_aisle[k] >=source_aisle)):
								if len(dl_here)>0:
									dl_here.pop()
								r=r/best_routes[29][3]
								r=r*faulty_routes[k][29][3]
								dl_here.append(faulty_routes[k][29][4])
				else:
					r1=1
					r2=1
					dl_here_1=[]
					dl_here_2=[]
					for i in range(source_aisle-dest_aisle-1):
						r1=r1*best_routes[24][3]
						dl_here_1.append(best_routes[24][4])
					for i in range(dest_aisle + aisle-source_aisle-1):
						r2=r2*best_routes[29][3]
						dl_here_2.append(best_routes[29][4])
					if r1<=r2:
						r=r*r1
						dl_here.append(dl_here_1)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and faulty_routers_aisle[k] <= source_aisle and faulty_routers_aisle[k] >=dest_aisle):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[24][3]
									r=r*faulty_routes[k][24][3]
									dl_here.append(faulty_routes[k][24][4])
					else:
						r=r*r2
						dl_here.append(dl_here_2)
						if number_of_faults >0:
							for k in range(faulty_routers_num):
								if (faulty_routers_row[k]==source_row and faulty_routers_column[k]==dest_column and (faulty_routers_aisle[k] <= dest_aisle or faulty_routers_aisle[k] >=source_aisle)):
									if len(dl_here)>0:
										dl_here.pop()
									r=r/best_routes[29][3]
									r=r*faulty_routes[k][29][3]
									dl_here.append(faulty_routes[k][29][4])
			#########################---------------end---------------####################
			traffic_reliability.append(r)
			traffic_data_loss[i]=dl_here

print(traffic_reliability)
print("average:")
print(sum(traffic_reliability)/len(traffic_reliability))

