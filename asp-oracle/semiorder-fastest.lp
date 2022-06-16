track(1..2).
%Theorem 2.9 (Scott and Suppes [SS58]) A partial order relation S defined on V is a semiorder
%if the following conditions hold:
%1. S is irreflexive.
%2. (x, y) ∈ S and (z, w) ∈ S imply (x, w) ∈ S or (z, y) ∈ S.
%3. (x, y) ∈ S and (y, z) ∈ S imply (x, w) ∈ S or (w, z) ∈ S.
:- tsemiorder(T,X,Y), tsemiorder(T,Y,Z), not tsemiorder(T,X,Z).
:- tsemiorder(T,X,Y), tsemiorder(T,Y,X).
%:- tsemiorder(T,X,Y), tsemiorder(T,Z,W), not tsemiorder(T,X,W), not tsemiorder(T,Z,Y).%, X <= Z.
twotwoAux(T,Y,W) :- tsemiorder(T,X,Y), vertex(W), not tsemiorder(T,X,W).
:- twotwoAux(T,Y,W), twotwoAux(T,W,Y), Y < W.
%:- tsemiorder(T,X,Y), tsemiorder(T,Y,Z), vertex(W), not tsemiorder(T,X,W), not tsemiorder(T,W,Z).
threeoneAux(T,X,Z) :- vertex(X), vertex(W), vertex(Z), track(T), not tsemiorder(T,X,W), not tsemiorder(T,W,Z).
:- threeoneAux(T,X,Z), tsemiorder(T,X,Y), tsemiorder(T,Y,Z).

% Theorem 2.8 (Roberts [Rob69])
% There is a semiorder on S(V, P ) on the vertices of V such that (u, w) ∈ P ⇔ (u, w) not ∈ E(G).
% iff G is a unit interval graph.
{ tsemiorder(T,X,Y); tsemiorder(T,Y,X) } :- vertex(X), vertex(Y), X < Y, track(T).
:- ttheedge(T,X,Y), tsemiorder(T,X,Y).
:- ttheedge(T,X,Y), tsemiorder(T,Y,X).
:- vertex(X), vertex(Y), X < Y, track(T), not tsemiorder(T,X,Y), not tsemiorder(T,Y,X), not ttheedge(T,X,Y).


%1 { ttheedge(T,U,V) : track(T) } :- edge(U,V).
{ ttheedge(T,U,V) } :- vertex(U), vertex(V), U<V, track(T).
:- edge(U,V), not ttheedge(1,U,V), not ttheedge(2,U,V).
:- not edge(U,V), ttheedge(T,U,V).


semiorder(x(U),x(V)) :- tsemiorder(1,U,V).
semiorder(y(U),y(V)) :- tsemiorder(2,U,V).
theedge(x(U),x(V)) :- ttheedge(1,U,V).
theedge(y(U),y(V)) :- ttheedge(2,U,V).

:- edge(U,V), V <= U.


%#show.
%#show theedge/2.
%#show element/1.
%#show semiorder/2.
%#show theedge(U,V) : theedge(U,V), U<V.
