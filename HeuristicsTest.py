# Filename: HeuristicsTest.py

import txt2p
import rand
import dfs
import bfs
import Balanced
import Chunking
import DGreedy
import Hashing
import RGreedy
import Triangles

def test():
    datasetfile = ['com-dblp.ungraph', 'Email-Enron', 'facebook_combined']
    order = ['bfs', 'dfs', 'rand']
    ksize = [4,8,12]
    ba,ch,dg,ha,rg,tr=[],[],[],[],[],[]
    Edges_constant = [1049866,367662,88234]  #edges of each datasets
    #for dataname in datasetfile:
        #txt2p.txt2p(dataname)
        #rand.Rand(dataname)
        #dfs.dfs(dataname)
        #bfs.bfs(dataname)
    for dataname in datasetfile:
        for od in order:
            for k in ksize:
                ba.append(Balanced.Balanced(dataname, k, od))
                ch.append(Chunking.Chunking(dataname, k, od))
                dg.append(DGreedy.DGreedy(dataname, k, od))
                ha.append(Hashing.Hashing(dataname, k, od))
                rg.append(RGreedy.RGreedy(dataname, k, od))
                tr.append(Triangles.Triangles(dataname, k, od))
                
    print 'ba',ba
    print 'ch',ch
    print 'dg',dg
    print 'ha',ha
    print 'rg',rg
    print 'tr',tr
    
if __name__ == '__main__':
    test()


