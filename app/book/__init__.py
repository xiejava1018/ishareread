#-*-coding:utf-8-*-
from flask import Blueprint

book_blueprint=Blueprint('book_blueprint',__name__)

from . import views