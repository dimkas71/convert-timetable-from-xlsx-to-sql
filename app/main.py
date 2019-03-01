from flask import Flask
import flask_sqlalchemy 
import flask_restless

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orange2.db'

db =flask_sqlalchemy.SQLAlchemy(app)

class EmployeeInfo(db.Model):
    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key = True)
    pn = db.Column(db.Text)
    name = db.Column(db.Text)
    position = db.Column(db.Text)
    department = db.Column(db.Text)
    dt = db.Column(db.Text)
    value = db.Column(db.Text)

    def __repr__(self):
        return "EmployeeInfo(pn={}, name={}, value={})".format(self.pn, self.name, self.value)

manager = flask_restless.APIManager(app, flask_sqlalchemy_db = db)
manager.create_api(EmployeeInfo, methods = ["GET"])

@app.route("/")
def home():
    import os
    print(__file__)
    list = EmployeeInfo.query.all()
    print(list)
    return "hello"

if (__name__ == '__main__'):
    app.run(port=9292, debug=True)