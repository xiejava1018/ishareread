#-*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for,abort,flash,request,current_app,make_response
from app.common import getBookClassByParentId
from . import main
from .forms import SearchForm
from ..models import Book
from .. import db

@main.route('/',methods=['GET','POST'])
def index():
    form=SearchForm()
    bookClassList=getBookClassByParentId(0)
    newBooks=Book.query.filter_by(bookStatus=1).order_by(Book.createBy.desc()).limit(5)
    goodBooks=Book.query.filter(Book.bookStatus==1,Book.bookFloorId==1).order_by(Book.bookShoworder).limit(10)
    shareHotBooks=Book.query.filter_by(bookStatus=1).order_by(Book.bookShareEbookcount.desc()).limit(5)
    return render_template('index.html',form=form,bookClassList=bookClassList,
                           newBooks=newBooks,goodBooks=goodBooks,shareHotBooks=shareHotBooks)


