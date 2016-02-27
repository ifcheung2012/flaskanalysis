__author__ = 'IfCheung'
from flask import jsonify
from models import *
from . import api


@api.route('/lott/api/v1.0/douballs/top/<int:count>')
def get_douball_list(count):
    result = Doublechrom.get_top_list(count)
    lastlist = result.tolist()
    print(type(result))
    return jsonify({'the top ' + str(count): str(lastlist), 'and ordered': str(sorted(lastlist))})


@api.route('/lott/api/v1.0/douballs/random/<int:count>')
def get_douball_random(count):
    result = Doublechrom.get_random_list(count)
    print(type(result))
    return jsonify({'return random result': str(result)})









