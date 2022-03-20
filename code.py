import psycopg2 


def insert_postgress():

#Establishing the connection
    conn = psycopg2.connect(database=" ", user=' ', password=' ', host=' ', port= ' ')

#Setting auto commit false
    conn.autocommit = True

# Preparing SQL queries to INSERT a record into the database.
    query = "INSERT INTO track (id, data, datasys, longitude, latitude, odometro, velocidade,ignicao, rpm, transparent_data, ibutton, dir, in1, out1, out2,  gps, gprs, horimetro, voltagem, temperatura, contador, motivo, package_) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    data = (unique_id, gps_utc_time, datasys, longitude, latitude, odometro, speed, ignicao, rpm,
     transparent_data, rfid, azimuth, in1, out1, out2, gps_accuracy, gprs, horimetro,
      external_power_supply_voltage, temp, count_number, motivo, package_)

    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    conn.close()
