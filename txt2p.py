import numpy as np
import cPickle as pickle
from collections import deque

def txt2p():
    filename = 'com-dblp.ungraph'
    #open file
    fr = open((filename+".txt"))

    offset = 4
    
    #total number of edges
    line_num = len(fr.readlines())- offset 
    print line_num

    fr.seek(0, 0)  
    # disgard the header  
    for i in range(offset):
        header = fr.readline()
    
    print "loading"
    adlist = dict()
    total_node = set()
    for line in fr.readlines():
        edge = line.strip().split()
        if edge[0] not in total_node:   ##first appearance
            total_node.add(edge[0])
            key = int(edge[0])
            adlist[key] = []
            adlist[key].append(int(edge[0]))
            adlist[key].append(int(edge[1]))
        else:
            key = int(edge[0])
            adlist[key].append(int(edge[1]))  

        if edge[1] not in total_node:   ##first appearance
            total_node.add(edge[1])
            key = int(edge[1])
            adlist[key] = []
            adlist[key].append(int(edge[1]))
            adlist[key].append(int(edge[0]))
        else:
            key = int(edge[1])
            adlist[key].append(int(edge[0]))  


    edges = 0
    for j in adlist.keys():
        edges += (len(adlist[j])-1)
    print "total nodes:", len(total_node),len(adlist.keys())
    print "total edges:",edges
    pickle.dump(adlist,open(filename+'.p','wb'))
    

if __name__ == '__main__':
    txt2p()
