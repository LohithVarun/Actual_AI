fruit(apple, red).
fruit(apple, green).
fruit(banana, yellow).
fruit(orange, orange).

fruit_color(Fruit, Color) :-
  fruit(Fruit, Color).

colored_fruits(Color, Fruits) :-
  findall(Fruit, (fruit(Fruit, Color)), Fruits).
