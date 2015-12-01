import cPickle as pickle

def Hashing(name, k, order):
    #k = 8       ##number of machines
    filename = name
    #order = 'bfs'
    #order = 'dfs'
    #order = 'rand'
    print "======Hashing Streaming======="
    print "file:",name,"k size: ",k,"order: ",order
    f = file('result/hashing'+filename+str(k)+order+'.txt','w+')
    f.write("==============hashing streaming================\n")
    print >>f, "file:%s,k size:%d,order:%s" % (name,k,order)

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
        ##Use hash to find machine
        ##TODO HASH FUN need to change
        curSelectedMach = (curNode+k/3) % k
        Machines[curSelectedMach].add(curNode)

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
    Hashing()
