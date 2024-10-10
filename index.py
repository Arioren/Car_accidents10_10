from database.connect import my_collection


def show_thw_power_of_index():
    res = my_collection.find({"region": "1834"}).explain()["executionStats"]
    print(res)

    my_collection.create_index([("region", 1)])
    res = my_collection.find({"region": "1834"}).explain()["executionStats"]
    print(res)

    my_collection.drop_index("region_1")

show_thw_power_of_index()
