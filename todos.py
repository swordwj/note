from flask import Flask
from view.users import *
from view.notes import *


app = Flask(__name__)
app.secret_key = '123'

#logout
logout_view = LogoutAPI.as_view('logout_api')
app.add_url_rule('/api/logout/', view_func=logout_view, methods=['GET'])

#login/register
login_view = LoginAPI.as_view('login_api')
app.add_url_rule('/api/login/', view_func=login_view, methods=['POST'])
rgs_view = RegisterAPI.as_view('rgs_api')
app.add_url_rule('/api/register/', view_func=rgs_view, methods=['POST'])

#todos
note_view = NoteAPI.as_view('note_api')
app.add_url_rule('/api/todos/', view_func=note_view, methods=['GET','POST','PUT'])

#delete todos
delete_view = DeleteAPI.as_view('delete_api')
app.add_url_rule('/api/delete/', view_func=delete_view, methods=['PUT'])

#all todos completed
allcompeleted_view = AllCompleteAPI.as_view('allcompeleted_api')
app.add_url_rule('/api/compeleted/', view_func=allcompeleted_view, methods=['PUT'])


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#haha

if __name__ == '__main__':
    app.run(debug=True)
