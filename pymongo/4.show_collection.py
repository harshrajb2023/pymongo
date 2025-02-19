import pymongo


if __name__ == "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print("hello")
    print(client)
    
    collect=client['harsh_DB']
    coll_name=collect.list_collection_names()
    print(coll_name)
    
    