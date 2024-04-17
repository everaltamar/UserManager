from flask import jsonify, make_response


def make_error_response(message, status_code=500):
    response = {
        'message': message,
        'status': 'False',
    }
    return make_response(jsonify(response), status_code)

def make_error_validate_response(message, status_code=400):
    response = {
        'message': message,
        'status': 'False',
    }
    return make_response(jsonify(response), status_code)

def make_response_create_success(message, data=None, status_code=201):
    response = {
        'message': message,
        'status': 'True',
    }
    if data:
        response['users'] = data
    return make_response(jsonify(response), status_code)

def make_response_ok_success(message, data=None, status_code=200):
    response = {
        'message': message,
        'status': 'True',
    }
    if data:
        response['users'] = data
    return make_response(jsonify(response), status_code)