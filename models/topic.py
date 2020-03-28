import time
import json
from models import Model
from .user import User
from models.mongua import Mongua


class Topic(Model):
    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        m.views += 1
        m.save()
        return m

    def __init__(self, form):
        self.id = None
        self.views = 0
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.ct = int(time.time())
        self.ut = self.ct
        self.user_id = form.get('user_id', '')
        self.board_id = int(form.get('board_id', -1))

    def replies(self):
        from .reply import Reply
        ms = Reply.find_all(topic_id=self.id)
        return ms

    def user(self):
        u = User.find_by(id=self.user_id)
        return u


class Topic(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('content', str, ''),
        ('title', str, ''),
        ('user_id', int, -1),
        ('board_id', int, -1),
        ('views', int, 0)
    ]

    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        m.views += 1
        m.save()
        return m

    def replies(self):
        from .reply import Reply
        ms = Reply.find_all(topic_id=self.id)
        return ms

    def board(self):
        from .board import Board
        m = Board.find(self.board_id)
        return m

    def user(self):
        u = User.find(id = self.user_id)
        return u
