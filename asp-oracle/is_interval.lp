uedge(X,Y) :- edge(X,Y).
uedge(X,Y) :- edge(Y,X).

%isK15(C,X,Y,Z,T,W) :- uedge(C,X), uedge(C,Y), uedge(C,Z), uedge(C,T), uedge(C,W), X < Y, Y < Z, Z < T, T < W, not uedge(X,Y), not uedge(X,Z), not uedge(X,T), not uedge(X,W), not uedge(Y,Z), not uedge(Y,T), not uedge(Y,W), not uedge(Z,T), not uedge(Z,W), not uedge(T,W).
:- uedge(C,X), uedge(C,Y), uedge(C,Z), uedge(C,T), uedge(C,W), X < Y, Y < Z, Z < T, T < W, not uedge(X,Y), not uedge(X,Z), not uedge(X,T), not uedge(X,W), not uedge(Y,Z), not uedge(Y,T), not uedge(Y,W), not uedge(Z,T), not uedge(Z,W), not uedge(T,W).
%isC4(X,Y,Z,T) :- uedge(X,Y), uedge(Y,Z), uedge(Z,T), uedge(T,X), not uedge(X,Z), not uedge(Y,T), X < Y, X < Z, X < T, Y != Z, Y !=T, Z != T.
:- uedge(X,Y), uedge(Y,Z), uedge(Z,T), uedge(T,X), not uedge(X,Z), not uedge(Y,T), X < Y, X < Z, X < T, Y != Z, Y !=T, Z != T.
1 { coedge(X,Y); coedge(Y,X) } 1 :- vertex(X), vertex(Y), X < Y, not uedge(X,Y).
:- coedge(X,Y), coedge(Y,Z), not coedge(X,Z).
