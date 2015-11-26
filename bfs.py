import cPickle as pickle
from collections import deque

def bfs():
    filename = 'com-dblp.ungraph'

    adlist = pickle.load(open(filename+'.p','rb'))
    print type(adlist)#,adlis.readline()
    print adlist[3],adlist[35]
    print "total nodes:",len(adlist.keys())

    print "bfsing"
    #bfs
    q = deque()         #init
    curNode = 0         #first node
    q.append(curNode)
    bfsOrder = []       #result
    visited = set()
    while q:
        curNode = q.popleft()           ##dequeue
        if curNode not in visited:
            bfsOrder.append(curNode)    ##output to bfsOrder
            visited.add(curNode)
        else:
            pass
        if curNode not in adlist:       ##may have no neighbors   NOT NECESSARY
            pass
        else:
            curNeighbor = adlist[curNode]   ##all neighbors
            del adlist[curNode]             ##delete from adlist
            for i in curNeighbor:           ##enqueue all neighbors
                if i in adlist:
                    q.append(i)

    print len(bfsOrder),len(visited)    ##test
    pickle.dump(bfsOrder,open(filename+'_bfs'+'.p','wb'))


if __name__ == '__main__':
    bfs()
