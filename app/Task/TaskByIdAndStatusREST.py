from flask import request
from flask_restful import Resource

# defining the class with http verb based methods
class TaskByIdAndStatusREST(Resource):

    # defining method for updating task by status
    def put(self,taskId,taskStatus):
        print(taskId)
        print(taskStatus)
        return {"message":"taskUpdated"}
