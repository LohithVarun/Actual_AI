bird(eagle).
bird(penguin).
bird(ostrich).
bird(sparrow).
bird(pigeon).

flightless_bird(penguin).
flightless_bird(ostrich).

can_fly(Bird) :- 
  bird(Bird),
  \+ flightless_bird(Bird).

cannot_fly(Bird) :-
  bird(Bird),
  flightless_bird(Bird).
