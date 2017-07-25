from flask import request
from flask_restful import Resource

# defining the class with http verb based methods
class TaskREST(Resource):

    # defining method for get task
    def get(self):
        return {"message":"taskFound"}


    # defining method for create task
    def post(self):
        # task data will be recieved in the request object
        requestData = request.form
        
        # extracting task parameters
        task = requestData.get('task',None)

        return {"message":"taskCreated"}
