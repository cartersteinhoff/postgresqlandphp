import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

connection = psycopg2.connect(
    host=config['database']['host'],
    database=config['database']['database'],
    user=config['database']['user'],
    password=config['database']['password']
)

try:
    cursor = connection.cursor()

    # Create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS languages (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    )
    """
    cursor.execute(create_table_query)

    # Insert the placeholder data
    insert_data_query = """
    INSERT INTO languages (name)
    VALUES (%s)
    """
    languages = ['English', 'Japanese', 'French', 'Spanish', 'German', 'Italian', 'Korean', 'Chinese', 'Russian', 'Portuguese']
    for language in languages:
        cursor.execute(insert_data_query, (language,))

    connection.commit()
    print("Table created and data inserted successfully!")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")