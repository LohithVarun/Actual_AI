male(john).
male(peter).
male(michael).
female(mary).
female(sarah).
female(anne).

parent(john, mary).
parent(john, peter).
parent(mary, sarah).
parent(mary, anne).
parent(peter, michael).

child(Child, Parent) :-
  parent(Parent, Child).

parent_of(Parent, Child) :-
  child(Child, Parent).

sibling(X, Y) :-
  parent(Z, X),
  parent(Z, Y),
  X \= Y.
