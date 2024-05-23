from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig


def get_svc() -> MySQLDataService:
    config = MySQLDataServiceConfig()
    svc = MySQLDataService(config)
    return svc


def t1():
    get_svc()


def t_where_clause():
    predicate = {"nameLast": "Williams", "nameFirst": "Ted", "H": 72}
    svc = get_svc()
    res, args = svc.predicate_to_where_clause_args(predicate)
    print("t_where_clause: clause=", res, "args=", args)


def t_build_sql():
    predicate = {"nameLast": "Williams", "nameFirst": "Ted"}
    svc = get_svc()
    res = svc.build_select("lahmansbaseballdb", "people",
                                 predicate,
                                 ["nameLast", "nameFirst", "birthCity"])
    print("t_build_sql: clause=", res)

def t_build_delete():
    predicate = {"primaryName": "Tom Hanks", "birthYear": 1960}
    svc = get_svc()
    res = svc.build_delete("s23_w4111_hw2_jl6094", "name_basics_all",
                                 predicate)
    print("t_build_delete: clause=", res)

def t_build_update():
    predicate = {"primaryName": "Tom Hanks", "birthYear": 1960}
    new = {"primaryName": "Jane Lim", "birthYear": 2001}
    svc = get_svc()
    res = svc.build_update("s23_w4111_hw2_jl6094", "name_basics_all",
                                 predicate, new)
    print("t_build_update: clause=", res)

def t_build_insert():
    new = {"primaryName": "Jane Lim", "birthYear": 2001}
    svc = get_svc()
    res = svc.build_insert("s23_w4111_hw2_jl6094", "name_basics_all",
                                 new)
    print("t_build_insert: clause=", res)



if __name__ == "__main__":
    t_build_sql()
    t_build_delete()
    t_build_update()
    t_build_insert()
