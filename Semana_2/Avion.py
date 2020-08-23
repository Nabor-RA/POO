print(" A   V   I   O   N")
print("")
class Avion:
    def __init__(self, persona, tamaño, color, carga, capacidad_tanque,
                 tiempo_vuelo, altura, velocidad, marca):
        self.persona = persona
        self.tamaño = tamaño
        self.color = color
        self.carga = carga
        self.capacidad_tanque = capacidad_tanque
        self.tiempo_vuelo = tiempo_vuelo
        self.altura = altura
        self.velocidad = velocidad
        self.marca = marca
        print("Se acaba de crear un objeto")
        print("")
    def volar(self):
        print("volando")
    def aterrizar(self):
        print("aterrizando")
    def acelerar(self):
        print("acelerando")
    def bajar_velocidad(self):
        print("reduciendo velocidad")
    def girar(self):
        print("girando")
    def __str__(self):
        return "EL avion de marca {} va a una velocidad {}".format(
            self.marca, self.velocidad)
f = Avion(15, 60, "Blanco", 50, 15, 56, "Mediana", "Maxima", "no")
print("")
print("Metodos")
f.volar()
f.aterrizar()
f.acelerar()
f.bajar_velocidad()
f.girar()
print("Atributos")
print(str(f))