# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField('邮箱'.decode('utf-8'), validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('密码'.decode('utf-8'), validators=[DataRequired()])
    remember_me = BooleanField('保持登录'.decode('utf-8'))
    submit = SubmitField('登录'.decode('utf-8'))

class RegistrationForm(Form):
    email = StringField('邮箱'.decode('utf-8'), validators=[DataRequired(),Length(1, 64),
                                             Email()])
    username = StringField('用户名'.decode('utf-8'), validators=[
        DataRequired(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                             '用户名必须只能包括字母, '
                                             '数字, 点或下划线'.decode('utf-8'))])
    password = PasswordField('密码'.decode('utf-8'), validators=[
        DataRequired(), EqualTo('password2', message='密码必须相同.'.decode('utf-8'))])
    password2 = PasswordField('重输密码'.decode('utf-8'), validators=[DataRequired()])
    submit = SubmitField('注册'.decode('utf-8'))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册.'.decode('utf-8'))

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise  ValidationError('用户名已存在.'.decode('utf-8'))


class ChangePasswordForm(Form):
    old_password = PasswordField('旧密码'.decode('utf-8'), validators=[DataRequired()])
    password = PasswordField('新密码'.decode('utf-8'), validators=[
        DataRequired(),  EqualTo('password2', message='密码必须相同.'.decode('utf-8'))])
    password2 = PasswordField('重输密码'.decode('utf-8'), validators=[DataRequired()])
    submit = SubmitField('更新密码'.decode('utf-8'))


class PasswordResetRequestForm(Form):
    email = StringField('邮箱'.decode('utf-8'), validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('重置密码'.decode('utf-8'))


class PasswordResetForm(Form):
    email = StringField('邮箱'.decode('utf-8'), validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('新密码'.decode('utf-8'), validators=[
        DataRequired(),  EqualTo('password2', message='密码必须相同.'.decode('utf-8'))])
    password2 = PasswordField('重输密码'.decode('utf-8'), validators=[DataRequired()])
    submit = SubmitField('重置密码'.decode('utf-8'))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('未知邮箱.'.decode('utf-8'))


class ChangeEmailForm(Form):
    email = StringField('新邮箱'.decode('utf-8'), validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('密码'.decode('utf-8'), validators=[DataRequired()])
    submit = SubmitField('更新邮箱'.decode('utf-8'))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册.'.decode('utf-8'))