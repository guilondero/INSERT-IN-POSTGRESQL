import psycopg2 


def insert_postgress():

#Establishing the connection
    conn = psycopg2.connect(database=" ", user=' ', password=' ', host=' ', port= ' ')

#Setting auto commit false
    conn.autocommit = True

# Preparing SQL queries to INSERT a record into the database.
    query = "INSERT INTO track (id, value1, value2) VALUES (%s, %s, %s);"
    data = (id, value1, value2)

    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    conn.close()
