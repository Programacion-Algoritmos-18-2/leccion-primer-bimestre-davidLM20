#Se importa todo lo que tinene el paquete
from mipaquete.modelado import *
#se crea el objeto para agregar valores y presentar usando la clase padre
e = Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("1110001")
print(e.presentar_datos())

#se crea una segunda clase para agregar valores y presentar datos esta ves se usara la clase empleado por hora y los valores de la clase padre
e1 = EmpleadoPorHoras()
nombre = input("Ingrese el nombre:\n")# se pide por teclado el nombre
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.cedula = "112233"
e1.agregar_valor_horas(20.2)
e1.agregar_numero_horas(15)
print(e1.presentar_datos()) 

#se crea un nuevo objeto este trabajara con la clase empleado fijo
e2 = EmpleadoFijo()
e2.agregar_sueldo_fijo(300.2)
e2.descuento_seguro = 10
comision = float(input("Ingrese comision:\n")) # se pide la comision y se lo declara como objeto
e2.agregar_comision_fija(comision)
e2.nombre = "Ana"
e2.apellido = "Diaz"
print(e2.presentar_datos()) 

#este objeto es para comprobar la funcionalidad de la clase empelado por semana
e3 = EmpleadoPorSemana()
e3.agregar_numero_semana(3)
e3.agregar_valor_semana(80)
e3.nombre = "David"
e3.apellido = "Diaz"
print(e3.presentar_datos()) 
