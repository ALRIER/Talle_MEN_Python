import mysql.connector
from mysql.connector import Error


def crear_conexion(nombre_host, usuario, contrasena, basedatos):
    conexion = None
    try:
        conexion = mysql.connector.connect(
                host = nombre_host,
                user = usuario,
                passwd = contrasena,
                database = basedatos
                )        
    except Error as e:
        print("Error al establecer conexión: ",e)
    
import mysql.connector
from mysql.connector import Error


def crear_conexion(nombre_host, usuario, contrasena, basedatos):
    conexion = None
    try:
        conexion = mysql.connector.connect(
                host = nombre_host,
                user = usuario,
                passwd = contrasena,
                database = basedatos
                )        
    except Error as e:
        print("Error al establecer conexión: ",e)
    
    return conexion

  

def consulta_registros(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)        
        result = cursor.fetchall()        
        for row in result:
            print(row)
    except Error as e:
         print("Se ha presentado error: ",e)      
    


print(""" 
      
 ¡Bienvenido!
 _  __                         _   _                                           
 | |/ /                        | | | |                                          
 | ' / _  _ _  _ _ _ _  _| | | |     _  _ _ __ _ _  ___             
 |  < / _ \| '_ \| '_/ _` |/ _` | | |    / _ \| '/ _ \ ' \|_  /             
 | . \ () | | | | | | (| | (| | | |_| () | | |  __/ | | |/ /              
 ||\\__/|| |||  \_,|\_,| |__\__/||  \__|| |/__|             
 """)
#colocar datos de conexión
con = crear_conexion('34.122.51.150','alvaroriverae','alvaroriverae','alvaroriverae')
cursor = con.cursor()

continuar = True

while continuar:
    
    print(""" 
              ******
              Menu principal
              ******
          """)
    print("Ingrese una opción:")
    print(""" Visualizar TASA_MATRICULACIÓN_5_16, DESERCIÓN, DESERCIÓN_TRANSICIÓN, DESERCIÓN_PRIMARIA, DESERCIÓN_SECUNDARIA, DESERCIÓN_MEDIA  
              de un departamento y un año determinado
          (1)""")
    print(""" Visualizar los nombres de departamentos y el valor de la deserción de los 5 con mayor deserción en un año determinado.
              El año debe ser ingresado por el usuario
          (2) """)    
    print(""" Crear tabla reportemen con los datos de la vista estmenlatlon_view de un determinado año.
          El año debe ser ingresado por el usuario 
          (R)""")    
    print("Salir (S o s)")
    
    opcion = input("Ingresa una opción: ")
    
    if opcion == "1":
       print("Visualizción de datos de deserción")
       consulta_registros(con,'SELECT ANIO, CODIGO_DEPARTAMENTO, DESERCION FROM estMen2')
       
    elif opcion == "2":
        print("Visualizción 5 departamentos con mayor deserción")
        #Digitar codigo del departamento
        anio = input("digite el año:")
        consulta_registros(con,'SELECT CODIGO_DEPARTAMENTO, DESERCION FROM estMen2 WHERE ANIO = '+"'"+ anio + "'" + 'ORDER BY  DESERCION  DESC LIMIT 5' )
        
    elif opcion == "R" or opcion == "r":
       print("Creando tabla reporte")     
       try:
        
         sql ='DROP TABLE IF EXISTS reporteMEN'        
         cursor.execute(sql)
         sql = """ CREATE TABLE reporteMEN AS
                       SELECT m.ANIO,
                        m.CODIGO_DEPARTAMENTO,
                        m.DEPARTAMENTO,
                        m.POBLACION_5_16,
                        m.TASA_MATRICULACION_5_16,
                        m.COBERTURA_NETA,
                        m.COBERTURA_NETA_TRANSICION,	
                        m.COBERTURA_NETA_PRIMARIA,	   
                        m.COBERTURA_NETA_SECUNDARIA,   
                        m.COBERTURA_NETA_MEDIA,      
                        m.COBERTURA_BRUTA,          
                        m.COBERTURA_BRUTA_TRANSICION,     
                        m.COBERTURA_BRUTA_PRIMARIA,      
                        m.COBERTURA_BRUTA_SECUNDARIA,    
                        m.COBERTURA_BRUTA_MEDIA,    
                        m.TAMAÑO_PROMEDIO_DE_GRUPO,     
                        m.SEDES_CONECTADAS_A_INTERNET,      
                        m.DESERCION,     
                        m.DESERCION_TRANSICION,  
                        m.DESERCION_PRIMARIA,     
                        m.DESERCION_SECUNDARIA,     
                        m.DESERCION_MEDIA,     
                        m.APROBACION,     
                        m.APROBACION_TRANSICION,     
                        m.APROBACION_PRIMARIA,    
                        m.APROBACION_SECUNDARIA,      
                        m.APROBACION_MEDIA,     
                        m.REPROBACION,      
                        m.REPROBACION_TRANSICION,     
                        m.REPROBACION_PRIMARIA,    
                        m.REPROBACION_SECUNDARIA,    
                        m.REPROBACION_MEDIA,      
                        m.REPITENCIA,     
                        m.REPITENCIA_TRANSICION,    
                        m.REPITENCIA_PRIMARIA,     
                        m.REPITENCIA_SECUNDARIA,   
                        m.REPITENCIA_MEDIA,      
                        p.latitud, 
                        p.longitud
                        FROM estMen2 m inner join
                        posDept p
                        on m.CODIGO_DEPARTAMENTO = p.codigo_departamento
                        ;"""
         cursor.execute(sql)
         con.commit()
         print("Tabla reporte creada satisfactoriamente")
         
       except Error as e:
        print("Se ha presentado error: ",e)
        
       
       
    elif opcion == "S" or opcion == "s":
        continuar = False
    else:
        print("""
              
        Opción incorrecta, intente nuevamente
              
        """)
    
print("""
      ¡Hasta pronto!
 _  __                         _   _                                           
 | |/ /                        | | | |                                          
 | ' / _  _ _  _ _ _ _  _| | | |     _  _ _ __ _ _  ___             
 |  < / _ \| '_ \| '_/ _` |/ _` | | |    / _ \| '/ _ \ ' \|_  /             
 | . \ () | | | | | | (| | (| | | |_| () | | |  __/ | | |/ /              
 ||\\__/|| |||  \_,|\_,| |__\__/||  \__|| |/__|             
 """)

        
con.close()        

# Crear informe en google datastudio con los datos de la tabla reporte que visualice:
# Producción por municipio
# Producción por tipo de cultivo
# El rendimiento por tipo de cultivo
# Tabla con el nombre del municipio, nombre del cultivo
