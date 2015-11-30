import cPickle as pickle
from collections import deque

def bfs():
    filename = 'Email-Enron'

    adList = pickle.load(open(filename+'.p','rb'))
    print type(adList)#,adlis.readline()
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys())

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
        if curNode not in adList:       ##may have no neighbors   NOT NECESSARY
            pass
        else:
            curNeighbor = adList[curNode]   ##all neighbors
            del adList[curNode]             ##delete from adList
            for i in curNeighbor:           ##enqueue all neighbors
                if i in adList:
                    q.append(i)
        if len(q) == 0:
            if len(adList.keys()) != 0:
                key = adList.keys()
                q.append(key[0])

    print len(bfsOrder),len(visited)    ##test
    pickle.dump(bfsOrder,open(filename+'_bfs'+'.p','wb'))


if __name__ == '__main__':
    bfs()
