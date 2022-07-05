import networkx as nx
import sys
import random
import os
import time

import oracle

#http://www.jaist.ac.jp/~uehara/graphs/

if len(sys.argv) < 2:
    print("Usage python3 script fileWithIntervalGraphs")
    sys.exit()

#f = open("interval_disconnected_9.txt", "r")

def has5Claw(G):
    #is there a 5-clique in the complement of the neighborood
    for n in G.nodes():
        neib = list(G[n])
        compl = nx.complement(G.subgraph(neib))
        for clique in nx.enumerate_all_cliques(compl):
            if len(clique) > 4:
                #print clique
                print(n, " creates claw", clique)
                return True
    return False

def has4Claw(G):
    #is there a 5-clique in the complement of the neighborood
    for n in G.nodes():
        neib = list(G[n])
        compl = nx.complement(G.subgraph(neib))
        for clique in nx.enumerate_all_cliques(compl):
            if len(clique) > 3:
                #print clique
                print(n, " creates claw", clique)
                return True
    return False

def generateClingoGraph(G):
    s = ""
    for (u,v) in G.edges():
        s += "pedge(" + u + ", " + v + "). \n"
    s += "edge(U,V) :- pedge(U,V), vertex(U), vertex(V), U < V.\n"
    s += "edge(V,U) :- pedge(U,V), vertex(U), vertex(V), U > V.\n"
    s += "vertex(1..N) :- nbVertices(N).\n"
    s += "nbVertices(" + str(len(G.nodes())) + ").\n"
    #print(s)
    return s

def doit():
    graphfile = sys.argv[1]
    lines = graphfile+".tries"
    startat=0


    try:
        linefile = open(lines,'r')
        startat = int(linefile.read())
        linefile.close()
        linefile = open(lines,"w")

    except IOError:
        linefile = open(lines,"w")


    linefile.write(str(startat))
    linefile.close()


    f = open(graphfile, "r")

    startTime = time.time()
    nbTested=1
    lnb = -1
    for l in f:
        lnb += 1
        #if lnb >= 100:
        #    print(time.time() - startTime)
        #    assert(False)
        #to start from where we were...
        if lnb < startat:
            continue
        #store where we were every 200 graphs
        if lnb % 200 == 0:
            with open(lines, 'w') as lf:
                lf.write(str(lnb))

        arr = l.split()

        pos = {}
        i = 0
        for a in arr:
            if a in pos:
                pos[a] = (pos[a],i)
            else:
                pos[a] = i
            i += 1

        G = nx.Graph()

        #vertex <-> pair of i in the array
        #edge uv <-> u and v are interleaved

        for i in pos:
            first,second = pos[i][0], pos[i][1]
            for j in range(first+1,second):
                G.add_edge(i,arr[j])

        print("NB {:5} line {:5} initial array {}".format(nbTested, lnb, arr), end=' ')
        nbTested+=1

        #G2 = nx.Graph()


        if not has5Claw(G) and len(G.edges())>0:
        #if not has4Claw(G) and len(G.edges())>0:
            #print("WILL SOLVE !", G.edges())
            #if not solve(G):

            graph = generateClingoGraph(G)
            edges = oracle.computeSchedule(graph)
            if edges == False:
                print(graph)
                print(False)
                candidates = open(graphfile+".candidates", "a")
                candidates.write(l)
                candidates.close()
                #assert(False)

            else:
                pass
                print(True)
                #print(edges)
            #assert(False)
        else:
            print("has a 5 claw, continue")
        



doit()
