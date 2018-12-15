#-*-coding:utf-8-*-
from . import db

class BookClass(db.Model):
    __tablename__ = 'ishare_book_class'
    bookClassId=db.Column('book_class_id',db.Integer,primary_key=True)
    bookClassName=db.Column('book_class_name',db.String(255),index=True)
    bookParentClassId=db.Column('book_parent_class_id',db.Integer)
    bookClassDesc=db.Column('book_class_desc',db.String(255))
    bookClassOrder=db.Column('book_class_order',db.Integer)
    createBy=db.Column('create_by',db.String(64))
    createDate=db.Column('create_date',db.DateTime())
    updateBy=db.Column('update_by',db.String(64))
    updateDate=db.Column('update_date',db.DateTime())
    remarks=db.Column('remarks',db.String(255))
    delFlag=db.Column('del_flag',db.String(1))
    books=db.relationship('Book', secondary='ishare_book_class_rela',backref=db.backref('book', lazy='dynamic'), lazy='dynamic')

class Book(db.Model):
    __tablename__ = 'ishare_book'
    bookId=db.Column('book_id',db.Integer,primary_key=True)
    bookName=db.Column('book_name',db.String(100),index=True)
    bookAuthor=db.Column('book_author',db.String(100))
    bookPress=db.Column('book_press',db.String(255))
    bookPressDate=db.Column('book_pressdate',db.String(20))
    bookIsbn=db.Column('book_isbn',db.String(50))
    bookContentDesc=db.Column('book_content_desc',db.Text)
    bookAuthorDesc=db.Column('book_author_desc',db.Text)
    bookCatalog=db.Column('book_catalog',db.Text)
    bookImage=db.Column('book_image',db.String(255))
    bookPrice=db.Column('book_price',db.String(20))
    bookTag = db.Column('book_tag',db.String(500))
    bookClassId=db.Column('book_class_id',db.Integer)
    bookIshot=db.Column('book_ishot',db.Integer)
    bookShoworder=db.Column('book_showorder',db.Integer)
    bookFloorId=db.Column('book_floor_id',db.Integer)
    bookAddDate=db.Column('book_add_date',db.DateTime())
    bookWantread_count=db.Column('book_wantread_count',db.Integer)
    bookIsreadCount=db.Column('book_isread_count',db.Integer)
    bookHavereadCount=db.Column('book_haveread_count',db.Integer)
    bookEbookHavecount=db.Column('book_ebook_havecount',db.Integer)
    bookBookHavecount=db.Column('book_book_havecount',db.Integer)
    bookShareEbookcount=db.Column('book_share_ebookcount',db.Integer)
    bookShareBookcount=db.Column('book_share_bookcount',db.Integer)
    bookPages=db.Column('book_pages',db.String(11))
    bookDoubanId = db.Column('book_douban_id',db.String(11))
    bookDoubanUrl=db.Column('book_douban_url',db.String(255))
    bookStatus=db.Column('book_status',db.Integer)
    createBy=db.Column('create_by',db.String(64))
    createDate=db.Column('create_date',db.DateTime())
    updateBy=db.Column('update_by',db.String(64))
    updateDate = db.Column('update_date',db.DateTime())
    remarks = db.Column('remarks',db.String(255))
    delFlag= db.Column('del_flag',db.String(1))
    bookClasses = db.relationship('BookClass', secondary='ishare_book_class_rela',backref=db.backref('bookclass', lazy='dynamic'),lazy='dynamic')


class BookClassRela(db.Model):
    __tablename__ = 'ishare_book_class_rela'
    bookId=db.Column('book_id',db.Integer,db.ForeignKey('ishare_book.book_id'),primary_key=True)
    bookClassId = db.Column('book_class_id', db.Integer,db.ForeignKey('ishare_book_class.book_class_id'),primary_key=True)
    createBy = db.Column('create_by', db.String(64))
    createDate = db.Column('create_date', db.DateTime())
    updateBy = db.Column('update_by', db.String(64))
    updateDate = db.Column('update_date', db.DateTime())
    remarks = db.Column('remarks', db.String(255))
    delFlag = db.Column('del_flag', db.String(1))







