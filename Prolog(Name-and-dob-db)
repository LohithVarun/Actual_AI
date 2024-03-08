person('Alice', '1980-01-01').
person('Bob', '1990-02-14').
person('Charlie', '2000-03-03').

find_person(Name, DOB) :-
  person(Name, DOB).

list_all_people :-
  findall(Name, person(Name, _), Names),
  format('List of all people: ~w\n', [Names]).
