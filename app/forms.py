# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
'''
导入 Form 类，接着导入两个我们需要的字段类，TextField 和 BooleanField。
DataRequired 验证器只是简单地检查相应域提交的数据是否是空。
'''

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)