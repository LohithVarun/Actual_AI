sum(0, 0).
sum(N, R) :-
  N1 is N - 1,
  sum(N1, R1),
  R is R1 + N.
