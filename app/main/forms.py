# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField, SubmitField, TextAreaField ,\
    BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(Form):
    name = StringField('姓名?'.decode('utf-8'), validators=[DataRequired()])
    submit = SubmitField('提交'.decode('utf-8'))


class EditProfileForm(Form):
    name = StringField('真实姓名'.decode('utf-8'), validators=[Length(0, 64)])
    location = StringField('位置'.decode('utf-8'), validators=[Length(0, 64)])
    about_me = TextAreaField('关于我'.decode('utf-8'))
    submit = SubmitField('提交'.decode('utf-8'))


class EditProfileAdminForm(Form):
    email = StringField('邮箱'.decode('utf-8'), validators=[DataRequired(),
                                             Length(1, 64), Email()])
    username = StringField('用户名'.decode('utf-8'), validators=[
        DataRequired(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                             '用户名必须只能包括字母, '
                                             '数字, 点或下划线'.decode('utf-8'))])
    confirmed = BooleanField('已验证'.decode('utf-8'))
    role = SelectField('邮箱'.decode('utf-8'), coerce=int)
    name = StringField('真实姓名'.decode('utf-8'), validators=[Length(0, 64)])
    location = StringField('位置'.decode('utf-8'), validators=[Length(0, 64)])
    about_me = TextAreaField('关于我'.decode('utf-8'))
    submit = SubmitField('提交'.decode('utf-8'))

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册.'.decode('utf-8'))

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在.'.decode('utf-8'))


class PostForm(Form):
    body = PageDownField("你在想什么?".decode('utf-8'), validators=[DataRequired()])
    submit = SubmitField('提交'.decode('utf-8'))


class CommentForm(Form):
    body = StringField('', validators=[DataRequired()])
    submit = SubmitField('提交'.decode('utf-8'))
