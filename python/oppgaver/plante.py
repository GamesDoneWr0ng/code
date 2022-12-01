class Plant:
    def __init__(self, maksgrenseVann):
        self.maksgrenseVann = maksgrenseVann
        self.vannbeholder = 0
        self.alive = True
    
    def vannPlante(self, vannCl):
        self.vannbeholder = self.vannbeholder + vannCl
        if self.vannbeholder > self.maksgrenseVann:
            self.alive = False
    
    def nyDag(self):
        self.vannbeholder = self.vannbeholder - 20
        if self.vannbeholder < 0:
            self.alive = False
        
    def levende(self):
        return self.alive

plante40 = Plant(40)
plante90 = Plant(90)

plante40.vannPlante(10)
plante90.vannPlante(10)

plante40.nyDag()
plante90.nyDag()
plante40.nyDag()
plante90.nyDag()

print(plante40.levende())
print(plante90.levende())