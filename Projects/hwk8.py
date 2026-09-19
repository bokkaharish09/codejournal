import pymysql
from prettytable import PrettyTable # for organising table in proper format

def connect_to_database(username, password): #Defining MySQL Connection based on user input credential
    try:
        connection = pymysql.connect(
            host='localhost',
            user=username,
            password=password,
            database='bus_schema_bokkah' #Based on the given SQL Dump
        )
        if connection.open:
            print("Connection to MySQL database established successfully.")
        return connection
    # pymysql exceptions
    except pymysql.OperationalError as e:
        print(f"Operational error: {e}")
    except pymysql.InternalError as e:
        print(f"Internal database error: {e}")
    except pymysql.MySQLError as e:
        print(f"MySQL error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def get_customer_list(connection):   #Generate distinct list of Customer username
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT username FROM customer")
            customers = cursor.fetchall()
            if customers:
                print("\nSelect from these available customer usernames:")
                for username in customers:
                    print(username[0])
            else:
                print("No customer usernames found.")
            return [username[0].lower() for username in customers]
    except pymysql.MySQLError as e:
        print(f"Error retrieving customer list: {e}")
        return []

def get_customer_journeys(connection, customer_name): #Call Procedure for Customer Journeys

    try:
        with connection.cursor() as cursor:
            cursor.execute("CALL get_customer_journeys(%s);", (customer_name,))
            journeys = cursor.fetchall()
            
            table = PrettyTable([    #Table Headers
                "Username", "First Name", "Last Name", "Payment Method", "Seats Booked",
                "Fare Price", "Scheduled Date Time", "Route Instance", "Origin City",
                "Origin State", "Destination City", "Destination State", "Bus Type",
                "Bus Model", "License Plate", "Bus ID"
            ])

            if journeys:
                for row in journeys:
                    table.add_row(row)
                print(table)
            else:
                print("No journeys found for this user.")
    except pymysql.MySQLError as e:
        print(f"Error retrieving journeys: {e}")

def main():
    print(r"""

__        __   _                                  
\ \      / /__| | ___ ___  _ __ ___   ___ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| 

    🌐 Customer Journey Data Fetcher! 🌐

""")
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")

    connection = connect_to_database(username, password)
    if not connection:
        print("Failed to connect to the database. Invalid Username/Password. Exiting application.")
        return

    while True:
        print("\nMAIN MENU:")
        print("\nPlease select an option from the menu below to continue:")
        print("\n1: Generate a list of journeys for a specific user")
        print("2: Disconnect from the database and close the application")
        
        try:
            option = int(input("\nEnter your choice (1 or 2): ").strip())
            if option == 1:
                # print("\nHere are the available customers:")
                
                customer_list = get_customer_list(connection)
                if customer_list:
                    print("\n***Please enter the username exactly as shown from the list above***")
                    select_user = input("\nEnter a customer username from the list displayed: ").strip().lower()
                    if select_user in customer_list:
                        print("\n User details successfully retrieved! Here’s what we found:.")
                        get_customer_journeys(connection, select_user)
                    else:
                        print("\nInvalid username. Please select a username from the displayed list.")
            elif option == 2:
                print("\nDisconnecting from the database... Thank you for using the Customer Journey Management System.")
                connection.close()
                print("Connection closed. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Please enter a valid option (1 or 2).")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
