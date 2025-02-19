import pymongo


if __name__ == "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print("hello")
    print(client)
    db=client['harsh_DB']
    collection=db['raj_collection']

    documents = [
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"},
    {"name": "David", "age": 35, "city": "Houston"}
    ]
    collection.insert_many(documents)