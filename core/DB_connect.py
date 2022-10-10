import psycopg2


DATABASE_URL = "postgresql+psycopg2://mvlab:z1x2c3@0.0.0.0:5432/postgres"


def createConnection():
    data = DATABASE_URL.split('://')[1]
    data = data.split(':', 1)
    user = data[0]
    data = data[1].split('@', 1)
    password = data[0]
    data = data[1].split(':', 1)
    host = data[0]
    data = data[1].split('/')
    port = int(data[0])
    dbname = data[1]
    return psycopg2.connect(dbname=dbname, user=user,
                                password=password, host=host,
                                port=port)