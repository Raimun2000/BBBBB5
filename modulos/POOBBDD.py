# -*- coding: utf-8 *-* 

# IMPORTAMOS LIBRERIA NECESARIA
import mysql.connector # Instalar mediante: pip install mysql-connector-python

class AccesoBD:
      '''
      Clase AccesoBD que proporciona los accesos necesarios a la BBDD "Proy_Colab_BBBBB5" de la actividad propuesta en el PROYECTO TECNOLÓGICO INTEGRADOR 2022 - PROYECTO GAMA.
      '''
      def __init__(self, host = 'localhost', user = 'root', password = '', database = 'Proy_Colab_BBBBB5'):
            self.conexion = mysql.connector.connect(
                  host = host,
                  user = user,
                  password = password,
                  database = database
                  )
            self.cursor = self.conexion.cursor()

            
      def nuevaBD(self, nombre):
            '''
            El método "nuevaBD" crea una nueva Base de Datos
            '''
            
            self.mysql_cursor.execute("CREATE DATABASE", self.nombre)

      def nuevaTabla(self,nombre,listaCampos):
            '''
            El método "nueva Tabla" crea una tabla dentro de la base de datos a la que se haya conectado el usuario.\nEl parámetro "listaCampos" es una lista que contiene todas las características de los campos que contendrá la tabla.\nDeberá tener, por ejemplo, este formato:\n["id INT(11)", "titulo VARCHAR(100)", "autor VARCHAR(100)", "disponibilidad VARCHAR(30)", "precio DOUBLE(8,2)"]
            '''
            
            self.sql = "CREATE TABLE "+nombre+"("
            p = 0
            largo = len(listaCampos)
            for x in listaCampos:
                  if p == largo:
                        self.sql = self.sql+x+");"
                  else:
                        self.sql = self.sql+x+", "
                  p = p+1
            self.mysql_cursor.execute(self.sql)

      def clavePrimaria(self,campoClave):
            '''El método "clavePrimaria" permite indicar a una nueva base de datos, cuál sería el campo que funcionará como clave primaria.\nPor lo general es el campo ID de cualquier tabla.\nLuego de indicar a la BBDD qué campo será el campo clave, lo configura como autoincremental.\n\nLa forma de invocarlo sería:\nOBJ.clavePrimaria(campoClave).\n'''
            
            self.mysql_cursor.execute("ALTER TABLE libros ADD PRIMARY KEY (campoClave)");
            self.mysql_cursor.execute("ALTER TABLE libros MODIFY "+campoClave+" AUTO_INCREMENT")
            
      def campoUnico(self, campo):
            '''El método "campoUnico" permite indicar a la base de datos, un campo determinado que contendrá valores únicos e irrepetibles, como el caso del ISBN de un libro o ejemplos similares.\nPor lo general es el campo ID de cualquier tabla.\nLuego de indicar a la BBDD qué campo será el campo clave, lo configura como autoincremental.\n\nLa forma de invocarlo sería:\nOBJ.campoUnico(nombreDelCampo).\n'''
            self.mysql_cursor.execute("ALTER TABLE `libros` ADD UNIQUE INDEX `"+campo+"` (`"+campo+"`);")

      def Ejecutar(self, sql): 
            '''
            \nModo de uso:\nEl método se debe llamar desde el OBJETO del siguiente modo:\n\nOBJ.Ejecutar(cadenaSQL)\nSimplemente ejecuta la sentencia SQL que recibe.\n\nDebido a que existen decenas de variables posibles a ejecutar vía SQL, era mejor para el proyecto dejar abierta esta posibilidad de consultar a la tabla con la sentencia que nos parezca más relevante en lugar de codificar absolutamente todas las variantes.\nLa idea de codificar todas las variantes de consultas de SQL parecía muy atractiva pero dado el tiempo con que contamos decidimos evitarlo, abocándonos a la consigna del proyecto de poder modificar y borrar registros.
            '''
            self.cursor.execute(sql)
            self.conexion.commit()
            
      def InsertarLibro(self, valores):
            '''
            \nModo de uso:\nEl método se debe llamar desde el OBJETO del siguiente modo:\n\nOBJ.InsertarLibro([valores])\nEl parámetro "valores" es una lista conteniendo\nlos valores a guardar en los campos de la tabla.\n\nLa cantidad de valores debe coincidir con la cantidad\nde campos requeridos de la tabla para ser guardados correctamente.\nLa ubicación de los valores, debe coincidir con el orden de los campos en la sentencia SQL INSERT INTO a saber:\n\n01) titulo, 02) autor, 03) disponibilidad, 04) precio, 05) editorial, 06) isbn, 07) paginas, 08) idioma, 09) formato, 10) clasificacion, 11) fechaPub, 12) imagenUrl, 13) libroUrl\n\nEl campo "id" es autoincremental de la tabla y carga el número siguiente por defecto\ny el campo "visible" se carga como 1 (es decir: True) por defecto,\npor lo tanto, estos dos campos no es necesario ingresarlos.\n
            '''
            
            sql = "INSERT INTO `libros`(`titulo`, `autor`, `disponibilidad`, `precio`, `editorial`, `isbn`, `paginas`, `idioma`, `formato`, `clasificacion`, `fechaPub`, `sinopsis`, `imagenUrl`, `libroUrl`) VALUES ("
            p=0
            largo = len(valores)
            if largo == 13:
                  print("\n\nLo siento... \nDebe enviar a la base de datos una lista con los valores de las 14 variables\nnecesarias para cargar el libro en la tabla.\nSólo ha enviado",largo,"de ellas.\n\n")
                  return
            for x in valores:
                  x = str(x)
                  p = p + 1
                  if p == 1:
                        sql = sql+"'"+x+"', "
                  else:
                        if p == largo: # Si es el último campo
                              sql = sql+"'"+x+"')"
                        else:
                              sql = sql+"'"+x+"', "
            self.cursor.execute(sql)
            self.conexion.commit()

      def consultaBio(self, autor):
            '''
            ### METODO consultaBio()
            Modo de uso: Se debe llamar desde el objeto creado del siguiente modo: OBJ.consultaBio(autor) donde "autor" es el valor con el nombre del autor del libro a ser buscado en la tabla biografias de la BBDD para ver si ya está cargada la información de ese autor en particular antes de ser insertada dicha información.
            '''
            sql = "SELECT `autor` FROM `biografias` WHERE `autor` = '"+autor+"'"
            self.cursor.execute(sql)
            resultados = self.cursor.fetchone()
            if resultados == None:
                  return False
            else:
                  return True

      def InsertarBio(self, bio):
            '''
            ### METODO InertarBio()
            \nModo de uso:\nEl método se debe llamar desde el OBJETO del siguiente modo:\n\nOBJ.InsertarBio([biografia])\nEl parámetro "biografia" es una lista con el nombre del autor y el texto de su biografía y sólo se ingresa en la tabla si el autor no existe aún.\n
            '''

            largo = len(bio)
            if not largo == 2:
                  print("\n\nLo siento... \nDebe enviar a la base de datos una lista con los valores 'autor' y 'biografia' para cargarlos en la tabla.\n\n")
                  return
            if bio[1] == '':
                  biog = "No se menciona la biografía de este autor."
            else: 
                  biog = bio[1]
            sql = "INSERT INTO `biografias`(`autor`, `bio`) VALUES ('"+bio[0]+"', '"+biog+"');"
            print("################################")
            print("#### SE INGRESA NUEVO AUTOR ####:")
            print("################################")
            print(sql)
            print("################################")
            self.cursor.execute(sql)
            self.conexion.commit()
                  
      def Borrar(self, nroId):
            '''
            Este método resuelve la eliminación de un registro, aunque sólo de modo virtual (sin quitarlo permanentemente de la BBDD).\nDado lo costoso que resultó el hallazgo de la información, decidimos utilizar un campo "visible" para marcarlo como cero (0) en el caso en que se decida no mostrarlo.\nEventualmente, para otros usos, sería posible recuperarlo, cambiando su estado de "no visible" a "visible".
            '''            
            self.sql = "UPDATE libros SET `visible` = 0 WHERE id = '"+str(nroId)+"';"
            self.cursor.execute(self.sql)
            self.conexion.commit()
      
      def Cambiar(self, cambios):
            '''
            \nModo de uso:\nEl método se debe llamar desde el OBJETO del siguiente modo:\nOBJ.Cambiar([cambios])\n\nEl parámetro "cambios" es una lista que dentro contiene el campo a ser modificado, el nuevo valor de ese campo y el numero de registro que se modificará.\n
            '''
            
            self.sql = "UPDATE libros SET "+cambios[0]+"= '"+cambios[1]+"' WHERE id ="+str(cambios[2])+";" 
            print("Está por enviar la siguiente sentencia a la base de datos para modificarla:")
            print(self.sql)
            print("¿Está realmente seguro de hacer estos cambios?")
            e = input('Para continuar, responda "Si" o cualquier tecla para cancelar:')
            if e == "Si" or e == "Sí":                  
                  self.cursor.execute(self.sql)
                  self.conexion.commit()
                  print("Los cambios se realizaron con éxito!")                  
            else:
                  print("Se omitió el cambio en la base de datos...")
      
      def Ver(self, campos, condicion = ["1"]):
            '''
            \nModo de uso:\nSe llama desde el OBJETO del siguiente modo:\n\nOBJ.Ver(["campo1", "campo2", "campo3"], ["campoCondicional","ValorEsperado"])\n\nEl segundo parámetro es opcional, si no se define, se listarán todos los registros de la tabla.
            '''
            
            self.sql = "SELECT "
            p = 0            
            for x in campos:
                  if p == 0:
                        self.sql = self.sql+x
                        p = 1;
                  else:
                        self.sql = self.sql+", "+x
            if condicion[0] == "1":
                  self.sql = self.sql+" FROM libros WHERE visible AND 1;"
            else:
                  self.sql = self.sql+" FROM libros WHERE visible AND "+condicion[0]+" = "+condicion[1]+";"
            self.cursor.execute(self.sql)
            resultados = self.cursor.fetchall()
            return resultados
            
      def mostrarEliminados(self):
            '''
            Muestra el listado completo de registros virtualmente eliminados.
            '''
            
            self.sql = "SELECT * FROM libros WHERE visible = 1;"
            self.cursor.execute(self.sql)
            resultados = self.cursor.fetchall()
            return resultados
      
      

      def cerrarConexion(self):
            '''
            Este método cierra la conexión a la base de datos.
            '''
            self.cursor.close()
            self.conexion.close()
            