loc(left).
loc(center).
loc(right).

move(1, From, To, _) :-
  write('Move disk from '), 
  write(From), 
  write(' to '), 
  write(To), 
  nl.

move(N, From, To, Aux) :-
  N > 1,
  M is N - 1,

  move(M, From, Aux, To),

  move(1, From, To, _),

  move(M, Aux, To, From).

hanoi(N) :-
  move(N,left,right,center).
