pedge( 1, 2).
pedge( 1, 3).
pedge( 1, 4).
pedge( 1, 5).
pedge( 1, 6).
pedge( 1, 7).
pedge( 1, 8).
%pedge( 1, 9).
pedge( 1,10).
%%%pedge( 2, 3). %
pedge( 2, 4).
pedge( 2, 5).
pedge( 2, 6).
%%%pedge( 2, 7). %
pedge( 2, 8).
%pedge( 2, 9). %
pedge( 4, 5).
pedge( 4, 6).
pedge( 4, 7).
pedge( 4, 8).
%%pedge( 4, 9).
pedge( 4,10).
pedge( 4,11).
pedge( 4,12).
pedge( 4,13).
pedge( 5, 6).
pedge( 5, 7).
pedge( 5, 8).
%pedge( 5, 9).
pedge( 5,10).
pedge( 5,11).
pedge( 5,12).
%%pedge( 8, 9).
pedge( 8,10).
pedge( 8,11).
pedge( 8,12).
pedge( 8,13).
pedge( 8,14).
%%pedge( 9,10).
%pedge( 9,11).
pedge( 9,12).
%%pedge( 9,13).
pedge(10,11).
pedge(10,12).
pedge(12,13).
pedge(12,14).
edge(U,V) :- pedge(U,V), vertex(U), vertex(V), U < V.
edge(V,U) :- pedge(U,V), vertex(U), vertex(V), U > V.
vertex(1..N) :- nbVertices(N).
nbVertices(14).
%edge(U,V) :- pedge(U,V), vertex(U), vertex(V), U < V, not bad(U,V).
%edge(V,U) :- pedge(U,V), vertex(U), vertex(V), U > V, not bad(U,V).
%5 { bad(U,V) : pedge(U,V) } 5. #show bad/2.
