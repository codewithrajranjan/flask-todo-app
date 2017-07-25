from flask import request
from flask_restful import Resource

# defining the class with http verb based methods
class TaskByIdREST(Resource):

    # defining method for get task by id
    def get(self,taskId):
        print(taskId)
        return {"message":"taskFound"}

    # defining method to delete task by id
    def delete(self,taskId):
        print(taskId)
        return {"message":"taskDeleted"}
