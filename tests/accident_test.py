import pytest
from repository.accident_repo import count_by_region, count_by_region_day, count_by_region_week, count_by_region_month, \
    group_by_main_cause, statistics_by_region

def test_test_count_by_region():
    res = count_by_region('1834')
    assert res >= 0

def test_count_by_region_day():
    res = count_by_region_day('1834', {'year': 2020, 'month': 1, 'day': 1})
    assert res >= 0

def test_count_by_region_week():
    res = count_by_region_week('1834', {'year': 2020, 'month': 1, 'day': 1})
    assert res >= 0

def test_count_by_region_month():
    res = count_by_region_month('1834', {'year': 2020, 'month': 1})
    assert res >= 0

def test_group_by_main_cause():
    res = group_by_main_cause('1834')
    assert len(res) >= 0
    assert '_id' in res[0]
    assert 'count' in res[0]
    assert 'total injury' in res[0]
    assert 'fatal' in res[0]

def test_statistics_by_region():
    res = statistics_by_region('1834')
    assert len(res) >= 0
    assert '_id' in res[0]
    assert 'all accidents' in res[0]
    assert 'fatal' in res[0]
    assert 'non_fatal' in res[0]
    assert 'total injury' in res[0]
    assert len(res[0]['all accidents']) >= 0



