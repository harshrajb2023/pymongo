import pymongo


if __name__ == "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print("hello")
    print(client)
    db=client['harsh_DB']
    collection=db['raj_collection']
    
    # delete_one
    # record={"name":"Bob"}
    # collection.delete_one(record)
    
    # delete_many
    record={"name":"Charlie"}
    delete_items= collection.delete_many(record)
    print(delete_items.deleted_count)