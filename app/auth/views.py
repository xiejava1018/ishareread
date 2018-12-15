#-*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for,abort,flash,request,current_app,make_response
from . import auth_blueprint
from .. import db

@auth_blueprint.route('/',methods=['GET','POST'])
def index():
    pass;


