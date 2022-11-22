# -*- coding: utf-8 *-* 

# IMPORTAMOS LAS LIBRERIAS NECESARIAS
from modulos.POOBBDD import AccesoBD
from modulos.Scraping import Scraper, fListaDeValores
import time # Para hacer pausas entre una página y otra
import random
# from tabulate import tabulate

print("\n\n\n****************************************\n*** RECUERDE QUE DEBE TENER CREADA   ***\n*** LA BASE DE DATOS QUE CORRESPONDA ***\n*** O CREARLA MEDIANTE EL SCRIPT     ***\n*** CORRESPONDIENTE Y, POR OTRO LADO,***\n*** DEBE CONFIGURAR LOS VALORES DE   ***\n*** ACCESO A SU BASE DE DATOS LOCAL  ***\n*** EN EL ARCHIVO POOBBDD.py PARA    ***\n*** PODER ACCEDER A GUARDAR LA INFO  ***\n*** EN LA BBDD.                      ***\n****************************************\n\n\n")
saliendo = input("Pulse cualquier tecla para continuar o escriba SALIR para salir:    ")

if saliendo.upper() == "SALIR":
      exit()
else:
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\nPor favor, aguarde mientras comenzamos la búsqueda\nde las páginas que contienen libros. \n\nEste proceso puede demorar unos 20 segundos como máximo (aproximadamente).\n\nLuego podrá ver en pantalla la información\nque se irá guardando en la BBDD, libro a libro.\n\n\nGracias por aguardar !!!")
print("\n\n\n")

# Ejecutamos la función Scraper(), del módulo Scraping.py que reúne la información de todos los links hacia los libros del sitio Tematika.com.
# Sabemos que, en total, la paginación de Tematika.com alcanza 2012 páginas conteniendo 20 (veinte) libros cada una. Lo que arroja un total que va entre 40221 y 40240 libros.

# Definimos la ruta principal
ruta = 'https://www.tematika.com/libros' 

# Ahora creamos el objeto de conexión a la base de datos con el módulo correspondiente proveniente del archivo /modulos/POOBBDD.py (ya improtado):
libro = AccesoBD()

# Iniciamos las variables que harán POR ETAPAS el proceso de recolección de datos de todas las páginas de los libros:
inicioEtapa = 1
finEtapa = 2

# Iniciamos la variable que mantendrá el siguiente bucle en funcionamiento mientras su valor no sea 1.
salir = 0


# especial = 1 # Variable temporal para continuar con el loop luego de alguna interrupción no prevista del sistema. Ej: errores de configuración de PHP, o de variables del sistema donde se ejecute. Mientras su valor sea 1, no ejecutará la sopa sobre esa URL ya que se trata de un libro ya recorrido antes. En el caso de hallar el libro mencionado en la siguiente variable (sitioDondeContinuar) se le dará el valor 0 para que a partir de aquí, recorra todos los libros subsiguientes.

# sitioDondeContinuar = "https://www.tematika.com/link-del-ultimo-libro-hallado.html" # Es el último sitio visitado que generó el error en tiempo de ejecución, como para continuar desde este punto.

# Iniciamos el bucle que recorrerá todas las páginas de Tematika.com
while not salir == 1:
      
      # Definimos el rango de consulta...
      rango = range(inicioEtapa, finEtapa) # 2012) # <<<<<<================================
            # EVITAMOS USAR LAS 2012 páginas en las verificaciones de código
            # ya que duraría 2 horas (o más) la recolección de la información.
            # ==========================================>>>>>>>>>>>>>>>>>>>>>>

      # Definimos la variable para obtener los links de los libros consultados. 
      linksLibros = Scraper(ruta, rango)
      temporal = 0
      # Recorremos el listado de links recibidos y los guardamos en la BBDD.
      for x in range(0, len(linksLibros)-1):
            ##################################
            ## BLOQUE PARA UTILIZAR EN CASO 
            # DE INTERRUPCIÓN IMPREVISTA DEL SISTEMA
            # if x == sitioDondeContinuar:
            #       especial = 0                        
            # if especial == 1:
            #       continue     
            #####################################
            try:
                  sql, bio = fListaDeValores(linksLibros[x]) # Ejecutamos la función listaDeValores que nos devuelve una lista para guardar en la BBDD por cada libro. 
                  # A fin de ir evaluando si todo va bien, mostramos la sentencia SQL que se ingresará a la BD en cada registro. De este modo sabremos que el proceso sigue activo y que aún no ha terminado.
            except:
                  continue
            
            print("=====================================")
            print("== Variables a insertar en la BBDD ==")
            print("===LISTA PARA LA SENTENCIA SQL=======")
            print(sql)
            print("========FIN DE LA LISTA =============")
            try:     
                  libro.InsertarLibro(sql)
            except:
                  continue
            
            if temporal > 3:   # Si el valor de temporal superó el valor 3, entonces
                  temporal = 0 # le asigna su valor original de cero.
            tmp = random.random()+temporal
            print("=== La próxima instrucción demorará ",round(tmp,2),"segs.===")
            time.sleep(round(tmp,2))  # Hace una pausa entre cada consulta al servidor web. Aquí se usa la variable "temporal" que añade un segundo al valor random para demostrar diferentes niveles de espera antes de volver a hacer una petición al servidor.
            # (Se usa esta función "time.sleep" para evitar bloqueos de IP).
            
            # Verificamos si el autor ya se encuentra en la base de datos:
            if libro.consultaBio(sql[1]) == False:
                  # Si no está, lo agregamos con su biografía correspondiente.
                  try:
                        libro.InsertarBio([sql[1],bio])
                  except:
                        continue
                  
            temporal = temporal + 1 # incrementa el valor de temporal en 1.

      salida = 0
      
      while salida == 0:
            print("Si desea continuar responda SI a la siguiente pregunta del sistema, si responde NO se dará por finalizado el proceso...")
            print("Actualmente hemos reunido información de unos",finEtapa*20,"libros.")
            seguir = input("¿Desea continuar recuperando información de más libros?")
            if seguir.upper() == "SI":
                  if finEtapa == 2000:
                        inicioEtapa = 2001
                        finEtapa = 2012
                  else:      
                        inicioEtapa = finEtapa + 1
                        finEtapa = finEtapa + 10
                  salida = 1
                  continue
            elif seguir.upper() == "NO":
                  salida = 1
                  salir = 1
                  break
            else:
                  continue

