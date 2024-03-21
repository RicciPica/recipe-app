from utilities.db_connection import fetchone, fetchall
from utilities.JSON_converter import convert_to_json

import json
import base64

def get_all_recipes():
        sql_statement = 'SELECT * FROM recipe'
        res = json.loads(fetchall(sql_statement))

        for re in res:
                if re['image_file_name']:
                   with open(f"backend\img_recipe\{str(re['image_file_name'])}", "rb") as imagefile:
                        re['image_file_name']  = base64.b64encode(imagefile.read()).decode('utf-8')
        
        res = convert_to_json(res)
        return res

def get_all_recipes_no_img():
       sql_statement = 'SELECT uid_recipe, name, author, difficulty, time_min FROM recipe'
       res = fetchall(sql_statement)

       return res

def get_recipe_by_id(id):
        id = {'id': id}
        sql_statement = 'SELECT * FROM recipe WHERE uid_recipe = %(id)s'
        res = json.loads(fetchone(sql_statement, id))
        
        if res['image_file_name']:
                with open(f"backend\img_recipe\{str(res['image_file_name'])}", "rb") as imagefile:
                        res['image_file_name'] = base64.b64encode(imagefile.read()).decode('utf-8')
        
        res = convert_to_json(res)
        return res

def get_ingridients(id):
       id = {'id': id}
       sql_statement = '''SELECT i.name FROM recipe r 
                        INNER JOIN ingridients i ON r.uid_recipe = i.uid_recipe 
                        WHERE r.uid_recipe = %(id)s'''
       
       res = fetchall(sql_statement, id)
       return res

def get_steps(id):
        id = {'id': id}
        sql_statement = '''SELECT s.step_number, s.step_description FROM recipe r 
                        INNER JOIN recipe_steps s ON s.uid_recipe = r.uid_recipe 
                        WHERE r.uid_recipe = %(id)s
                        ORDER BY s.step_number'''
       
        res = fetchall(sql_statement, id)
        return res
       

# get_recipe_by_id('8f5b95be-aaf4-4f7d-a4e1-4eb2472a92ba')
# get_ingridients('8f5b95be-aaf4-4f7d-a4e1-4eb2472a92ba')
# get_all_recipes_no_img()
# get_steps("8f5b95be-aaf4-4f7d-a4e1-4eb2472a92ba")
