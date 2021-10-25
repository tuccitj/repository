from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	
    data = {
	"{{vendor_name}}": "CloudBill LLC",
	"{{vendor_fullname}}": "Theodore J. Tucci",
	"{{vendor_title}}": "Partner",
	"{{date}}": "October 21, 2021",
    "{{licensee_name}}": "Gerald Vasile",
    "{{date}}": "October 21, 2021",
    "{{product_name}}": "DocuFill",
	"{{date}}": "October 21, 2021",
	"{{vendor_sign_date}}": "October 21, 2021",
	"{{licensee_sign_date}}": "October 21, 2021",
	"{{Ipsum}}": "Gerald Vasile",
    "{{venenatis}}": "TEST-FILLED",
    "{{ante}}": "TEST-FILLED$%!@#$%^&*()_fdsfa.",
    "{{HIHIHIDSFSFDSF}}": "IS THIS FSDJFDFFD",
	"{{fee}}": "$1500.00"
}
    lines = {}
    
    for key in data:
        key = key.strip('}')
        key = key.strip('{')
        lines[key] = StringField(key)

        # globals()[key] = StringField(key)
    # print(globals())
    # print(vendor_name)
    # vendor_name = lines['vendor_name']
    username = StringField('Username')
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')