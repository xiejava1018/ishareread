#-*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for,abort,flash,request,current_app,make_response
from . import book_blueprint
from ..models import BookClass,Book
from .. import db
from app.common import getBookClassByParentId,getBookClassById

@book_blueprint.route('/booklist',methods=['GET','POST'])
def booklist():
    bookClassList=getBookClassByParentId(0)
    bookClassId=request.args.get('bookClassId',type=int)
    subBookClassId=request.args.get('subBookClassId',type=int)
    per_page=current_app.config['ISHAREREAD_BOOKLIST_PER_PAGE']
    page = request.args.get('page', 1, type=int)
    subBookClassList=[]
    if bookClassId and subBookClassId:
        subBookClassList = getBookClassByParentId(bookClassId)
        pagination = Book.query.join(BookClass.bookclass).filter(BookClass.bookClassId == subBookClassId).paginate(page,per_page=per_page,error_out=False)
    elif bookClassId:
        subBookClassList = getBookClassByParentId(bookClassId)
        pagination = Book.query.join(BookClass.bookclass).filter(BookClass.bookParentClassId == bookClassId).paginate(page, per_page=per_page, error_out=False)
    else:
        pagination=Book.query.join(BookClass.bookclass).paginate(page,per_page=per_page,error_out=False)
    bookList=pagination.items
    return render_template('book/booklist.html',bookClassId=bookClassId,subBookClassId=subBookClassId,
                           bookClassList=bookClassList,subBookClassList=subBookClassList,
                           bookList=bookList,pagination=pagination)



@book_blueprint.route('/book/<int:bookId>',methods=['GET','POST'])
def getbookdetail(bookId):
    book=Book.query.filter(Book.bookId==bookId).first()
    bookClass=book.bookClasses.first()
    if bookClass:
        parentBookClass=getBookClassById(bookClass.bookParentClassId)
        sameTypeBooks=Book.query.join(BookClass.bookclass).filter(BookClass.bookClassId == bookClass.bookClassId,Book.bookId!=bookId).limit(5)
    return render_template('book/book.html',parentBookClass=parentBookClass,bookClass=bookClass,book=book,sameTypeBooks=sameTypeBooks)