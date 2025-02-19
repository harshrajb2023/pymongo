import pymongo


if __name__ == "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print("hello")
    print(client)
    db=client['harsh_DB']
    collection=db['raj_collection']
    # # bydefault
    # one =collection.find_one()
    # print(one)
    
    # one =collection.find_one({'name':'harsh1'})
    # print(one)
    # result = collection.find_one({"name": "harsh"})
    # print(result) 
    
    # one =collection.find_one({"name":"Harsh1"})
    # print('one : ',one)
    
    # #  not print 
    # all_doc=collection.find({"name": "harsh"})
    # print('all_doc',all_doc)
    
    # all_doc=collection.find({"name": "harsh"})
    # for item in all_doc:
    #      print(item)
         
    #     # include name (show name) , and exclude id(not show id)
    # all_doc=collection.find({"name": "harsh"},{"name":1, "_id":0})
    # for item in all_doc:
    #      print(item)
    
    
    # all_doc=collection.find({"name": "harsh"},{"name":0, "_id":0})
    # for item in all_doc:
    #      print(item)
    
    # # othe than name -- show hoga
    # all_doc=collection.find({"name": "harsh"},{"name":0})
    # for item in all_doc:
    #      print(item)
    
    # # add display limited data
    # all_doc=collection.find({"name": "harsh"},{"name":0}).limit(2)
    # for item in all_doc:
    #      print(item)
    
    
    # # other name --- not show
    # all_doc=collection.find({"name": "harsh"},{"name":1})
    # print('count list of data ',all_doc.count())
    # for item in all_doc:
    #      print(item)
    
    # less than equal
    all_doc=collection.find({"name": "David", "age": {"$lte": 30}})
    print(all_doc.count())
    for item in all_doc:
         print(item)