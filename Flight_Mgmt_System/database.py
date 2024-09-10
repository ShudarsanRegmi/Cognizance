# database.py

import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establish a connection to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def disconnect(self):
        """Close the connection to the MySQL database."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

    # def execute_query(self, query, params=None):
    #     """Execute a query and return results."""
    #     if not self.connection or not self.connection.is_connected():
    #         self.connect()
    #     self.cursor.execute(query, params or ())
    #     self.connection.commit()
    #     return self.cursor.fetchall()
    def execute_query(self, query, params=None):
        """Execute a query and return results."""
        if not self.connection or not self.connection.is_connected():
            self.connect()
        
        self.cursor.execute(query, params or ())
        results = self.cursor.fetchall()  # Fetch all results to clear the result set
        
        self.connection.commit()
        return results
    
    def insert_flight(self, flight_number, start, destination, price):
        """Insert a new flight into the flights table."""
        query = """
        INSERT INTO flights (flight_number, start, destination, price)
        VALUES (%s, %s, %s, %s)
        """
        params = (flight_number, start, destination, price)
        self.execute_query(query, params)

    def get_all_flights(self):
        """Fetch all flights from the flights table."""
        query = "SELECT flight_number, start, destination, price FROM flights"
        return self.execute_query(query)
    
    def get_available_flights(self, departure, destination):
        """Fetch available flights based on departure and destination."""
        query = """
        SELECT flight_number, start, destination, price
        FROM flights
        WHERE start = %s AND destination = %s
        """
        params = (departure, destination)
        return self.execute_query(query, params)
    

    def book_flight(self, user_name, flight_number):
        """Book a flight by inserting an entry into the booked_flights table."""
        query = """
        INSERT INTO booked_flights (user_name, flight_number)
        VALUES (%s, %s)
        """
        params = (user_name, flight_number)
        self.execute_query(query, params)



    def get_booked_flights(self, user_name):
        """Fetch the list of booked flights for the user."""
        query = """
            SELECT bf.booking_id, bf.flight_number, f.start, f.destination
            FROM booked_flights bf
            JOIN flights f ON bf.flight_number = f.flight_number
            WHERE bf.user_name = %s
        """
        self.cursor.execute(query, (user_name,))
        return self.cursor.fetchall()

    
    # def delete_flight(self, flight_number):
    #     """Delete a flight from the database based on the flight_number."""
    #     try:
    #         query = "DELETE FROM flights WHERE flight_number = %s"
    #         self.cursor.execute(query, (flight_number,))
    #         self.connection.commit()
    #     except Exception as e:
    #         raise Exception(f"An error occurred while deleting the flight: {str(e)}")


    def delete_flight(self, flight_number):
        """Delete a flight from the database based on the flight_number."""
        try:
            # Prepare the delete query using MySQL's parameter placeholder '%s'
            query = "DELETE FROM flights WHERE flight_number = %s"
            
            # Execute the query with the flight_number as a parameter
            # Ensure the flight_number is treated as a string
            self.cursor.execute(query, (str(flight_number),))
            
            # Commit the transaction
            self.connection.commit()
            
            # Check if any row was affected (i.e., deleted)
            if self.cursor.rowcount == 0:
                raise Exception("No flight found with the given flight number.")
        except Exception as e:
            raise Exception(f"An error occurred while deleting the flight: {str(e)}")

        
    # Add more methods for specific operations as needed
