import psycopg2

conn = psycopg2.connect(database="test", user="postgres", password="123", host="localhost", port="5432")

print ("Opened database successfully")