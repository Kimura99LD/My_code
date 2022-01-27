f = open("altura.txt","r")
estaturas = []
for linea in f.readlines():
  estaturas.append(float(linea))
f.close()

print(f"La cantidad de alturas registradas es de {len(estaturas)} mediciones.")
print(f"La altura minima registrada es de: '{min(estaturas)}m', y la maxima altura registrada es de:'{max(estaturas)}m.' ")

media = sum(estaturas) / len(estaturas)
print(f"La estatura media es de {media:.2f}m.")

numerador=0
for estatura in estaturas:
  numerador = numerador + (estatura-media)**2
  desv= (numerador / (len(estaturas)-1))**0.5
print(f"La desviacion tipica es de: {desv:.3f}m")

estatura = float(input("¿Cuánto mídes?: "))
if estatura > media:
  print(f"Mides {100 * (estatura - media):.0f}cm más de la media")
else:
  print(f"Mides {100 * (estatura - media):.0f}cm menos que la media")

print("Fin del programa") 