import cPickle as pickle
from math import *
def DGreedy():
    k = 8       ##number of machines
    filename = 'com-dblp.ungraph'
    order = 'bfs'

    adList = pickle.load(open(filename+'.p','rb'))
    Stream = pickle.load(open(filename+'_'+order+'.p','rb'))
    print type(adList),type(Stream)
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys()),len(Stream)

    print "Partition"

    Cap = len(Stream)/k + 1 ##Capacity of each machine
    curSelectedMach = 0     ##init the default selected machine number
    cutEdges = 0            ##number of edges being cut
    Machines = []           ##List of machines
    Machine = set()         ##Single machine
    for i in xrange(k):             ##init k sets
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
        for i in xrange(len(mostEdgeMach)):
            #mostEdgeMach[i] = mostEdgeMach[i]
            mostEdgeMach[i] = mostEdgeMach[i] * (1 - (len(Machines[i]))/Cap)
            ##TODO FIX EXP
            #mostEdgeMach[i] = mostEdgeMach[i] * (1 - exp(len(Machines[i])-Cap))

        #Argmax
        candidateMachList = [i for i,j in enumerate(mostEdgeMach) if j == max(mostEdgeMach)]
        if len(candidateMachList) == 1:           ##only one maximum edge machine, add to that machine
            Machines[candidateMachList[0]].add(curNode)
        ##TODO Random pick and change curSelectedMach 
        else:                               ##More than one machines has maximum edge, Randomly pick one
            Machines[candidateMachList[0]].add(curNode)
        curSelectedMach = candidateMachList[0]
        #print curSelectedMach

        ##Calculate cutEdges
        #curNeighbors = adList[curNode]
        #del adList[curNode]
        for Neighbor in curNeighbors:
            if Neighbor == curNode:          ##Skip first node
                continue
            for i in xrange(k):
                if Neighbor in Machines[i] and i != curSelectedMach:     ##Neighbor was in a machine but not same as curNode
                    cutEdges += 1
                else:
                    continue

    print cutEdges


if __name__ == '__main__':
    DGreedy()
