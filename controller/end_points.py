from dataclasses import asdict

from flask import Blueprint, request, jsonify

from repository.accident_repo import count_by_region, count_by_region_day, count_by_region_week, count_by_region_month, \
    group_by_main_cause, statistics_by_region
from repository.csv_repository import init_car_accident

end_points = Blueprint('end_points', __name__)


@end_points.route('/initialization', methods=['GET'])
def initialization():
    init_car_accident()
    return jsonify({'status': True})

# Total accidents by region:
@end_points.route('/region/<string:region>', methods=['GET'])
def region(region):
    res = count_by_region(region)
    return jsonify({region: res})

#Total accidents by region and by period
@end_points.route('/region_period/<string:type>/<string:region>', methods=['GET'])
def region_period(type, region):
    period = request.json
    res = None
    if type == 'day':
        res = count_by_region_day(region, period)
    elif type == 'week':
        res = count_by_region_week(region, period)
    elif type == 'month':
        res = count_by_region_month(region, period)

    return jsonify({'region_period': res})

# Accidents are grouped according to the main cause of the accident:
@end_points.route('/main_cause/<string:region>', methods=['GET'])
def main_cause(region):
    res = group_by_main_cause(region)
    return jsonify(res)

# Statistics on injuries by region:
@end_points.route('/injuries/<string:region>', methods=['GET'])
def injuries(region):
    res = statistics_by_region(region)
    return jsonify(res)