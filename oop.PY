class GrupoAnimal:
   x: int = 0

   def __init__(self, nom: str) -> None:
     self.nombre = nom
     print('Estoy construido', nom)
   def grupo(self) -> None:
     self.x = self.x + 1
     print(self.nombre,"recuento grupal",self.x)

   def __del__(self) -> None:
     print('Estoy destruido', self.nombre, self.x)  

class GrilloFan(GrupoAnimal):
    puntos: int=0

    def seis(self) -> None:
        self.puntos = self.puntos + 6
        self.grupo()
        print(self.nombre,"puntos", self.puntos) 

s: GrupoAnimal = GrupoAnimal(nom='Sally')
j: GrilloFan = GrilloFan(nom='Jim')

s.grupo()
j.grupo()
j.seis()

print(dir(j))