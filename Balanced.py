import cPickle as pickle
from random import *
def Balanced():
    k = 8       ##number of machines
    filename = 'com-dblp.ungraph'
    order = 'bfs'

    adList = pickle.load(open(filename+'.p','rb'))
    Stream = pickle.load(open(filename+'_'+order+'.p','rb'))
    print type(adList),type(Stream)
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys()),len(Stream)

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
        ##find minSize Machine(s)
        minSizeList = []
        for i in xrange(k):
            if len(minSizeList) == 0:
                minSizeList.append(i)
                minSize = len(Machines[i])
                continue
            if len(Machines[i]) > minSize:
                continue
            elif len(Machines[i]) == minSize:
                minSizeList.append(i)
            elif len(Machines[i]) < minSize:                ##curMachine size is less than all previous machines, clear list, reset minSize
                minSizeList = []
                minSizeList.append(i)
                minSize = len(Machines[i])

        ##Select Machine to put curNode
        if len(minSizeList) == 1:                           ##only one mininum size machine, add to that machine
            curSelectedMach = minSizeList[0]
            Machines[curSelectedMach].add(curNode)
        else:                                               ##More than one machines has minimum size, Randomly pick one
            randInd = randint(0,len(minSizeList)-1)         ##Random pick one if ties
            curSelectedMach = randInd
            Machines[curSelectedMach].add(curNode)
        #print curSelectedMach
        ##Calculate cutEdges
        curNeighbors = adList[curNode]
        del adList[curNode]
        for Neighbor in curNeighbors:
            if Neighbor == curNode:                         ##Skip first node
                continue
            for i in xrange(k):
                if Neighbor in Machines[i] and i != curSelectedMach:     ##Neighbor was in a machine but not same as curNode
                    cutEdges += 1
                else:
                    continue

    print cutEdges


if __name__ == '__main__':
    Balanced()
