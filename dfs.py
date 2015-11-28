import cPickle as pickle

def dfs():
    filename = 'com-dblp.ungraph'

    adList = pickle.load(open(filename+'.p','rb'))
    print type(adList)#,adlis.readline()
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys())

    print "dfsing"
    #dfs
    curNode = 0         #first node
    st = []
    st.append(curNode)
    dfsOrder = []       #result
    visited = set()
    while st:
        curNode = st.pop()           ##pop
        if curNode not in visited:
            dfsOrder.append(curNode)    ##output to dfsOrder
            visited.add(curNode)
        else:
            pass
        if curNode not in adList:       ##may have no neighbors   NOT NECESSARY
            pass
        else:
            curNeighbor = adList[curNode]   ##all neighbors
            del adList[curNode]             ##delete from adList
            for i in curNeighbor:           ##push all neighbors
                if i in adList:
                    st.append(i)

    print len(dfsOrder),len(visited)    ##test
    print dfsOrder[0:10]
    pickle.dump(dfsOrder,open(filename+'_dfs'+'.p','wb'))


if __name__ == '__main__':
    dfs()
