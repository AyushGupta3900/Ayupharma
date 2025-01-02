from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from ayupharma.models import User,Message
from flask_login import login_user, current_user, logout_user, login_required

# RegistrationForm inherits from FlaskForm

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2,max=20)])
    mobile_number = StringField('Mobile Number',
                            validators=[DataRequired(),Length(min=10,max=10)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken')

class SigninForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired(),Length(max=50)])
    submit = SubmitField('Submit')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class DiseaseForm(FlaskForm):
    disease_1 = StringField('disease-1',validators=[DataRequired(),Length(max=20)])
    disease_2 = StringField('disease-2',validators=[DataRequired(),Length(max=20)])
    disease_3 = StringField('disease-3',validators=[DataRequired(),Length(max=20)])
    submit = SubmitField('Update Diseases')

class ContactUsForm(FlaskForm):
    firstname = StringField('Firstname',
                            validators=[DataRequired(), Length(min=2,max=20)])
    lastname = StringField('Lastname',
                            validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    mobile_number = StringField('Mobile Number',
                            validators=[DataRequired(),Length(min=10,max=10)])
    message = TextAreaField('Message',validators=[DataRequired(),Length(max=200)])
    submit = SubmitField('Send Message')

    