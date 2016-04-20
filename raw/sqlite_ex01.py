import sqlite3


conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE person
          (id INTERGER PRIMARY KEY ASC, name VARCHAR(250) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE address
          (id INTERGER PRIMARY KEY ASC,
          street_name VARCHAR(250) NOT NULL,
          street_number VARCHAR(250) NOT NULL,
          post_code VARCHAR(250) NOT NULL,
          person_id INTERGER NOT NULL,
          FOREIGN KEY(person_id) REFERENCES person(id))
          ''')
c.execute('INSERT INTO person VALUES(1, "Ronald Theodoro")')
c.execute('INSERT INTO address VALUES(1, "Rua Maria", "258", "456", 1)')

conn.commit()
conn.close()
