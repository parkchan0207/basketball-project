from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class CourtForm(FlaskForm):
    name = StringField('경기장 이름', validators=[DataRequired()])
    location = StringField('위치', validators=[DataRequired()])
    operating_hours = StringField('운영 시간', validators=[DataRequired()])
    wheelchair_rental = BooleanField('휠체어 대여')
    wheelchair_ramp = BooleanField('휠체어 경사로')
    elevator = BooleanField('엘리베이터')
    adjustable_basket = BooleanField('골대 높낮이 조절')
    facilities = TextAreaField('시설 정보')
    image = FileField('경기장 사진', validators=[
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], '이미지 파일만 업로드 가능합니다.')
    ])
    submit = SubmitField('등록하기') 