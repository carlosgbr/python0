""" Funciones y condicionales if: resultados_examen.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Entrada: 
  Salida: 
  Se ilustra el uso de funciones y la estructura if en Python
"""
"""
ENUNCIADO: Los estudiantes en una clase reciben sus calificaciones como 
aprobado / reprobado. Un puntaje de 60 o más (de 100) significa que la
calificación es "Aprobado". Para puntajes más bajos, la calificación es 
"Reprobado". Además, los puntajes superiores a 95 (no incluidos) se califican 
como "Puntaje superior". Complete esta función para que devuelva la 
calificación adecuada.
"""
def resultados_examen(puntuacion):
	if puntuacion > 95:
		grado = "Puntaje superior"
	elif puntuacion >=60:
		grado = "Aprobado"
	else:
		grado = "Reprobado"
	return grado

print(resultados_examen(65)) # Debe ser Aprobado
print(resultados_examen(55)) # Debe ser Reprobado
print(resultados_examen(60)) # Debe ser Aprobado
print(resultados_examen(95)) # Debe ser Aprobado
print(resultados_examen(100)) # Debe ser Puntaje superior
print(resultados_examen(0)) # Debe ser Reprobado
