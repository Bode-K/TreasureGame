from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

sense.show_message("Level 1")
# Just return the actions we are interested in
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

R = [255, 0, 0]  # red
Y = [255, 255, 0] # yellow
G = [0, 255, 0] # green
W = [255, 255, 255] # white

score = 0


for turns in range(5):

  coinx = randint(0,7)
  coiny = randint(0,7)
  print(coinx, coiny)

  sense.set_pixel(coinx, coiny, Y)
  sleep(2)
  sense.clear()


  x = randint(0,7)
  y = randint(0,7)
  sense.set_pixel(x, y, W)

  while True:
  
    e = wait_for_move()
    
    if e.direction == DIRECTION_MIDDLE:

        if x == coinx and y == coiny:
            sense.set_pixel(x, y, G)
            score += 1



        else:
            sense.set_pixel(x, y, R)

             
      
        sleep(1.25)
        sense.clear()
        sleep(0.5)


        break;


             
    sense.clear()
    if e.direction == DIRECTION_UP and y > 0:
        y = y - 1
    elif e.direction == DIRECTION_DOWN and y < 7:
        y = y + 1
    elif e.direction == DIRECTION_LEFT and x > 0:
        x = x - 1
    elif e.direction == DIRECTION_RIGHT and x < 7:  
        x = x + 1

    sense.set_pixel(x, y, W)

sense.show_message("Score: " + str(score))

if score == 5:
  sense.show_message("Level 2")
  def wait_for_move():
      while True:
        e = sense.stick.wait_for_event()
        if e.action != ACTION_RELEASED:
          return e

  R = [255, 0, 0]  # red
  Y = [255, 255, 0] # yellow
  G = [0, 255, 0] # green
  W = [255, 255, 255] # white

  for turns in range(5):

    coinx = randint(0,7)
    coiny = randint(0,7)
    print(coinx, coiny)

    sense.set_pixel(coinx, coiny, Y)
    sleep(1.5)
    sense.clear(Y)
    sleep(1)
    sense.clear()

    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(x, y, W)

    while True:
    
      e = wait_for_move()
      
      if e.direction == DIRECTION_MIDDLE:

          if x == coinx and y == coiny:
              sense.set_pixel(x, y, G)
              score += 1



          else:
              sense.set_pixel(x, y, R)

               
        
          sleep(1.25)
          sense.clear()
          sleep(0.5)


          break;


               
      sense.clear()
      if e.direction == DIRECTION_UP and y > 0:
          y = y - 1
      elif e.direction == DIRECTION_DOWN and y < 7:
          y = y + 1
      elif e.direction == DIRECTION_LEFT and x > 0:
          x = x - 1
      elif e.direction == DIRECTION_RIGHT and x < 7:  
          x = x + 1

      sense.set_pixel(x, y, W)
  sense.show_message("Score: " + str(score))
else:
  sense.show_message("You Lose")

if score == 10:
  sense.show_message("Level 3")
  def wait_for_move():
      while True:
        e = sense.stick.wait_for_event()
        if e.action != ACTION_RELEASED:
          return e

  R = [255, 0, 0]  # red
  Y = [255, 255, 0] # yellow
  G = [0, 255, 0] # green
  W = [255, 255, 255] # white

  for turns in range(5):

    coinx = randint(0,7)
    coiny = randint(0,7)
    print(coinx, coiny)

    sense.set_pixel(coinx, coiny, Y)
    sleep(0.5)
    sense.clear(Y)
    sleep(0.5)
    sense.clear()
    sleep(0.5)
    sense.clear(G)
    sleep(0.5)
    sense.clear()
    sleep(0.5)
    sense.clear(R)
    sleep(1)
    sense.clear()
  

    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(x, y, W)

    while True:
    
      e = wait_for_move()
      
      if e.direction == DIRECTION_MIDDLE:

          if x == coinx and y == coiny:
              sense.set_pixel(x, y, G)
              score += 1



          else:
              sense.set_pixel(x, y, R)

               
        
          sleep(1.25)
          sense.clear()
          sleep(0.5)


          break;


               
      sense.clear()
      if e.direction == DIRECTION_UP and y > 0:
          y = y - 1
      elif e.direction == DIRECTION_DOWN and y < 7:
          y = y + 1
      elif e.direction == DIRECTION_LEFT and x > 0:
          x = x - 1
      elif e.direction == DIRECTION_RIGHT and x < 7:  
          x = x + 1

      sense.set_pixel(x, y, W)
  sense.show_message("Score: " + str(score))
            
else:
  sense.show_message("You Lose")

