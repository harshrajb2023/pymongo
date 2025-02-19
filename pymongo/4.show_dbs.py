import pymongo


if __name__ == "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print("hello")
    print(client)
    
    # find all database name
    list_dbs= client.list_database_names()
    print(list_dbs)
   

