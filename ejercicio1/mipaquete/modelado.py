#Clase principal de la cual se van a heredar los atributos que comparten los demas empleados
class Empleado(object):
	#se crea los atributos de empleado que se compartiran con las demas clases
	def __init__(self):
		self.nombre = ""
		self.apellido = ""
		self.cedula = ""
		self.comision_fija = 0.0 
	#metodos para agregar y obtener comision fija 
	def agregar_comision_fija(self, comision):
		self.comision_fija = comision

	def obtener_comision_fija(self):
		return self.comision_fija
	#metodos para agregar y obtener el nombre del empleado	
	def agregar_nombre(self, n):
		self.nombre = n

	def obtener_nombre(self):
		return self.nombre
	#metodos para agregar y obtener el apllido del empleado	
	def agregar_apellido(self,a):
		self.apellido = a

	def obtener_apellido(self):
		return self.apellido
	#metodos para agregar y obtener la cedula del empleado 	
	def agregar_cedula(self,c):
		self.cedula = c

	def obtener_cedula(self):
		return self.cedula
	# metodo para presentar todos los datos del empleado, este metodo presentar datos sera el que se envie a las demas clases para la presentacion de valores 	
	def presentar_datos(self):
		cadena = "Informacion de %s %s\n\t Cedula: %s" % (self.obtener_nombre(), self.apellido, self.obtener_cedula())
		return cadena

#clase hija que se refiere a los empleados por hora se llama a la pase padre
class EmpleadoPorHoras(Empleado):
	"""docstring for EmpleadoPorHoras"""
	#se llama con super los atributos de la clase padre
	def __init__(self):
		super(EmpleadoPorHoras, self).__init__()
		#se crea las variables locales de la clase
		self.numero_horas = 0 
		self.valor_horas = 0 
		self.sueldo_final = 0 	
	#metodos para agregar el numero de horas y el valor de las horas
	def agregar_numero_horas(self,h):
		self.numero_horas = h

	def agregar_valor_horas(self,v):
		self.valor_horas = v
	#metodos para obtener el valor y el numero de las horas 
	def obtener_numero_horas(self):
		return self.numero_horas

	def obtener_valor_horas(self):
		return self.valor_horas
 	#metodos para calcular el sueldo final
	def calcular_valor_sueldo(self):
		self.sueldo_final = (self.numero_horas * self.valor_horas) 
		return self.sueldo_final

	#metodo para presentar los datos de los empleados por hora
	def presentar_datos(self):
		cadena = "%s\n\tNumero horas: %s\n\tValor hora: %s\n\tSueldo Final: %s" % (super(EmpleadoPorHoras,self).presentar_datos(), self.obtener_numero_horas(), self.obtener_valor_horas(), self.calcular_valor_sueldo())
		return cadena
#s
class EmpleadoFijo(Empleado):
	"""docstring for EmpleadoFijo"""
	def __init__(self):
		super(EmpleadoFijo, self).__init__()
		self.sueldo_fijo = 0 
		self.descuento_seguro = 0 
		self.sueldo_final = 0.0

	def agregar_sueldo_fijo(self,s):
		self.sueldo_fijo = s 

	def agregar_descuento(self,d):
		self.descuento_seguro = d


	def obtener_sueldo_fijo(self):
		return self.sueldo_fijo

	def obtener_descuento(self):
		return self.descuento_seguro

	def calcular_sueldo_final(self):
		self.sueldo_final = ((self.sueldo_fijo - ((self.sueldo_fijo * self.descuento_seguro)/100)) + super(EmpleadoFijo,self).obtener_comision_fija())
		return self.sueldo_final

	def presentar_datos(self):
		cadena = "%s\n\tSueldo Fijo: %s\n\tDescuento del seguro:%s\n\tSueldo Final:%s" %(super(EmpleadoFijo,self).presentar_datos(), self.obtener_sueldo_fijo(), self.obtener_descuento(), self.calcular_sueldo_final())
		return cadena

				