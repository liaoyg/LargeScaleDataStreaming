import numpy as np
import cPickle as pickle
from collections import deque

def main():
    filename = 'com-dblp.ungraph'
    #open file
    fr = open((filename+".txt"))

    offset = 4
    
    #total number of examples
    line_num = len(fr.readlines())- offset 
    print line_num

    fr.seek(0, 0)  
    # disgard the header  
    for i in range(offset):
        header = fr.readline()
    

    node = []
    adlist = dict()
    i=0
    total_node = set()
    for line in fr.readlines():
        edge = line.strip().split()
        if edge[0] not in total_node:
            total_node.add(edge[0])
        if edge[1] not in total_node:
            total_node.add(edge[1])
        if node == []:
            node.append(int(edge[0]))
            node.append(int(edge[1]))
        elif int(edge[0]) == node[0]:
            node.append(int(edge[1]))
        else:
            #adlist.add(node)
            #print node
            key = (node[0])
            adlist[key] = node
            node = []
            node.append(int(edge[0]))
            node.append(int(edge[1]))
            i+=1
    edges = 0
    for j in adlist.keys():
        edges += len(adlist[j])-1
    print "total nodes:", i,len(total_node),len(adlist.keys())
    print "total edges:",edges
    pickle.dump(adlist,open(filename+'.p','wb'))

    adlist = pickle.load(open(filename+'.p','rb'))
    print type(adlist)#,adlis.readline()
    print adlist[3],adlist[35]
    print len(adlist.keys())


    #bfs
    q = deque()
    curNode = 0
    q.append(curNode)
    bfsQueue = []
    visited = set()
    while q:
        curNode = q.popleft()       ##dequeue
        if curNode not in visited:
            bfsQueue.append(curNode)    ##enqueue
            visited.add(curNode)
        else:
            pass
        if curNode not in adlist:   ##may have no neighbors
            pass
        else:
            curList = adlist[curNode]   ##all neighbors
            del adlist[curNode]         
            for i in curList:
                if i in adlist:
                    q.append(i)

    print len(bfsQueue),len(visited)#,bfsQueue
    

if __name__ == '__main__':
    main()
