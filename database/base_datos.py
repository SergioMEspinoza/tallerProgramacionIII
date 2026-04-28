import psycopg2
# patron singleton
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creando conexión única a PostgreSQL...")

            cls._instance = super(Database, cls).__new__(cls)

            cls._instance.connection = psycopg2.connect(
                host="localhost",
                database="clinica",
                user="postgres",
                password="megagus123",
                port="5432"
            )

        return cls._instance

    def get_connection(self):
        return self.connection