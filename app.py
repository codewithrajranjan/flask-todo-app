from flask import Flask
from flask_restful import Resource, Api
from app import TaskREST,TaskByIdREST, TaskByIdAndStatusREST


# creating the app instance
app = Flask(__name__)


# creating api instance
api = Api(app)


# adding resources
api.add_resource(TaskREST,"/task")
api.add_resource(TaskByIdREST,"/task/id/<taskId>")
api.add_resource(TaskByIdAndStatusREST,"/task/id/<taskId>/status/<taskStatus>")






#This will run if the the this module is run standalone
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    
