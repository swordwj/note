from flask import session,json
from main.models import Note
from flask.views import MethodView
from flask import make_response, request
import json


class NoteAPI(MethodView):


    def get(self):

        if session.get('userid') is not None:
            masterid = session.get('userid')

            # 获用户所有note数据
            sql = 'SELECT * FROM notes WHERE user_id = %s ORDER BY note_id DESC;'
            parm = (masterid,)
            rows = Note().get_AllNote(sql, parm)
            # 读取元组数据，转换为json类型
            notes = []
            for row in rows:
                note = {}
                note['id'] = row[0]
                note['content'] = row[1]
                note['completed'] = row[2]
                note['deleted'] = row[3]
                notes.append(note)

            #返回所有notes信息
            info = {
                "success": True,
                "errorMsg": None,
                "data": notes
            }
            result = json.dumps(info, ensure_ascii=False)
            response = make_response(result)
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response

        else:

            # 未登录，返回错误信息
            info = {
                "success": False,
                "errorMsg": "Please log in first!",
                "data": None
            }
            result = json.dumps(info, ensure_ascii=False)
            response = make_response(result)
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response


    def post(self):

        if session.get('userid') is not None:
            masterid = session.get('userid')

            # 获取前端发送的note内容
            new_note = request.json
            content = new_note["content"]

            # 添加一条note
            sql_add = 'INSERT INTO notes (content,completed,deleted,user_id) VALUES (%s,FALSE,FALSE ,%s);'
            parm_add = (content, masterid)
            Note().set_Note(sql_add, parm_add)

            # 获用户添加的note数据
            sql = 'SELECT * FROM notes WHERE user_id = %s  ORDER BY note_id DESC;'
            parm = (masterid,)
            rows = Note().get_AllNote(sql, parm)
            print(rows)
            # 读取元组数据，转换为json类型
            notes = []
            for row in rows:
                note = {}
                note['id'] = row[0]
                note['content'] = row[1]
                note['completed'] = row[2]
                note['deleted'] = row[3]
                notes.append(note)

            # 返回新添加的note信息
            info = {
                "success": True,
                "errorMsg": None,
                "data": notes
            }

            result = json.dumps(info, ensure_ascii=False)
            response = make_response(result)
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response

        else:
            # 未登录，返回错误信息
            info = {
                "success": False,
                "errorMsg": "Please log in first!",
                "data": None
            }
            result = json.dumps(info, ensure_ascii=False)
            response = make_response(result)
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response


    def put(self):

        if session.get('userid') is not None:
            masterid = session.get('userid')

            # 获取前端发送的note内容
            note = request.json
            noteid =  note["id"]
            content = note["content"]
            completed = note["completed"]
            deleted = note["deleted"]

            if noteid is not None:
                # 修改note信息
                sql_update = 'UPDATE notes SET content = %s,completed = %s,deleted = %s  WHERE note_id = %s;'
                parm_update = (content,completed,deleted,noteid)
                Note().set_Note(sql_update, parm_update)

                # 获用更改后的note
                sql = 'SELECT * FROM notes WHERE note_id = %s;'
                parm = (noteid,)
                rows = Note().get_AllNote(sql, parm)

                # 读取元组数据，转换为json类型
                notes = []
                for row in rows:
                    note = {}
                    note['id'] = row[0]
                    note['content'] = row[1]
                    note['completed'] = row[2]
                    note['deleted'] = row[3]
                    notes.append(note)

                # 返回新添加的note信息
                info = {
                    "success": True,
                    "errorMsg": None,
                    "data": notes
                }

                result = json.dumps(info, ensure_ascii=False)
                response = make_response(result)
                response.headers["Content-Type"] = "application/json; charset=utf-8"
                return response
            else:
                # 返回错误信息
                info = {
                    "success": False,
                    "errorMsg": "can not find a note",
                    "data": None
                }
                result = json.dumps(info, ensure_ascii=False)
                response = make_response(result)
                response.headers["Content-Type"] = "application/json; charset=utf-8"
                return response

        else:
            # 未登录，返回错误信息
            info = {
                "success": False,
                "errorMsg": "Please log in first!",
                "data": None
            }
            result = json.dumps(info, ensure_ascii=False)
            response = make_response(result)
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response

    def delete(self):

        if session.get('userid') is not None:
            masterid = session.get('userid')

            # 获取前端发送的note内容
            listid = request.data

            if listid is not None:
                # notes = []
                for id in listid:
                    return id

        #             # 修改note的deleted值
        #             sql_update = 'UPDATE notes SET deleted = True  WHERE note_id = %s;'
        #             parm_update = (id,)
        #             Note().set_Note(sql_update, parm_update)
        #
        #             # 获用更改后的note
        #             sql = 'SELECT * FROM notes WHERE note_id = %s;'
        #             parm = (id,)
        #             row = Note().get_Note(sql, parm)
        #
        #             # 读取元组数据，转换为json类型
        #             note = {}
        #             note['id'] = row[0]
        #             note['content'] = row[1]
        #             note['completed'] = row[2]
        #             note['deleted'] = row[3]
        #             notes.append(note)
        #
        #         # 返回新添加的note信息
        #         info = {
        #             "success": True,
        #             "errorMsg": None,
        #             "data": notes
        #         }
        #
        #         result = json.dumps(info, ensure_ascii=False)
        #         response = make_response(result)
        #         response.headers["Content-Type"] = "application/json; charset=utf-8"
        #         return response
        #
        #     else:
        #         # 返回错误信息
        #         info = {
        #             "success": False,
        #             "errorMsg": "can not find a note",
        #             "data": None
        #         }
        #         result = json.dumps(info, ensure_ascii=False)
        #         response = make_response(result)
        #         response.headers["Content-Type"] = "application/json; charset=utf-8"
        #         return response
        #
        # else:
        #     # 未登录，返回错误信息
        #     info = {
        #         "success": False,
        #         "errorMsg": "Please log in first!",
        #         "data": None
        #     }
        #     result = json.dumps(info, ensure_ascii=False)
        #     response = make_response(result)
        #     response.headers["Content-Type"] = "application/json; charset=utf-8"
        #     return response
