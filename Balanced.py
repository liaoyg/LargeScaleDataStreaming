import cPickle as pickle
from collections import deque

def Balanced():
    k = 8       ##number of machines
    filename = 'com-dblp.ungraph'
    order = 'bfs'

    adlist = pickle.load(open(filename+'.p','rb'))
    Stream = pickle.load(open(filename+'_'+order+'.p','rb'))
    print type(adlist),type(Stream)
    print adlist[3],adlist[35]
    print "total nodes:",len(adlist.keys()),len(Stream)

    print "Partition"

    Cap = len(Stream)/k     ##Capacity of each machine
    




if __name__ == '__main__':
    Balanced()
