#-*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


class SearchForm(FlaskForm):
    searchInfo=StringField('')
    submit=SubmitField('搜索')