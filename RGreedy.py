import cPickle as pickle
from math import *
from random import *

def random_pick_odd(some_list, odds):  
    #print 'random pick'  
    table = [z for x,y in zip(some_list,odds) for z in [x] * y]   
    #print table  
    if len(table) == 0:
        return choice(some_list)
    return choice(table) 

def RGreedy(name, k, order):
    #k = 8       ##number of machines
    filename = name
    #order = 'bfs'
    #order = 'dfs'
    #order = 'rand'
    print "======Random Greedy Streaming======="
    print "file:",name,"k size: ",k,"order: ",order
    f = file('result/RGreedy/'+filename+str(k)+order+'.txt','w+')
    f.write("==============random greedy streaming================\n")
    print >>f, "file:%s,k size:%d,order:%s" % (name,k,order)

    adList = pickle.load(open(filename+'.p','rb'))
    Stream = pickle.load(open(filename+'_'+order+'.p','rb'))
    print type(adList),type(Stream)
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys()),len(Stream)
    print >>f,"total nodes: %d" % len(adList.keys())
    
    print "Partition"
    
    Cap = len(Stream)/k + 1     ##Capacity of each machine
    curSelectedMach = 0         ##init the default selected machine number
    cutEdges = 0                ##number of edges being cut
    Machines = []               ##List of machines
    Machine = set()             ##Single machine
    for i in xrange(k):         ##init k sets
        Machine = set()         ##Single machine
        Machines.append(Machine)
        
    for curNode in Stream:
        ##find the machine that has most v's neighbor
        curNeighbors = adList[curNode]
        del adList[curNode]
        mostEdgeMach = [0]*k 
        for Neighbor in curNeighbors:
            if Neighbor == curNode:         ##Skip first node
                continue
            for i in xrange(k):
                if Neighbor in Machines[i]:  
                    mostEdgeMach[i] += 1
                else:
                    continue
                
        ##Penalize larger partitions
        ##3 different ways to penalize
        normalConstant = 0;
        for i in xrange(len(mostEdgeMach)):
            #mostEdgeMach[i] = mostEdgeMach[i]
            mostEdgeMach[i] = mostEdgeMach[i] * (1 - (len(Machines[i]))/Cap)
            normalConstant += mostEdgeMach[i]
            ##TODO FIX EXP
            #mostEdgeMach[i] = mostEdgeMach[i] * (1 - exp(len(Machines[i])-Cap))
        
        ##Choose Machine by probability
        candidate_List = [i for i in xrange(k)]
        curSelectedMach = random_pick_odd(candidate_List,mostEdgeMach)
        Machines[curSelectedMach].add(curNode)
        
        ##Calculate cutEdges
        for Neighbor in curNeighbors:
            if Neighbor == curNode:          ##Skip first node
                continue
            for i in xrange(k):
                if Neighbor in Machines[i] and i != curSelectedMach:    ##Neighbor was in a machine but not same as curNode
                    cutEdges += 1
                else:
                    continue
                
    print cutEdges
    print >>f,"cut edges num: %d" % cutEdges
    total = 0
    for i in xrange(k):
        total += len(Machines[i])
        print i,len(Machines[i])
        print >>f,"%d, %d" % (i,len(Machines[i]))
    print >>f,"total node: %d" % total
    print total
    return cutEdges

    f.close()
    
if __name__ == '__main__':
    RGreedy()
        
        
