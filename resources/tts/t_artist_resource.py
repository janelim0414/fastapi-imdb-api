from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig
from resources.imdb_resources.artist_resource import ArtistResource
import json
from service_factory import ServiceFactory

service_factory = ServiceFactory()
artist_resource = service_factory.get_resource("ArtistResource")


def t1():

    a_resource = artist_resource
    result = a_resource.get_by_key("nm038969")
    print("t1: result = \n", json.dumps(result.dict(), indent=2))

def t2():

    a_resource = artist_resource
    result = a_resource.get(birthYear='1976')
    print("t2: result = \n")
    for entry in result:
        print(json.dumps(entry.dict(), indent=2))

def t3():
    a_resource = artist_resource
    result = a_resource.delete(primaryName='Susie Kelly')
    print("t3: result = \n", result, "row(s) affected")

def t4():
    a_resource = artist_resource
    result = a_resource.update(primaryName='Matteo Elezi', newValues={"primaryName": "Jane Lim"})
    print("t4: result = \n", result, "row(s) affected")

def t5():
    a_resource = artist_resource
    result = a_resource.post(newValues={"nconst": "nm000002", "primaryName": "Donald Ferguson"})
    print("t5: result = \n", result)

if __name__ == "__main__":
    # t1()
     t2()
    # t3()
    # t4()
    # t5()
