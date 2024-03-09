planet(mercury, 4.87, 0.39).
planet(venus, 4.2, 0.72).
planet(earth, 5.97, 1.00).
planet(mars, 0.642, 1.52).

planet_info(Name, Mass, Distance) :-
  planet(Name, Mass, Distance).
