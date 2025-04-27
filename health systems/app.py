from flask import Flask, jsonify
from system import HealthSystem

app = Flask(__name__)
health_system = HealthSystem()

health_system.create_program("TB")
health_system.create_program("Malaria")
health_system.create_program("HIV")
health_system.register_client("C001", "Kelvin Alianda", 30)
health_system.register_client("C002", "Sandra Jannel", 25)
health_system.register_client("C003", "Rollins Maloba", 25)
health_system.enroll_client_in_program("C001", "TB")
health_system.enroll_client_in_program("C002", "Malaria")
health_system.enroll_client_in_program("C003", "HIV")

@app.route('/api/client/<client_id>', methods=['GET'])
def get_client_profile(client_id):
    profile = health_system.get_client_profile(client_id)
    if profile:
        return jsonify(profile), 200
    else:
        return jsonify({"error": "Client not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
