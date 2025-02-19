import pymongo


if __name__ == "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print("hello")
    print(client)
    db=client['harsh_DB']
    collection=db['raj_collection']
    
    # # update_one , only one update 
    # prev={"name":"David"}
    # # nextt={"city":"kanpur"}
    # nextt={"$set":{"city": "kanpur"}}
    # collection.update_one(prev,nextt)
    
    # # update_many
    # prev={"name":"harsh"}
    # nextt={"$set":{"city": "mirzapur"}}
    # collection.update_many(prev,nextt)
    
    # # find modify items
    prev={"name":"harsh"}
    nextt={"$set":{"city": "mzp"}}
    Modify_items= collection.update_many(prev,nextt)
    print(Modify_items.modified_count)
 