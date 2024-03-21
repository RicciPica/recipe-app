from db_controller_recipe import get_all_recipes, get_all_recipes_no_img, get_recipe_by_id, get_ingridients, get_steps
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)

# TODO: Limit CORS
CORS(app)

@app.route('/api/recipe/all', methods=['GET'])
def api_get_all_recipies():
    return get_all_recipes()

@app.route('/api/recipe/all-id-name', methods=['GET'])
def api_get_all_recipes_id_name():
    return get_all_recipes_no_img()

@app.route('/api/recipe/<id>', methods=['GET'])
def api_get_recipe_by_id(id):
    return get_recipe_by_id(id)

@app.route('/api/recipe/ingridients/<id>', methods=['GET'])
def api_get_ingridients(id):
    return get_ingridients(id)

@app.route('/api/recipe/steps/<id>', methods=['GET'])
def api_get_steps(id):
    return get_steps(id)

if __name__ == "__main__":
    app.run(debug=True)