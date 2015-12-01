import cPickle as pickle
from random import *
def Rand(name):
    filename = name

    adList = pickle.load(open(filename+'.p','rb'))
    print type(adList)#,adlis.readline()
    print adList[3],adList[35]
    print "total nodes:",len(adList.keys())

    print "Random"
    #random
    randOrder = []       #result
    randOrder = adList.keys()
    shuffle(randOrder)
    print len(randOrder)    ##test
    print randOrder[0:10]
    pickle.dump(randOrder,open(filename+'_rand'+'.p','wb'))


if __name__ == '__main__':
   Rand()
