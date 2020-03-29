from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.topic import Topic
from models.board import Board

main = Blueprint('topic', __name__)

import uuid

csrf_tokens = dict()


@main.route("/")
def index():
    # board_id = 2
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        ms = Topic.find_all(deleted=False)
    else:
        ms = Topic.find_all(board_id=board_id, deleted=False)
    token = str(uuid.uuid4())
    u = current_user()
    csrf_tokens[token] = u.id
    bs = Board.all()
    # ms = Topic.all()
    return render_template("topic/index.html", ms=ms, token=token, bs=bs)


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
    m = Topic.new(form, user_id=u.id)  # , user_id=u.id
    return redirect(url_for('.detail', id=m.id))


@main.route('/delete')
def delete():
    id = int(request.args.get('id'))
    token = request.args.get('token')

    u = current_user()
    # print(id, token, u, csrf_tokens)
    # 判断 token 是否是我们给的
    if token in csrf_tokens and csrf_tokens[token] == u.id:
        csrf_tokens.pop(token)
        if u is not None:
            print('删除topic用户是:', u, '删除的topicid为：', id)
            # 此处应该是 以 实例对象来访问类方法，所以需要先确定对象，不能直接进行类方法 Topic.delete()的请求
            t = Topic.find_by(id=id)
            t.delete()
            # Topic.delete(id)
            return redirect(url_for('.index'))
        else:
            abort(404)
    else:
        abort(404)


@main.route("/new")
def new():
    bs = Board.all()
    return render_template("topic/new.html", bs=bs)
