from datetime import datetime, timedelta, date

from database.connect import my_collection, days_sum, month_sum


def count_by_region(region):
    return my_collection.count_documents({'region': region})

def count_by_region_day(region, period):
    period = datetime(year=period['year'], month=period['month'], day=period['day'])
    res = days_sum.find_one({'region': region, 'date': period})
    return 0 if res is None else res['count']

def count_by_region_week(region, period):
    start = datetime(year=period['year'], month=period['month'], day=period['day'])
    end = start + timedelta(days=6)
    try:
        return sum(x['count'] for x in list(days_sum.find({'region': region, 'date': {'$gte': start, '$lte': end}})))
    except Exception:
        return 0

def count_by_region_month(region, period):
    res = month_sum.find_one({'region': region, 'date':period})
    return 0 if res is None else res['count']
