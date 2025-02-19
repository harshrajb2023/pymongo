# import pymongo
# import pymongo.mongo_client

# if __name__ == "__main__":
#     client=pymongo.MongoClient("mongodb://localhost:27017/")
#     print("hello")
#     print(client)
#     db=client['harsh_DB']
#     collection=db['raj_collection']




import pymongo

if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Connected to MongoDB:", client)

    # Create database and collection
    db = client['harsh_DB']
    collection = db['raj_collection']

    # # Insert a sample document to create the collection
    # sample_document = {"name": "Harsh", "message": "Hello from MongoDB!"}
    # collection.insert_one(sample_document)
    
    # sample_document = {"name": "Harsh1", "message": "Hello from MongoDB!" , "marks":24}
    # collection.insert_one(sample_document)
    
    #insert_many
    documents = [
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"},
    {"name": "David", "age": 35, "city": "Houston"}
    ]
    # add id , not use bydefault
    documents = [
    { "_id":1, "name": "Bob", "age": 25, "city": "Los Angeles"},
    { "_id":2,"name": "Charlie", "age": 28, "city": "Chicago"},
    { "_id":3,"name": "David", "age": 35, "city": "Houston"}
    ]
    collection.insert_many(documents)

    print("Database and collection created with a sample document.")
