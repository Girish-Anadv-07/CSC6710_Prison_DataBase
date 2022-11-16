import psycopg2

conn = psycopg2.connect(
    database="Prison_DataBase", user='postgres', password='trewq', host='127.0.0.1', port= '5432'
    )
