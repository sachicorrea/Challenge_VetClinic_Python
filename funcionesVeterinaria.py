#---------------- Zona de librerias------------
from collections import namedtuple
from typing import NamedTuple

#---------------- Zona de Constantes------------
PERRO="perro"
GATO="gato"
OTRO="otro"

#---------------- Zona Diccionarios------------

diccionario_servicios={"consulta": 40000, "peluqueria":25000, "vacunacion":35000, "hospitalizacion":200000, "cirugia":400000}

#---------------- Zona Tuplas------------
Mascota= namedtuple("Mascota", "id nombre propietario tipo raza compania")

mascota1=Mascota(10, "Max", "Pedro", PERRO, "Collie", True)
mascota2=Mascota(20, "Rex", "Reinaldo", PERRO, "Pastor Aleman", True)
mascota3=Mascota(30, "Milo", "Juana", PERRO, "Labrador", False)
mascota4=Mascota(40, "Orion", "Linda", GATO, "Persa", False)

#---------------- Zona listas------------

lista_mascotas=[mascota1, mascota2, mascota3, mascota4]

#---------------- Zona funciones------------

# Pet Class
class Pet(NamedTuple):
  id: int
  name: str
  owner: str
  category: str
  breed: str
  company: bool

  def print_me(self):
    print(f"{self.id}-{self.name}-{self.category}")

def get_pets():
  return [
      Pet(10, "Max", "Pedro", PERRO, "Collie", True),
      Pet(20, "Rex", "Reinaldo", PERRO, "Pastor Aleman", True),
      Pet(30, "Milo", "Juana", PERRO, "Labrador", False),
      Pet(40, "Orion", "Linda", GATO, "Persa", False),
  ]
# End Class Pet

def mostrar_servicios_precios():
  """
  TODO 
  Mostrar todos los servicios y precios con el formato nombre:precio
  ejemplo: consulta:40000
  """
  for service, cost in diccionario_servicios.items():
    print("{}:{}".format(service, cost))

def adicionar_nuevo_servicio(nombre, precio):
  """
  TODO 
  Adiciona un nuevo servicio 
  Parametros: 
    nombre: nombre del nuevo servicio
    precio: precio del nuevo servicio

  Si el servicio ya existe, actualiza el valor por el valor actual
  """
  diccionario_servicios[nombre] = precio

def buscar_servicio(nombre_servicio):
  """
  TODO
  Busca un servicio 
    Si lo encuentra retorna el nombre y el valor (Tenga en cuenta buscar sin importar mayusculas o minusculas)
    Ejemplo: 40000
    Si no lo encuenta retorna un mensaje "servicio no encontrado"
  """

  if nombre_servicio in diccionario_servicios:
    searchService = diccionario_servicios.get(nombre_servicio)
        
    return "{}:{}".format(nombre_servicio,searchService)

  return "servicio no encontrado"

def eliminar_servicio(nombre_servicio):
  """
  TODO
  Elimina un servicio 
    Si lo encuentra retorna el mensaje servicio nombre_servicio eliminado
    Ejemplo: servicio consulta eliminado
    Si no lo encuenta retorna un mensaje "servicio no encontrado"
  """
  
  if nombre_servicio in diccionario_servicios:
        
    diccionario_servicios.pop(nombre_servicio)
    return "servicio " + nombre_servicio + " eliminado"

  return "servicio no encontrado"

def mostrar_servicios_rango_precios(rangoInicial, rangoFinal):
  """
  Mostrar servicios por rango inicial y rango final
  Debe validar que el rango inicial sea menor al rango final
  """
  newDict = dict()
  for (key, value) in diccionario_servicios.items():
    if value > rangoInicial and value < rangoFinal:
      newDict[key] = value

  for service, price in newDict.items():
    print("{}:{}".format(service, price))

def mostrar_mascotas():
  """
  Mostrar mascotas con todos sus datos
  """
  for id, name, owner, category, breed, company in lista_mascotas:
    print(f'{id}-{name}-{owner}-{category}-{breed}-{company}')

def adicionar_nuevo_paciente(id, nombre, propietario,tipo,raza,compania):
  """
  Adiciona un nueva mascota, debe validar que el id no exista previamente
  """
  mascota5 = Mascota(id, nombre, propietario, tipo, raza, compania)
  return mascota5
    
def buscar_mascota(nombre_mascota):
  """
  Busca una mascota según su nombre
    Si la encuentra retorna un mensaje con su id, nombre y tipo
    Ejemplo: 10-Max-perro
    Sino la encuentra retorna un mensaje "mascota no encontrada"
  Recuerde validar que el nombre puede estar con mayusculas o minisculas 
  """
  # Generator expression to find list index where pet's name is located - Pet class constructor
  indexlistPets = next((i for i, v in enumerate(get_pets()) if v[1] == nombre_mascota), None)

  # Invokin constructor of Pet class
  pets = get_pets()

  if (indexlistPets or indexlistPets == 0):
    return pets[indexlistPets].print_me()
  return "mascota no encontrada"

def eliminar_mascota(id_mascota):
  """
  TODO elimina una mascota según su id
    Si la encuentra y elimina retorna un mensaje, ejemplo: mascota Max eliminada
    Sino retorna un mensaje "mascota no encontrada"

  """
  return ""


def mostrar_mascota_tipo(tipo_buscado):
  """
  TODO muestra mascota según el tipo buscado gato - perro - otro
  ejemplo: 10-Max-Collie-Pedro
  """
  pets = get_pets()
  filtered = []

  for item in pets:
    if item[3] == tipo_buscado:
      filtered.append(item)

  for id, name, owner, category, breed, company in filtered:
    print(f'{id}-{name}-{breed}-{owner}')

def porcentaje_mascotas_compania():
  """
  TODO
  Muestra el porcentaje de mascosta de compañia registrada en la clinica veterinaria
  ejemplo: 20%
  """
  return ""