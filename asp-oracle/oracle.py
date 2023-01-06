import clingo
import clingo.ast


def storeModel(model,output):
    l = model.symbols(atoms=True)
    for atom in l:
        if atom.name == "theedge":
            assert(len(atom.arguments) == 2)
            eu = atom.arguments[0]
            ev = atom.arguments[1]
            output.append((str(eu),str(ev)))

#with open("semiorder-f.lp",'r') as f:
#with open("semiorder-faster.lp",'r') as f:
#2-tracks
#with open("semiorder-fastest.lp",'r') as f:

#2unit
with open("semiorder-f.lp",'r') as f:
    storedConstraints = f.read()
def collectDefaultConstraints():
#    with open("semiorder.lp",'r') as f:
#        total = f.read()
    total = storedConstraints
    return total

def computeSchedule(graph):
    ctl = clingo.Control()
    with clingo.ast.ProgramBuilder(ctl) as bld:
        clingo.ast.parse_string(graph, bld.add)
        clingo.ast.parse_string(collectDefaultConstraints(), bld.add) # parse from string

    ctl.ground([('base', [])])
    #output = defaultdict(lambda: defaultdict(list))
    output = []
    #print(ctl.solve(on_model=print))
    result = ctl.solve(on_model=lambda m: storeModel(m, output))
    if result.satisfiable:
#        print(output)
        return output
#        print(output)
#        pass
    elif result.satisfiable is False:
#        print(False)
        return False
    else:
        print("???")
        assert False

if __name__ == "__main__":
    g = """pedge( 1, 2). pedge( 1, 3). pedge( 1, 4). pedge( 1, 7). pedge( 1, 8). pedge( 1,10). pedge(1,13). pedge(1,19). % 8
pedge( 2, 5). pedge( 2, 6). pedge( 2, 7). pedge( 2, 8). pedge( 2,13). pedge( 2,14). pedge(2,15). pedge(2,17). pedge(2,19). % 9
pedge( 3, 8). pedge( 3,10). pedge( 3,13). pedge( 3,14). pedge( 3,19). % 5
pedge( 4, 9). pedge( 4,10). pedge( 4,11). pedge( 4,12). pedge( 4,14). pedge( 4,19). pedge(4,20). % 7
pedge( 5,17). pedge( 5,13). pedge( 5,15). % 3
pedge( 6, 8). pedge( 6,13). pedge( 6,15). pedge( 6,17). % 4
pedge( 7, 8). pedge( 7,13) .pedge( 7,15). pedge( 7,19). % 4
pedge( 8,10). pedge( 8,13). pedge( 8,14). pedge( 8,15). pedge( 8,17). pedge( 8,19). % 6
pedge( 9,10). pedge( 9,19). % 2
pedge(10,11). pedge(10,12). pedge(10,13). pedge(10,14). pedge(10,19). pedge(10,20). % 6
pedge(11,14). pedge(11,19). % 2
pedge(12,20). % 1
pedge(13,14). pedge(13,15). pedge(13,19). %3
pedge(14,19). % 1
pedge(15,16). pedge(15,17). pedge(15,19). % 3
pedge(16,17). pedge(17,18). % 2
pedge(20,21). pedge(20,22). pedge(20,23). % 3

edge(U,V) :- pedge(U,V), vertex(U), vertex(V), U < V.
edge(V,U) :- pedge(U,V), vertex(U), vertex(V), U > V.

pvertex(1..N) :- nbVertices(N).
vertex(V) :- pvertex(V), V < 18, V != 3, V!=4, V!=8.
%vertex(V) :- pvertex(V), V < 17, V!=3.
%actualVertices(C) :- C = #count { V : vertex(V) }.
%:- actualVertices(C), C < 23.

cliqueNumber(5) :- nbVertices(N), N <= 18.
cliqueNumber(6) :- nbVertices(N), N > 18.

nbVertices(23).
"""
    computeSchedule(g)
