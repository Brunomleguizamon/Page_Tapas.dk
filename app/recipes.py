from flask import(
    Blueprint,
    render_template
)

bp = Blueprint('recipes', __name__, url_prefix='/recipes')


@bp.route('/', methods=['GET'])
def recipes():
    return render_template('recipes/home-recipes.html')
