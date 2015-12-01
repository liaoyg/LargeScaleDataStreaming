# Filename: txt2p.py
import cPickle as pickle
from collections import deque

def txt2p(name):
    filename = name
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
    adList = dict()
    total_node = set()
    for line in fr.readlines():
        edge = line.strip().split()
        if edge[0] not in total_node:   ##first appearance
            total_node.add(edge[0])
            key = int(edge[0])
            adList[key] = []
            adList[key].append(int(edge[0]))
            adList[key].append(int(edge[1]))
        else:#if edge[1] not in total_node:
            key = int(edge[0])
            if int(edge[1]) not in adList[key]:
                adList[key].append(int(edge[1]))  

        if edge[1] not in total_node:   ##first appearance
            total_node.add(edge[1])
            key = int(edge[1])
            adList[key] = []
            adList[key].append(int(edge[1]))
            adList[key].append(int(edge[0]))
        else:#if edge[0] not in total_node:
            key = int(edge[1])
            if int(edge[0]) not in adList[key]:
                adList[key].append(int(edge[0]))  


    edges = 0
    for j in adList.keys():
        edges += (len(adList[j])-1)
    print "total nodes:", len(total_node),len(adList.keys())
    print "total edges:",edges/2
    pickle.dump(adList,open(filename+'.p','wb'))
    

if __name__ == '__main__':
    txt2p()
