from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.topic import Topic
from models.board import Board


main = Blueprint('topic', __name__)


@main.route("/")
def index():
    # board_id = 2
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        ms = Topic.all()
    else:
        ms = Topic.find_all(board_id=board_id)
    u = current_user()
    bs = Board.all()
    # ms = Topic.all()
    return render_template("topic/index.html", ms=ms, bs=bs)


@main.route('/<int:id>')
def detail(id):
    m = Topic.get(id)
    b = Board.get(m.board_id)
    u = User.get(m.user_id)
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=m, board=b, user=u)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Topic.new(form, user_id=u.id) # , user_id=u.id
    return redirect(url_for('.detail', id=m.id))


@main.route('/delete')
def delete():
    id = int(request.args.get('id'))
    u = current_user()
    # 判断 token 是否是我们给的
    Topic.delete(id)
    return redirect(url_for('.index'))


@main.route("/new")
def new():
    bs = Board.all()
    return render_template("topic/new.html", bs=bs)
