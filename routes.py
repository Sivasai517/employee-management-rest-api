from flask import request, jsonify
from models import db, Employee

def register_routes(app):

    @app.route('/')
    def home():
        return "Employee Management API is Running!"

    @app.route('/employee', methods=['POST'])
    def add_employee():
        data = request.get_json()

        employee = Employee(
            name=data["name"],
            department=data["department"],
            salary=data["salary"]
        )

        db.session.add(employee)
        db.session.commit()

        return jsonify({
            "message": "Employee added successfully!",
            "id": employee.id
        }), 201

    @app.route('/employees', methods=['GET'])
    def get_employees():

        employees = Employee.query.all()

        employee_list = []

        for emp in employees:
            employee_list.append({
                "id": emp.id,
                "name": emp.name,
                "department": emp.department,
                "salary": emp.salary
            })

        return jsonify(employee_list)

    @app.route('/employee/<int:id>', methods=['GET'])
    def get_employee(id):

        employee = db.session.get(Employee, id)

        if employee is None:
            return jsonify({"message": "Employee not found"}), 404

        return jsonify({
            "id": employee.id,
            "name": employee.name,
            "department": employee.department,
            "salary": employee.salary
        })

    @app.route('/employee/<int:id>', methods=['PUT'])
    def update_employee(id):

        employee = db.session.get(Employee, id)

        if employee is None:
            return jsonify({"message": "Employee not found"}), 404

        data = request.get_json()

        employee.name = data["name"]
        employee.department = data["department"]
        employee.salary = data["salary"]

        db.session.commit()

        return jsonify({
            "message": "Employee updated successfully!"
        })

    @app.route('/employee/<int:id>', methods=['DELETE'])
    def delete_employee(id):

        employee = db.session.get(Employee, id)

        if employee is None:
            return jsonify({"message": "Employee not found"}), 404

        db.session.delete(employee)
        db.session.commit()

        return jsonify({
            "message": "Employee deleted successfully!"
        })