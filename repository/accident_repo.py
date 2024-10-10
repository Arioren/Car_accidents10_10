from database.connect import my_collection


def count_by_region(region):
    return my_collection.count_documents({'region': region})