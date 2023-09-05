import psycopg2
from config import DATABASE

class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def create_table(self):
        try:
            connection = psycopg2.connect(**DATABASE)
            cursor = connection.cursor()

            create_table_query = """
                CREATE TABLE IF NOT EXISTS login_details (
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """
            cursor.execute(create_table_query)
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def user_exists(self):
        try:
            connection = psycopg2.connect(**DATABASE)
            cursor = connection.cursor()

            check_user_query = "SELECT id FROM login_details WHERE email = %s"
            cursor.execute(check_user_query, (self.email,))
            user_id = cursor.fetchone()

            return user_id is not None

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

        
    def save(self):
        if not self.user_exists():
            try:
                connection = psycopg2.connect(**DATABASE)
                cursor = connection.cursor()

                insert_query = """
                    INSERT INTO login_details (email, name, password) VALUES (%s, %s, %s)
                """
                cursor.execute(insert_query, (self.email, self.name, self.password))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()

    def verify_password(self, password):
        try:
            connection = psycopg2.connect(**DATABASE)
            cursor = connection.cursor()

            verify_query = "SELECT id FROM login_details WHERE email = %s AND password = %s"
            cursor.execute(verify_query, (self.email, password))
            user_id = cursor.fetchone()

            return user_id is not None

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = psycopg2.connect(**DATABASE)
            cursor = connection.cursor()
            delete_query = "DELETE FROM login_details WHERE email = %s"
            cursor.execute(delete_query, (self.email,))
            connection.commit()
            
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

class Profile:
    def __init__(self,emp_id,name, email, gender, designation, experience, tools, area_of_interest):
        self.emp_id = emp_id
        self.name= name
        self.email = email
        self.gender = gender
        self.designation = designation
        self.experience = experience
        self.tools = tools
        self.area_of_interest = area_of_interest

    def create_profile_table(self):
        connection = psycopg2.connect(**DATABASE)
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS profile_details
                               (id SERIAL PRIMARY KEY,
                                emp_id VARCHAR NOT NULL,
                                email VARCHAR NOT NULL,
                                name VARCHAR NOT NULL,
                                gender VARCHAR NOT NULL,
                                designation VARCHAR NOT NULL,
                                experience INTEGER NOT NULL,
                                tools TEXT NOT NULL,
                                area_of_interest TEXT NOT NULL);'''
        cursor.execute(create_table_query)
        connection.commit()
        connection.close()

    def save_profile(self):
        try:
            connection = psycopg2.connect(**DATABASE)
            cursor = connection.cursor()

            # Check if a profile with the email already exists in the database
            check_profile_query = "SELECT email FROM profile_details WHERE email = %s"
            cursor.execute(check_profile_query, (self.email,))
            existing_email = cursor.fetchone()

            if existing_email:
                # Update the existing profile
                update_query = '''
                    UPDATE profile_details
                    SET emp_id = %s, name = %s, gender = %s, designation = %s,
                        experience = %s, tools = %s, area_of_interest = %s
                    WHERE email = %s
                '''
                data = (self.emp_id, self.name, self.gender, self.designation,
                        self.experience, self.tools, self.area_of_interest, self.email)
                cursor.execute(update_query, data)
            else:
                # Check if the email exists in the login_details table
                user = User(self.email, None, None)
                if user.user_exists():
                    # Insert a new profile record
                    insert_query = '''
                        INSERT INTO profile_details 
                        (emp_id, name, email, gender, designation, experience, tools, area_of_interest) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    '''
                    data = (self.emp_id, self.name, self.email, self.gender,
                            self.designation, self.experience, self.tools, self.area_of_interest)
                    cursor.execute(insert_query, data)
                else:
                    # User does not exist in login_details table
                    return "User with this email does not exist. Please register first."

            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def perform_search(query):
        connection = psycopg2.connect(**DATABASE)
        cursor = connection.cursor()

        # Search for profiles based on the query (emp_id, name, tools, or area_of_interest)
        search_query = f"%{query}%"  # Use % as a wildcard for partial matches
        search_query = search_query.lower()  # Convert the query to lowercase for case-insensitive search

        # Query to search for profiles with emp_id, name, tools, or area_of_interest matching the query
        search_profiles_query = '''SELECT emp_id, email, name, gender, designation, experience, tools, area_of_interest
                                    FROM profile_details
                                    WHERE lower(emp_id) LIKE %s
                                    OR lower(email) LIKE %s
                                    OR lower(name) LIKE %s
                                    OR lower(gender) LIKE %s
                                    OR lower(designation) LIKE %s
                                    OR experience::text LIKE %s
                                    OR lower(tools) LIKE %s
                                    OR lower(area_of_interest) LIKE %s;'''

        data = (
            search_query,
            search_query,
            search_query,
            search_query,
            search_query,
            search_query,
            search_query,
            search_query,
        )
        cursor.execute(search_profiles_query, data)
        profiles = cursor.fetchall()

        connection.close()
        return profiles
    

    def delete(self):
        try:
            connection = psycopg2.connect(**DATABASE)
            cursor = connection.cursor()

            delete_query = "DELETE FROM profile_details WHERE email = %s"
            cursor.execute(delete_query, (self.email,))
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


    @staticmethod
    def execute_query(query):
        try:
            connection = psycopg2.connect(**DATABASE)
            cursor = connection.cursor()

            cursor.execute(query)
            results = cursor.fetchall()

            connection.close()
            return results

        except (Exception, psycopg2.Error) as error:
            print("Error while executing the query:", error)
            return None