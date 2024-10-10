from dataclasses import asdict

from flask import Blueprint, request, jsonify

from repository.accident_repo import count_by_region
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

# #Total accidents by region and by period
# @end_points.route('/region_period/<string:region>/<string:period>', methods=['GET'])
#
# # Accidents are grouped according to the main cause of the accident:
# @end_points.route('/main_cause/<string:main_cause', methods=['GET'])
#
# # Statistics on injuries by region:
# @end_points.route('/injuries/<string:region>', methods=['GET'])