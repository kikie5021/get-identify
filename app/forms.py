# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired, Optional, ValidationError

from app.models import Strain, TestFood
from app import constants as C


class StrainForm(FlaskForm):
    name = StringField('Strain', validators=[DataRequired()])
    category = SelectField('Category',
        validators=[Optional()],
        choices=[(C.NON_PATHOGENIC, C.CATEGORY[C.NON_PATHOGENIC]),
                 (C.PATHOGENIC, C.CATEGORY[C.PATHOGENIC])],
        coerce=int)
    test_result = HiddenField('Test result', validators=[DataRequired()])

    # def validate_name(form, field):
    #     if Strain.exists(name=field.data):
    #         raise ValidationError(u'Strain has already exists.')

    def validate_test_result(form, field):
        num = TestFood.query.count()
        if num != len(field.data):
            raise ValidationError(u'Please fulfill test result.')


class TestFoodForm(FlaskForm):
    name = StringField('Biochemical broth', validators=[DataRequired()])

    def validate_name(form, field):
        if TestFood.exists(name=field.data):
            raise ValidationError(u'Biochemical broth has already exists.')


class SampleFoodForm(FlaskForm):
    name = StringField(u'Memo', validators=[Optional()])
    test_result = HiddenField('Test result', validators=[DataRequired()])

    def validate_test_result(form, field):
        field.data = field.data.replace(' ', '').replace('\t', '').strip()
        num = TestFood.query.count()
        if num != len(field.data):
            raise ValidationError(u'Please fulfill test result.')
