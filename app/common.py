#-*-coding:utf-8-*-
from .models import BookClass
from app import cache

@cache.cached(timeout=7200,key_prefix='getBookClass')
def getBookClass():
    bookClasses=BookClass.query.all()
    return bookClasses

def getBookClassByParentId(parentId):
    bookClasses=[]
    for bookClass in getBookClass():
        if parentId==bookClass.bookParentClassId:
            bookClasses.append(bookClass)
    return bookClasses

def getBookClassById(id):
    for bookClass in getBookClass():
        if id==bookClass.bookClassId:
            return bookClass
    return None