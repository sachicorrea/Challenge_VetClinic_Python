""" RETO SEMANA 5
  Santiago Correa Restrepo
  Clínica veterinaria
  Grupo 96
  Mayo 08 de 2021
"""""

import funcionesVeterinaria as f

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
#---------------- Zona librerias------------
def menuOpciones():
  bandera=0
  while(bandera == 0):
    print("\n ||||--------------- CLINICA VETERINARIA ---------------|||| ")
    print("\n [............. SERVICIOS ................]\n")
    print("   1.Mostrar servicios y precio (1) ")
    print("   ...............................")
    print("   2. Adicionar nuevo servicio (2) ")
    print("   ...............................")
    print("   3. Buscar servicio por nombre (3) ")
    print("   ...............................")
    print("   4. Eliminar servicio por nombre (4) ")
    print("   ...............................")
    print("   5. Mostrar servicios por rango de precio (5) ")
    print("\n [........ PACIENTES MASCOTAS ...........]\n")
    print("   6. Mostrar pacientes mascotas (6) ")
    print("   ...............................")
    print("   7. Adicionar nuevo paciente (7) ")
    print("   ...............................")
    print("   8. Buscar paciente mascota por nombre  (8) ")
    print("   ...............................")
    print("   9. Eliminar paciente mascota por id  (9) ")
    print("   ...............................")
    print("   10. Mostrar pacientes mascotas por tipo (10)")
    print("   ...............................")
    print("   11. Mostrar porcentaje mascotas compañia (11)")
    print("   ...............................")
    print("\n 0. Salir (0)")
    print("\n .............OPCIONALES..................")
    print("....")
    opcion = int(input("\n Seleccione una opción: "))

    if(opcion==1):
      print("1. Mostrar servicios y precio")
      #TODO
      f.mostrar_servicios_precios()
    
    if(opcion==2):
      print("2. Adicionar nuevo servicio")
      #TODO
      nombre = input("Ingrese nuevo servicio: ")
      precio = int(input("Ingrese valor:"))
      f.adicionar_nuevo_servicio(nombre, precio)
    
    if(opcion==3):
      print("3. Buscar servicio por nombre")
      #TODO

      nombre_servicio = input("Ingrese servicio a buscar: ")
      print(f.buscar_servicio(nombre_servicio))
    
    if(opcion==4):
      print("4. Eliminar servicio por nombre")

      nombre_servicio = input("Ingrese servicio a eliminar: ")
      print(f.eliminar_servicio(nombre_servicio))

    if(opcion==5):
      print("5. Mostrar servicios por rango de precio")

      rangoInicial = int(input("Ingrese rango inicial:"))
      rangoFinal = int(input("Ingrese rango final:"))

      f.mostrar_servicios_rango_precios(rangoInicial, rangoFinal)
    
    if(opcion==6):
      print("6. Mostrar pacientes mascotas")
      f.mostrar_mascotas()

    if(opcion==7):
      print("7. Adicionar nuevo paciente")
      
      def entry_data_pets():

        id = int(input("ingrese id: "))
        name = input("ingrese nombre mascota: ")
        owner = input("ingrese nombre propietario: ")
        category = input("ingrese tipo perro/gato: ")
        breed = input("ingrese raza mascota: ")
        company = bool(input("ingrese si es animal de compañia True o False: "))

        thislist = [id, name, owner, category, breed, company]
        return thislist

      questions = entry_data_pets()

      id = questions[0]
      nombre = questions[1]
      propietario = questions[2]
      tipo = questions[3]
      raza = questions[4]
      compania = questions[5]

      f.adicionar_nuevo_paciente(id, nombre, propietario,tipo,raza,compania)

    if(opcion==8):
      nombre_mascota = input("ingrese nombre mascota a buscar: ")
      print(f.buscar_mascota(nombre_mascota))

    if(opcion==10):
      print("10. Mostrar pacientes mascotas por tipo")
      tipo_buscado = input('perro - gato - otro: ')
      f.mostrar_mascota_tipo(tipo_buscado)

    elif(opcion==0):
      bandera=1

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#Recuerde comentar la siguiente instrucción para ejecutar los test
menuOpciones()
