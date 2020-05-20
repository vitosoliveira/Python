import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=LAPTOP-RRDL1VEO;'
                        'Database=TREINO;'
                        'Trusted_Connection=yes;'


)       

cursor = conn.cursor

cursor.execute (
    """ 
        CREATE TABLE dedidnho (
            NOME VARCHAR (50)

        )
     
    """
)

cursor.commit()