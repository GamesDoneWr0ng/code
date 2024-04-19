import pygame as pg
import numpy as np

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 800
VINDU_HOYDE  = 600
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
font = pg.font.SysFont("Arial", 30)

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, pos, radius, farge):
    """Konstruktør"""
    self.pos = pos
    self.radius = radius
    self.farge = farge
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(vindu, self.farge, self.pos, self.radius) 
  
  def finnAvstand(self, annenBall):
    """Metode for å finne avstanden til en annen ball"""
    sentrumsavstand = np.sqrt(np.sum((self.pos - annenBall.pos) **2))

    radiuser = self.radius + annenBall.radius

    avstand = sentrumsavstand - radiuser

    return avstand


class Hinder(Ball):
  """Klasse for å representere et hinder"""
  def __init__(self, pos, radius, farge, fart: np.ndarray):
    super().__init__(pos, radius, farge)
    self.fart = fart

  def flytt(self, spiller, angle):
    """Metode for å flytte hinderet"""
    # Sjekker om hinderet er utenfor høyre/venstre kant
    if ((self.pos[0] + self.radius) <= 0) and self.fart[0] < 0 or ((self.pos[0] - self.radius) >= vindu.get_width()) and self.fart[0] > 0:
      # gå til andre side av vindu
      self.pos[0] = vindu.get_width() - self.pos[0]
    
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.pos[1] - self.radius) <= 0) and self.fart[1] < 0 or ((self.pos[1] + self.radius) >= vindu.get_height()) and self.fart[1] > 0:
      self.fart[1] *= -1

    # homeing
    dir = np.sign(np.cross(self.fart, spiller.pos - self.pos))
    if dir < 0:
      # rotate clockwise
      self.fart = np.matmul(self.fart, np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])) 
    else:
      # rotate counterclockwise
      self.fart = np.matmul(self.fart, np.array([[np.cos(-angle), -np.sin(-angle)], [np.sin(-angle), np.cos(-angle)]]))

    # Flytter hinderet
    self.pos += self.fart

class Coin(Ball):
  def __init__(self, radius, farge):
    super().__init__(np.array((0,0)), radius, farge)
    self.randomizePos()

  def randomizePos(self):
    self.radius = np.random.uniform(5, 20)
    self.pos = np.array((np.random.randint(self.radius, VINDU_BREDDE-self.radius), np.random.randint(self.radius, VINDU_HOYDE-self.radius)))


class Spiller(Ball):
  """Klasse for å representere en spiller"""
  def __init__(self, pos, radius, farge, fart):
    super().__init__(pos, radius, farge)
    self.fart = fart

  def flytt(self):
    """Metode for å flytte spilleren"""
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] or keys[pg.K_w]:
      self.pos[1] -= self.fart
      if self.pos[1] < self.radius:
        self.pos[1] = self.radius
    if keys[pg.K_DOWN] or keys[pg.K_s]:
      self.pos[1] += self.fart
      if self.pos[1] > vindu.get_height()-self.radius:
        self.pos[1] = vindu.get_height()-self.radius
    if keys[pg.K_LEFT] or keys[pg.K_a]:
      self.pos[0] -= self.fart
      if self.pos[0] < self.radius:
        self.pos[0] = self.radius
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
      self.pos[0] += self.fart
      if self.pos[0] > vindu.get_width()-self.radius:
        self.pos[0] = vindu.get_width()-self.radius

# Lager et Spiller-objekt
spiller = Spiller(np.array((200, 200), dtype=np.float64), 20, (255, 69, 0), 0.2)

# Lager et Coin-objekt
coins = [
  Coin(np.random.uniform(5, 20), (255, 255, 0)
       ) for _ in range(3)]

# Lager et Hinder-objekt
hindere = [
  Hinder(np.random.uniform(0,150,2), np.random.uniform(5,20), (0, 0, 255), np.random.uniform(0.01,0.19,2)
         ) for _ in range(15)]

angle = 0
points = 0

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    angle += np.deg2rad(0.000001)

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter spiller og hinder
    spiller.flytt()
    spiller.tegn()

    for coin in coins:
      if spiller.finnAvstand(coin) <= 0:
        points += 1
        coin.randomizePos()
      coin.tegn()
      
    img = font.render(f"Poeng: {points}", True, (0, 0, 0))
    vindu.blit(img, (0, 0))

    for hinder in hindere:
        hinder.flytt(spiller, angle)
        hinder.tegn()

        # Sjekker avstanden mellom spiller og hinder
        #print(spiller.finnAvstand(hinder))
        if spiller.finnAvstand(hinder) <= 0:
            vindu.fill((135, 206, 235))
            spiller.tegn()
            hinder.tegn()
            print("Du tapte!", points)
            fortsett = False
            break

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()