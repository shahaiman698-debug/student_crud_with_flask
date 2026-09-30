from flask import Flask, jsonify, request

app = Flask(__name__)
students=[
    {"id":1,"name":"shah aiman","age":21},
    {"id":2,"name":"khan alfiya","age":24},
    {"id":3,"name":"shaikh shifa","age":23},
    {"id":4,"name":"shah faizan","age":18},
    ] 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#to get the all the details(read)
@app.route("/students",methods=["GET"])
def get_all_students():
  return jsonify(students)

#to get the details from the specific user(read)
@app.route("/students/<int:student_id>",methods=["GET"])
def get_student(student_id):
  for student_details in students:
    if student_details["id"]==student_id:
      return student_details
  return "Student not found"

# to add the student details(update)
@app.route("/students",methods=["POST"]) 
def add_student():
  students_details=request.get_json()
  print("Student details",students_details)
  new_student_id=students[-1]["id"]+1
  students_details["id"]=new_student_id
  students.append(students_details)
  return "successfully added"   


#to add data (put)
@app.route("/students/<int:student_id>",methods=["PUT"])
def update_student(student_id):
    #to get the data from the body in postman
    update_student_details=request.get_json()
    for student_details in students:
        if student_details["id"]==student_id:
            if update_student_details.get("name"):
                student_details["name"]=update_student_details.get("name")
            if update_student_details.get("age"):
                student_details["age"]=update_student_details.get("age")
            return "Successfully updated"
    return "Student not found"

@app.route("/students/<int:student_id>",methods=["DELETE"])
def delete_student(student_id):
    for student_details in students:
        if student_details["id"]==student_id:
            students.remove(student_details)
            return "Successfully deleted"
    return "Student not found"




if __name__=="__main__":
    app.run(debug=True)
