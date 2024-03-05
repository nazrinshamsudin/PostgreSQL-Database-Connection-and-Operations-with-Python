import psycopg2

hostname = 'localhost'
database = 'demo'
username = 'postgres'
password = 'postgres'
port_id = '5432'
conn = None
cur = None


try:
    conn = psycopg2.connect(   
                    host = hostname, 
                    dbname = database,
                    user = username,
                    password = password,
                    port =  port_id )

    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS employee')
    create_script = ''' CREATE TABLE IF NOT EXISTS employee ( 
                        id      int PRIMARY KEY,
                        name    varchar(40) NOT NULL,
                        salary  int, 
                        dept_id varchar(30)
    )
'''
    cur.execute(create_script)

    insert_script = 'INSERT INTO EMPLOYEE(id, name, salary, dept_id) VALUES(%s, %s, %s, %s)'
    insert_value = [(1, 'Nazrin', 2000, 'D1'), (2, 'Akid', 2500, 'D2'),(3, 'Amirah', 4000, 'D1'), (4, 'Ridhwan', 5000, 'D3')  ]
    for record in insert_value:
        cur.execute(insert_script,record)

    update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)

    # delete_script = 'DELETE FROM EMPLOYEE WHERE name= %s'
    # delete_record = ('Nazrin', )
    # cur.execute(delete_script, delete_record)


    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record)


        
    

    


    conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()