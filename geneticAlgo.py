#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import csv
import numpy as np
import time
import randPaths
import genes

np.random.seed(0)
#Set here: number of iteration, childs(in one iteration), and possibility of mutation in percent:
ITERATION = 20
CHILDS = 100
MUT = 10
#Batch: 64 --- 7.6837475299835205 seconds ---
#Batch: 128 --- 44.893614530563354 seconds ---
#Batch: 256 --- 220.8189458847046 seconds ---
#Batch: 512 --- 1043.4989852905273 seconds ---
#Batch: 1024 --- 5940.745468378067 seconds ---

GRAPH = [[]]
NODES=0

file_num = 1024

with open(str(file_num)+'_data.csv', "rt") as f:
    reader = csv.reader(f)
    for line in reader:
    	for x in range(len(line)):
    		GRAPH[NODES].append(int(line[x]))
    	if(NODES>0):
    		GRAPH[NODES].remove(NODES)
    	NODES += 1
    	GRAPH.append([NODES])
GRAPH.pop()

start_time = time.time()

for xx in range(0, 3):
	start_time_small = time.time()
	rand_list = np.random.randint(0, NODES, 2)

	startCity = int(rand_list[0])
	print(startCity)
	stopCity = int(rand_list[1])
	print(stopCity)

	paths = randPaths.randPaths(GRAPH, NODES, startCity, stopCity)
	firstParent = paths.makeRoute()
	secondParent = paths.makeRoute()

	gen = genes.Genes(GRAPH, ITERATION, NODES, CHILDS, MUT, startCity, stopCity, firstParent, secondParent)
	gen.makeRoute()

	firstPath = gen.returnBestRoute()
	print()
	print('Best route: ' + str(firstPath))
	print("--- %s seconds ---" % (time.time() - start_time_small))

print("Batch: "+str(file_num)+" --- %s seconds ---" % (time.time() - start_time))