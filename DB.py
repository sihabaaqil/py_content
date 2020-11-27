import mysql.connector
from mysql.connector import Error


def db_connection(query):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='groptimizeddb',
                                             user='root',
                                             password='rootpwd')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            print("You're connected to database: ", record)
            return record

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def get_url(env, brand, campaign):
    query = "select " + env + "url  from campaign_urls where brand = '" + brand + "' and campaign = '" + campaign + "'"
    print(query)
    query_d = db_connection(query)
    print(query_d.__getitem__(0)[0])
    return query_d.__getitem__(0)[0]


def get_url2():
    query = "select produrl  from campaign_urls"
    print(query)
    query_d = db_connection(query)
    return query_d


def get_cta_locators(env, brand, campaign):
    if (brand == "CrepeErase"):
        query = "select VALUE from cta_locators where brand = '" + brand + "' and campaign = '" + campaign + "'"
        print(query)
        query_d = db_connection(query)
        print(query_d.__getitem__(0)[0])
        return query_d.__getitem__(0)[0]
    elif (brand == "MeaningfulBeauty"):
        query = "select VALUE from cta_locators where brand = '" + brand + "' and campaign = '" + campaign + "'"
        print(query)
        query_d = db_connection(query)
        print(query_d.__getitem__(0)[0])
        return query_d.__getitem__(0)[0]
    else:
        query = "select VALUE from cta_locators where brand = '" + brand + "' and campaign = 'core_full_deluxe20off_pnlfcp'"
        print(query)
        query_d = db_connection(query)
        print(query_d.__getitem__(0)[0])
        return query_d.__getitem__(0)[0]
