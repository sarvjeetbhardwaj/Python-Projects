import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient(<connection_link given by mongo db>,tlsCAFile=ca)

db1 = client['testdb'] # creating database with name testdb
c1=db1['firstable'] #creating table in the database

dict1={
    'name' : 'sarvjeet',
    'email' : 'sjitbh121993@gmail.com',
    'product' : ['onemuron', 123,'kids', '9098756'],
     'company' : 'Ameriprise'
}

dict2={
    'name' : 'sarvjeet',
    'email' : 'sjitbh121993@gmail.com',
    'product' : ['onemuron', 123,'kids', '9098756'],
     'company' : 'Ameriprise',
    'phone_number' : '89373648484938392'

}

l1=   [
     {  'item': 'lamp', 'qty': 50, 'type': 'desk' },
     {  'item': 'lamp', 'qty': 20, 'type': 'floor' },
     { 'item': 'bulk', 'qty': 100 }
   ]

c1.insert_one(dict2)
c1.insert_many(l1) #data should be inthe form of dictionary in list


#to fetch  all the data in a table
#for i in c1.find():
#    print(i)

#for i in c1.find({'name':'sarvjeet'}):
    #print(i)

#for i in c1.find({'name': {'$in':['sarvjeet','kids']},'email_id' : 'sjitbh121993@gmail.com'}):
    #print(i)

c1.find_one()

c1.find({'qty':{'$gt':25}}) #find recoreds where quantity is greater than 25
c1.find({'qty':{'$lt':25}}) #find recoreds where quantity is less than 25
c1.find({'qty':{'$lte':25}}) ##find recoreds where quantity is less than or equal to 25
c1.find({'qty':{'$gte':25}}) #find recoreds where quantity is greater than 25

c1.update_many({'name': 'sarvjeet'},{'$set':{'name': 'sarvjeet bhardwaj'}}) #to update the records

#for i in c1.find().limit(3): #first 3 records
    #print(i)

#for i in c1.find({'qty': {'$not': {'$gt':100}}}): # not greater than
    #print(i)

#for i in c1.find({'qty': {'$not': {'$lt':100}}}): # not lesser than
    #print(i)

#c1.find_one_and_update({'item': 'lamp'},{'$set':{'qty':250}})

#for i in c1.find({'item':'lamp'}):
    #print(i)


#c1.update_many({'qty':{'$gt':20}},{'$set':{'qty': 200}})

#for i in c1.find({'item': 'lamp'}):
   # print(i)

c1.delete_many({'name':'sarvjeet'})

for i in c1.find({'name':'sarvjeet'}):
    print(i)

#print(client.list_database_names())