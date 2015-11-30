import cPickle as pickle

def Chunking():
    k = 8       ##number of machines
    filename = 'com-dblp.ungraph'
    order = 'bfs'
    #order = 'dfs'
    #order = 'rand'

    adList = pickle.load(open(filename+'.p','rb'))
    Stream = pickle.load(open(filename+'_'+order+'.p','rb'))
    print type(adList),type(Stream)
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys()),len(Stream)

    print "Partition"

    Cap = len(Stream)/k + 1     ##Capacity of each machine
    curCap = 0
    curSelectedMach = 0         ##init the default selected machine number
    cutEdges = 0                ##number of edges being cut
    Machines = []               ##List of machines
    Machine = set()             ##Single machine
    for i in xrange(k):         ##init k sets
        Machine = set()         ##Single machine
        Machines.append(Machine)


    for curNode in Stream:
        ##find the machine to put curNode
        if curCap < Cap:
            curCap += 1
        else:
            curCap = 0
            curSelectedMach = (curSelectedMach + 1) % k

        Machines[curSelectedMach].add(curNode)

        #print curSelectedMach
        ##Calculate cutEdges
        curNeighbors = adList[curNode]
        del adList[curNode]
        for Neighbor in curNeighbors:
            if Neighbor == curNode:          ##Skip first node
                continue
            for i in xrange(k):
                if Neighbor in Machines[i] and i != curSelectedMach:     ##Neighbor was in a machine but not same as curNode
                    cutEdges += 1
                else:
                    continue

    print cutEdges
    total = 0
    for i in xrange(k):
        total += len(Machines[i])
        print i,len(Machines[i])
    print total


if __name__ == '__main__':
    Chunking()