print("\n\nSe terminó de ejecutar el proceso \n\n")
iterador = 1
valor = 3
while not iterador == 0:
      print("Indique qué desea hacer:")
      print("1 . Modificar información de un libro almacenado en la BBDD.")
      print("2 . Eliminar un libro almacenado en la BBDD.")
      print("0 . Salir.")
      valor = int(input("Ingrese su elección: "))
      if valor < 0 or valor > 2:
            continue
      elif valor == 1:
            listaCampos = ['id', 'titulo', 'autor', 'disponibilidad', 'precio', 'editorial', 'isbn', 'paginas', 'idioma', 'formato', 'clasificacion', 'fechaPub']
            resultado = libro.Ver(listaCampos)
            #print(tabulate(resultado, headers=listaCampos))
            for x in resultado:
                  print('Nº: ',x[0],' Título: ',x[1],' Autor: ',x[2],' Disponibilidad: ',x[3],' Precio: ',round(float(x[4]),2),' Editorial: ',x[5],' ISBN: ',x[6],' Páginas: ',x[7],' Idioma: ',x[8],' Formato: ',x[9],' Clasificación: ',x[10],' Publicado: ',x[11])
            print("\n\nIndique en qué Nº de libro desea hacer cambios")
            while True:
                  try:
                        nroId = int(input("(elija para ello el número que se encuentre a la izquierda del título que desea modificar):"))
                  except ValueError:
                        print("Debes escribir un número.")
                        continue

                  if nroId < 0:
                        print("Debes escribir un número positivo.")
                        continue
                  else:
                        break
            print("1) Disponibilidad\n2) Idioma\n3) Formato\n4) Clasificacion")
            print("Indique qué aspecto de ese libro desea modificar")
            while True:
                  try:
                        eleccion = int(input("de acuerdo a la lista numerada :"))
                  except ValueError:
                        print("Debes escribir un número.")
                        continue

                  if eleccion < 0:
                        print("Debes escribir un número positivo.")
                        continue
                  elif eleccion > 4:
                        print("Debes escribir un número entre el 1 y el 4.")
                        continue
                  else:
                        break
            if eleccion == 1:
                  campo = "disponibilidad"
            elif eleccion == 2:
                  campo = "idioma"
            elif eleccion == 3:
                  campo = "formato"
            elif eleccion == 4:
                  campo = "clasificacion"
                  
            print("Indique qué nuevo valor tendrá ese campo que eligió")
            valorACambiar = input("de acuerdo a la lista numerada :")                        
            libro.Cambiar([campo, valorACambiar, nroId])                  
            
      elif valor == 2:
            listaCampos = ['id', 'titulo', 'autor', 'disponibilidad', 'precio', 'editorial', 'isbn', 'paginas', 'idioma', 'formato', 'clasificacion', 'fechaPub']
            resultado = libro.Ver(listaCampos)
            for x in resultado:
                  print('Nº: ',x[0],' Título: ',x[1],' Autor: ',x[2],' Disponibilidad: ',x[3],' Precio: ',x[4],' Editorial: ',x[5],' ISBN: ',x[6],' Páginas: ',x[7],' Idioma: ',x[8],' Formato: ',x[9],' Clasificación: ',x[10],' Publicado: ',x[11])
            print("\n\nIndique el Nº de libro que desea BORRAR")
            while True:
                  try:
                        nroId = int(input("(elija para ello el número que se encuentre a la izquierda del título que desea BORRAR):"))
                  except ValueError:
                        print("Debes escribir un número.")
                        continue

                  if nroId < 0:
                        print("Debes escribir un número positivo.")
                        continue
                  else:
                        break
            libro.Borrar(nroId)
            print("\n\nEl libro "+str(nroId)+" fue borrado exitosamente !!!\n\n")
                  
      elif valor == 0:
            print("")
            print("=============================================")
            print("¡ Muchas gracias por usar el sistema BBBBB5 !")
            print("=============================================\n\n")
            iterador = 0
            print("Ha salido del sistema...\n\n")