if score == 15:
  sense.show_message("Level 4")
  def wait_for_move():
      while True:
        e = sense.stick.wait_for_event()
        if e.action != ACTION_RELEASED:
          return e

  R = [255, 0, 0]  # red
  Y = [255, 255, 0] # yellow
  G = [0, 255, 0] # green
  W = [255, 255, 255] # white
  O = [255, 165, 0]
  V = [238, 130, 238]
  B = [135, 206, 235]
  X = [0, 0, 0]
  I = [0, 0, 255]

  for turns in range(5):

    for i in range(2):
      
      coinx = randint(0,7)
      coiny = randint(0,7)
      print(coinx, coiny)

      sense.set_pixel(coinx, coiny, Y)
      sleep(0.25)
      sense.clear()
    rainbow = [
      R, R, R, R, R, R, R, R,
      R, O, O, O, O, O, O, O,
      R, O, Y, Y, Y, Y, Y, Y,
      R, O, Y, G, G, G, G, G,
      R, O, Y, G, B, B, B, B,
      R, O, Y, G, B, I, I, I,
      R, O, Y, G, B, I, V, V,
      R, O, Y, G, B, I, V, X
      ]
    invrainbow = [
      X, V, I, B, G, Y, O, R,
      V, V, I, B, G, Y, O, R,
      I, I, I, B, G, Y, O, R,
      B, B, B, B, G, Y, O, R,
      G, G, G, G, G, Y, O, R,
      Y, Y, Y, Y, Y, Y, O, R,
      O, O, O, O, O, O, O, R,
      R, R, R, R, R, R, R, R
      ]
    sense.set_pixels(rainbow)
    sleep(0.5)
    sense.clear()
    sleep(0.25)
    sense.set_pixels(invrainbow)
    sleep(0.5)
    sense.clear()
    sleep(0.25)
    sense.clear(R)
    sleep(0.25)
    sense.clear(O)
    sleep(0.25)
    sense.clear(Y)
    sleep(0.25)
    sense.clear(G)
    sleep(0.25)
    sense.clear(B)
    sleep(0.25)
    sense.clear(I)
    sleep(0.25)
    sense.clear(V)
    sleep(0.25)
    sense.clear()
    

    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(x, y, W)

    while True:
    
      e = wait_for_move()
      
      if e.direction == DIRECTION_MIDDLE:

          if x == coinx and y == coiny:
              sense.set_pixel(x, y, G)
              score += 1



          else:
              sense.set_pixel(x, y, R)

               
        
          sleep(1.25)
          sense.clear()
          sleep(0.5)


          break;


               
      sense.clear()
      if e.direction == DIRECTION_UP and y > 0:
          y = y - 1
      elif e.direction == DIRECTION_DOWN and y < 7:
          y = y + 1
      elif e.direction == DIRECTION_LEFT and x > 0:
          x = x - 1
      elif e.direction == DIRECTION_RIGHT and x < 7:  
          x = x + 1

      sense.set_pixel(x, y, W)
  sense.show_message("Score: " + str(score))
            
else:
  sense.show_message("You Lose")


if score == 20:
  sense.show_message("Level 5")
  def wait_for_move():
      while True:
        e = sense.stick.wait_for_event()
        if e.action != ACTION_RELEASED:
          return e

  R = [255, 0, 0]  # red
  Y = [255, 255, 0] # yellow
  G = [0, 255, 0] # green
  W = [255, 255, 255] # white
  O = [255, 165, 0]
  V = [238, 130, 238]
  B = [135, 206, 235]
  X = [0, 0, 0]
  I = [0, 0, 255]

  for turns in range(5):

    for i in range(5):
      
      coinx = randint(0,7)
      coiny = randint(0,7)
      print(coinx, coiny)
      distract = randint(0,7)
      distract = randint(0,7)
      

      sense.set_pixel(coinx, coiny, Y)
      sense.set_pixel(distract, distract, B)

      sleep(0.30)
      sense.clear()
    rainbow = [
      R, R, R, R, R, R, R, R,

      R, O, O, O, O, O, O, O,
      R, O, Y, Y, Y, Y, Y, Y,
      R, O, Y, G, G, G, G, G,
      R, O, Y, G, B, B, B, B,
      R, O, Y, G, B, I, I, I,
      R, O, Y, G, B, I, V, V,
      R, O, Y, G, B, I, V, X
      ]
    invrainbow = [
      X, V, I, B, G, Y, O, R,
      V, V, I, B, G, Y, O, R,
      I, I, I, B, G, Y, O, R,
      B, B, B, B, G, Y, O, R,
      G, G, G, G, G, Y, O, R,
      Y, Y, Y, Y, Y, Y, O, R,
      O, O, O, O, O, O, O, R,
      R, R, R, R, R, R, R, R
      ]
    sense.set_pixels(rainbow)
    sleep(0.25)
    sense.clear()
    sleep(0.25)
    sense.set_pixels(invrainbow)
    sleep(0.25)
    sense.clear()
    sleep(0.25)
    sense.clear(R)
    sleep(0.25)
    sense.clear(O)
    sleep(0.25)
    sense.clear(Y)
    sleep(0.25)
    sense.clear(G)
    sleep(0.25)
    sense.clear(B)
    sleep(0.25)
    sense.clear(I)
    sleep(0.25)
    sense.clear(V)
    sleep(0.25)
    sense.clear()
    sense.set_pixels(rainbow)
    sleep(0.25)
    sense.clear()
    sleep(0.25)
    sense.set_pixels(invrainbow)
    sleep(0.25)
    sense.clear()
    

    x = randint(0,7)
    y = randint(0,7)
    sense.set_pixel(x, y, W)

    while True:
    
      e = wait_for_move()
      
      if e.direction == DIRECTION_MIDDLE:

          if x == coinx and y == coiny:
              sense.set_pixel(x, y, G)
              score += 1



          else:
              sense.set_pixel(x, y, R)

               
        
          sleep(1.25)
          sense.clear()
          sleep(0.5)


          break;


               
      sense.clear()
      if e.direction == DIRECTION_UP and y > 0:
          y = y - 1
      elif e.direction == DIRECTION_DOWN and y < 7:
          y = y + 1
      elif e.direction == DIRECTION_LEFT and x > 0:
          x = x - 1
      elif e.direction == DIRECTION_RIGHT and x < 7:  
          x = x + 1

      sense.set_pixel(x, y, W)
  sense.show_message("Score: " + str(score))
  sense.show_message("You Win!")
            
else:
  sense.show_message("You Lose")


 
