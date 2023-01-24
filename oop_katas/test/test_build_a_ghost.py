from oop_katas.src.build_a_ghost import Ghost, Blinky, Pinky, Inky, Clyde

ghost = Ghost('Ducky', 3, 'yellow')
blinky = Blinky('Blinky', 3,'red')
pinky = Pinky('pinky', 2,'pink')
inky = Inky('inky', 4,'cyan')
clyde = Clyde('Clyde', 1,'cyan')


def test_contains_name_speed_colour_properties():
    assert ghost.name == 'Ducky'
    assert ghost.speed == 3
    assert ghost.colour == 'yellow'

def test_is_scared_default_is_false():
    assert ghost.is_scared == False

def test_can_be_eaten_if_scared_is_false():
    assert ghost.is_scared == ghost.can_be_eaten()

def test_frighten_method_colour_is_blue_if_is_scared_true():
    ghost.frighten()
    assert ghost.colour == 'blue'
    assert ghost.is_scared == True
    assert ghost.can_be_eaten() == True

def test_increases_speed_by_10_percent():
    ghost.speed_up()
    assert ghost.speed == 3.3
    ghost.speed_up()
    assert ghost.speed == 3.63

def test_pinky_new_ghost():
    assert pinky.colour == 'pink'
    pinky.frighten()
    assert pinky.colour == 'blue'
    assert pinky.is_scared == True
    assert pinky.can_be_eaten() == True
    assert pinky.name == 'pinky'
    assert pinky.speed == 2
    pinky.speed_up()
    assert pinky.speed == 2.2






    






   
       


  
  
