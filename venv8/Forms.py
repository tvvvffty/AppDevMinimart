from datetime import datetime
from wtforms.fields import DateField
from wtforms import Form, StringField,  SelectField, TextAreaField, validators, EmailField, PasswordField, FileField, IntegerField, RadioField
from wtforms.validators import EqualTo, DataRequired, ValidationError
from flask_wtf.file import FileAllowed



status_choices = [('', 'Select'), ('status text-success', 'Available'), ('status text-danger', 'Not Available')]

# category_choices = [('', 'Select'), ('E&D', 'Eggs & Diary'), ('MED', 'Over-The-Counter Medication'),
#                     ('D&C', 'Dry & Canned'), ('S&S', 'Sweets & Snacks'), ('D&B', 'Drinks & Beverages')]

# jia le
class CreateProduct(Form):
    name = StringField('Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    brand = StringField('Brand', [validators.Length(min=1, max=50), validators.DataRequired()])
    category = StringField('Category', [validators.Length(min=1, max=50), validators.DataRequired()])
    price = StringField('Price ($)', default='')
    quantity = StringField('Quantity', [validators.Length(min=1, max=50), validators.DataRequired()])
    status = SelectField('Status', [validators.DataRequired()], choices=status_choices, default='')
    date_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date_updated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    picture = FileField("Picture", validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

    def validate_quantity(form, quantity):
        if not quantity.data.isdigit():
            raise ValidationError("Quantity must be in numerical form")

    # def validate_picture(form, picture):
    #     if picture.data == None:
    #         raise ValidationError("Please Select An Image")


# jia le


# jing hui
class CreateCartForm(Form):
    name = StringField('Name', render_kw={'readonly': True})
    brand = StringField('Brand', render_kw={'readonly': True})
    category = StringField('Category', render_kw={'readonly': True})
    price = StringField('Price ($)', render_kw={'readonly': True})
    quantity = StringField('Quantity', [validators.Length(min=1, max=50), validators.DataRequired()])
    status = SelectField('Status', render_kw={'readonly': True})
    # status = SelectField('Status', [validators.DataRequired()], choices=status_choices, render_kw={'readonly': True})
    date_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date_updated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    picture = FileField("Picture", validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

    def validate_quantity(form, quantity):
        if not quantity.data.isdigit():
            raise ValidationError("Quantity must be in numerical form")

    # def validate_picture(form, picture):
    #     if picture.data == None:
    #         raise ValidationError("Please Select An Image")


class CreateOrderForm(Form):
    order_date = DateField('Date of Order', format='%Y-%m-%d')
    order_time = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    amount = StringField('Total amount $', [validators.Length(min=1, max=50), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])

    def validate_amount(form, amount):
        if not amount.data.isdigit():
            raise ValidationError("Money must be in digit")


class CreateSalesForm(Form):
    date = DateField('Date of Order', format='%Y-%m-%d')
    Total_amount = StringField('Total amount', [validators.Length(min=1, max=50), validators.DataRequired()])
    name = StringField('Name', [validators.Length(min=1, max=50), validators.DataRequired()])




# jing hui


# keith
class SignUpUser(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    # phone_number = StringField('Phone Number', validators=[validators.DataRequired(), validators.length(min=8, max=9)])
    phone_number = StringField('Phone Number', [validators.DataRequired()])
    unit_number = StringField('Unit Number', [validators.DataRequired()])
    postal_code = StringField('Postal Code', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    password_confirm = PasswordField('Password Confirmation', validators=[DataRequired(), EqualTo('password')])
    picture = FileField("Picture", validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

    def validate_phone_number(form, phone_number):
        if not phone_number.data.isdigit():
            raise ValidationError("Customer's number must all be digits")
        if len(phone_number.data) != 8:
            raise ValidationError("Customer's number must only have 8 digit")

    # def validate_picture(form, picture):
    #     if picture.data == None:
    #         raise ValidationError("Please Select An Image")

class updateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()], render_kw={'readonly': True})
    phone_number = StringField('Phone Number', [validators.DataRequired()], render_kw={'readonly': True})
    unit_number = StringField('Unit Number', [validators.DataRequired()], render_kw={'readonly': True})
    postal_code = StringField('Postal Code', [validators.DataRequired()], render_kw={'readonly': True})
    # password = PasswordField('Password', [validators.DataRequired()])
    # password_confirm = PasswordField('Password Confirmation', validators=[DataRequired(), EqualTo('password')])
    picture = FileField("Picture", validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

class updatePasswordForm(Form):
    password = PasswordField('Password', [validators.DataRequired()])
    password_confirm = PasswordField('Password Confirmation', validators=[DataRequired(), EqualTo('password')])


class LoginForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class UpdatePicture(Form):
    picture = FileField("Picture")


class PasswordForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
# keith

# jerell
class CreateStandardReward(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    value = StringField('Value', [validators.Length(min=1, max=150), validators.DataRequired()])
    points = IntegerField('Points')
    expiryDate = DateField('Expiration Date', format='%Y-%m-%d')
    category = SelectField('Category', choices=['Select', 'Shopping', 'Entertainment', 'Transport'])

    def validate_points(form, points):
        if points.data <= 0:
            raise ValidationError("Please enter a value more than 0")

    def validate_category(form, category):
        if category.data == "Select":
            raise ValidationError("Please enter a valid category")

    def validate_expiryDate(form, expiryDate):
        date_now = datetime.now().strftime("%Y-%m-%d")
        if str(expiryDate.data) < date_now:
            raise ValidationError("Expiry Date must not be earlier than today's date")
        elif str(expiryDate.data) == date_now:
            raise ValidationError("Expiry Date cannot be today's date")


class UpdateStandardReward(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    value = StringField('Value', [validators.Length(min=1, max=150), validators.DataRequired()])
    points = IntegerField('Points')
    expiryDate = StringField("Expiry Date (DD-MM-YYYY)", render_kw={'readonly': True})
    category = SelectField('Category', choices=['Select', 'Shopping', 'Entertainment', 'Transport'])

    def validate_points(form, points):
        if points.data <= 0:
            raise ValidationError("Please enter value more than 0")

    def validate_category(form, category):
        if category.data == "Select":
            raise ValidationError("Please enter a valid category")


class CreateSpecialReward(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    value = StringField('Value', [validators.Length(min=1, max=150), validators.DataRequired()])
    expiryDate = DateField('Expiration Date', format='%Y-%m-%d')
    category = SelectField('Category', choices=['Select', 'Shopping', 'Entertainment', 'Transport'])

    def validate_category(form, category):
        if category.data == "Select":
            raise ValidationError("Please enter valid category")

    def validate_expiryDate(form, expiryDate):
        date_now = datetime.now().strftime("%Y-%m-%d")
        if str(expiryDate.data) < date_now:
            raise ValidationError("Expiry Date must not be earlier than today's date")
        elif str(expiryDate.data) == date_now:
            raise ValidationError("Expiry Date cannot be today's date")


class UpdateSpecialReward(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    value = StringField('Value', [validators.Length(min=1, max=150), validators.DataRequired()])
    expiryDate = StringField("Expiration Date (DD-MM-YYYY)", render_kw={'readonly': True})
    category = SelectField('Category', choices=['Select', 'Shopping', 'Entertainment', 'Transport'])

    def validate_category(form, category):
        if category.data == "Select":
            raise ValidationError("Please enter valid category")


class CreatePromoCode(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    value = StringField('Value', [validators.Length(min=1, max=150), validators.DataRequired()])
    promoCode = StringField('Promo Code', [validators.Length(min=1, max=150), validators.DataRequired()])
    quantity = IntegerField('Quantity')
    expiryDate = DateField('Expiration Date', format='%Y-%m-%d')
    category = SelectField('Category', choices=['Select', 'Shopping', 'Entertainment', 'Transport'])

    def validate_quantity(form, quantity):
        if quantity.data <= 0:
            raise ValidationError("Please enter a value more than 0")

    def validate_expiryDate(form, expiryDate):
        date_now = datetime.now().strftime("%Y-%m-%d")
        if str(expiryDate.data) < date_now:
            raise ValidationError("Expiry Date must not be earlier than today's date")
        elif str(expiryDate.data) == date_now:
            raise ValidationError("Expiry Date cannot be today's date")


class UpdatePromoCode(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    value = StringField('Value', [validators.Length(min=1, max=150), validators.DataRequired()])
    promoCode = StringField('Promo Code', [validators.Length(min=1, max=150), validators.DataRequired()])
    quantity = IntegerField('Quantity')
    expiryDate = StringField("Expiration Date", render_kw={'readonly': True})
    category = SelectField('Category', choices=['Select', 'Shopping', 'Entertainment', 'Transport'])

    def validate_quantity(form, quantity):
        if quantity.data <= 0:
            raise ValidationError("Please enter a value more than 0")


class CreateFeedback(Form):
    q1 = StringField('Enter a question', [validators.Length(min=1, max=150), validators.DataRequired()])
    q2 = StringField('Enter a question', [validators.Length(min=1, max=150), validators.DataRequired()])
    q3 = StringField('Enter a question', [validators.Length(min=1, max=150), validators.DataRequired()])
    q4 = StringField('Enter a question', [validators.Length(min=1, max=150), validators.DataRequired()])
    q5 = StringField('Enter a question', [validators.Length(min=1, max=150), validators.DataRequired()])


class UpdateFeedback(Form):
    q1 = StringField('Enter question for Star Rating', [validators.Length(min=1, max=150), validators.DataRequired()])
    q2 = StringField('Enter question for Open-Ended', [validators.Length(min=1, max=150), validators.DataRequired()])
    q3 = StringField('Enter question for Open-Ended', [validators.Length(min=1, max=150), validators.DataRequired()])
    q4 = StringField('Enter question for Yes/No', [validators.Length(min=1, max=150), validators.DataRequired()])
    q5 = StringField('Enter question for Products Dropdown List', [validators.Length(min=1, max=150), validators.DataRequired()])


class UserFeedbackForms(Form):
    q1 = RadioField('How would you rate your experience with us ?', choices=[1, 2, 3, 4, 5], default=1)
    q2 = TextAreaField('What is one thing you like about our online store ?', [validators.length(max=200), validators.DataRequired()])
    q3 = TextAreaField('What is one thing you like least about our online store ?', [validators.length(max=200), validators.DataRequired()])
    q4 = RadioField('Would you visit us again ?', choices=['Yes', 'No'], default='Yes')
    dropdown = SelectField('What is your favourite product in out store ?', choices=[])
# jerell
