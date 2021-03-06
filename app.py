import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import os

APPOINTMENTS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Patient 1',
        'time': "15:00",
        'email': 'test@test.com',
        'doctor': 'Dr Sachin',
        'date': '5/10/2020'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Patient 1',
        'time': "15:00",
        'email': 'test2@test.com',
        'doctor': 'Dr Manuel',
        'date': '5/10/2020'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Patient 1',
        'time': "15:00",
        'email': 'test3@test.com',
        'doctor': 'Dr Nidhi',
        'date': '5/10/2020'
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
#app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_appointment(appointment_id):
    for appointment in APPOINTMENTS:
        if appointment['id'] == appointment_id:
            APPOINTMENTS.remove(appointment)
            return True
    return False


@app.route('/appointments', methods=['GET', 'POST'])
def all_appointments():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        APPOINTMENTS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'time': post_data.get('time'),
            'email': post_data.get('email'),
            'doctor': post_data.get('doctor'),
            'date': post_data.get('date')
            
        })
        response_object['message'] = 'Appointment added!'
    else:
        response_object['appointments'] = APPOINTMENTS
    return jsonify(response_object)


@app.route('/appointments/<appointment_id>', methods=['PUT', 'DELETE'])
def single_appointment(appointment_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_appointment(appointment_id)
        APPOINTMENTS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'time': post_data.get('time'),
            'email': post_data.get('email'),
            'doctor': post_data.get('doctor'),
            'date': post_data.get('date')
        })
        response_object['message'] = 'Appointment updated!'
    if request.method == 'DELETE':
        remove_appointment(appointment_id)
        response_object['message'] = 'Appointment removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')

'''if __name__ == '__main__':
    app.run()'''