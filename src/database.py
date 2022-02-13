import sqlite3
from sqlite3 import Error
from os.path import exists
import os
from csv import reader


class Database():

    def __init__(self):
        self.connection = self.sql_connection(name="warmup.db")

        # Check if table exists, if not create it
        # Ripped from https://pythonexamples.org/python-sqlite3-check-if-table-exists/
        c = self.connection.cursor()


    def load_external_cities(self):
        
        with open('data/cities.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header != None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    #print(row)
                    self.insert_cities(row[0],row[1],row[2],row[3],row[4])
                    print("inserted")

        read_obj.close()

    def load_external_pop2020(self):
        
        with open('data/pop2020.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header != None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    #print(row)
                    self.insert_pop2020(row[0],row[1],row[2],row[3],row[4], row[5])
                    print("inserted")
                    
        read_obj.close()

    def sql_connection(self, name='warmup.db'):
        try:
            connection = sqlite3.connect(name, check_same_thread=False)
            #print('database connected')
            return connection
        except Error:
            print(Error)

    def create_table(self):
        cursorObj = self.connection.cursor()
        try:
            cursorObj.execute("CREATE TABLE cities( id TEXT, city TEXT, lat TEXT, lng TEXT, population TEXT)")
            cursorObj.execute("CREATE TABLE countries( id TEXT, country TEXT, population TEXT, urbanPop TEXT, worldShare TEXT, capital TEXT)")

            self.connection.commit()

        except Error:
            print('create_table:', Error)

    def insert_cities(self, id, cities, lat, lng, population):
        sql = 'INSERT INTO cities (id,city,lat,lng,population) VALUES (?,?,?,?,?)'
        cur = self.connection.cursor()
        cur.execute(sql, (id,cities,lat,lng,population))
        #print("Inserted")
        self.connection.commit()

    def insert_pop2020(self,id, country, population, urbanPop, worldShare, capital):
        sql = 'INSERT INTO countries (id, country, population, urbanPop, worldShare, capital) VALUES (?,?,?,?,?,?)'
        cur = self.connection.cursor()
        cur.execute(sql, (id,country, population, urbanPop, worldShare, capital))
        #print("Inserted")
        self.connection.commit()

    def return_Data(self, query):
        
        conn = sqlite3.connect('warmup.db')
        cur = self.connection.cursor()
       
        
        with conn:
            cur.execute(query)
            output = cur.fetchall()

        self.connection.commit()
        return output
        
    def load_data(self):
        self.connection = self.sql_connection(name="warmup.db")
        c = self.connection.cursor()

        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='cities' ''')
        if c.fetchone()[0] == 1:
            print('Table exists.')
        else:
            self.create_table()
            self.sql_connection()
            self.load_external_cities()
            self.load_external_pop2020()


db = Database()


