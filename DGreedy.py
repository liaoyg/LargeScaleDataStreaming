import cPickle as pickle
from math import *
from random import *
def DGreedy(name, k, order):
    #k = 8       ##number of machines
    filename = name
    #order = 'bfs'
    #order = 'dfs'
    #order = 'rand'

    print "======Deterministic Greedy Streaming======="
    print "file:",name,"k size: ",k,"order: ",order
    f = file('result/DGreedy/'+filename+str(k)+order+'.txt','w+')
    f.write("==============determinisitic_greedy streaming================\n")
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
        mostEdgeMach = [0]*k                ##How may neighbors in each machine
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
        for i in xrange(len(mostEdgeMach)):
            #mostEdgeMach[i] = mostEdgeMach[i]
            mostEdgeMach[i] = mostEdgeMach[i] * (1 - (len(Machines[i]))/Cap)
            ##TODO FIX EXP
            #mostEdgeMach[i] = mostEdgeMach[i] * (1 - exp(len(Machines[i])-Cap))

        #Argmax
        candidateMachList = [i for i,j in enumerate(mostEdgeMach) if j == max(mostEdgeMach)]
        if len(candidateMachList) == 1:                                 ##only one maximum edge machine, add to that machine
            curSelectedMach = candidateMachList[0]
            Machines[curSelectedMach].add(curNode)
        else:                                                           ##More than one machines has maximum edge, Randomly pick one
            randInd = randint(0,len(candidateMachList)-1)               ##Random pick one if ties
            curSelectedMach = randInd
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
    DGreedy()
