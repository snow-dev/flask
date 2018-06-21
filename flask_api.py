
from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

# Prepare argument parsing
# parser = reqparse.RequestParser()
# parser.add_argument('rate', type=int, help='Rate to charge for this resource')
# args = parser.parse_args()

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):

    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
        pass

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
        pass


api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
