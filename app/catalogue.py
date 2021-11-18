from flask import(
    Blueprint,
    render_template
)

bp = Blueprint('catalogue', __name__, url_prefix='/catalogue')


@bp.route('/', methods=['GET'])
def products():
    return render_template('catalogue/home-catalogue.html')
