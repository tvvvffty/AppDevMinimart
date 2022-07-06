import User, Login
import shelve

from flask import Flask, render_template, request, redirect, url_for, flash, session, Markup
from flask_session import Session
from Forms import SignUpUser, LoginForm
import os
from werkzeug.utils import secure_filename


basedir = os.getcwd()
DBDIR = f"{basedir}/notes"
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

Upload_Folder = 'static/assets/profimg/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['Upload_FOLDER'] = Upload_Folder


labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"
]


@app.route('/line')
def line():
    line_labels = labels
    line_values = values

    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    db.close()

    lenVal = (len(signup_dict.keys()))
    return render_template('line.html', title='User Creation Statistics(Graph)', max=50, labels=line_labels,
                           values=line_values,
                           lenVal=lenVal)


@app.route('/preNavs')
def retrieveUser1():
    return render_template('preNavs.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/preLogin')
def preLogin():
    flash('Sign Out Successful!', 'success')
    return render_template('homeUser.html')


@app.route('/homeUser')
def homeUser():
    return render_template('preLogin.html')


@app.route('/userAccount')
def user_account():
    return render_template('userAccount.html')


@app.route('/viewAccount')
def view_account():
    return render_template('viewAccount.html')


@app.route('/userHelp')
def user_help():
    return render_template('userHelp.html')


# @app.route('/UserSignUp', methods=['GET', 'POST'])
# def userSign():
#     user_sign_up_form = SignUpUser(request.form)
#     if request.method == 'POST' and user_sign_up_form.validate():
#         return redirect(url_for('home'))
#     return render_template('UserSignUp.html', form=user_sign_up_form)


@app.route('/UserSignUp', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = SignUpUser(request.form)
    if request.method == 'POST' and sign_up_form.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'c')

        try:
            signup_dict = db['SignUp']
        except:
            print("Error in retrieving Users from User.db.")

        signup = User.User(sign_up_form.first_name.data, sign_up_form.last_name.data,
                           sign_up_form.email.data, sign_up_form.address.data, sign_up_form.phone_number.data,
                           sign_up_form.unit_number.data, sign_up_form.postal_code.data, sign_up_form.password.data,
                           sign_up_form.password_confirm.data, sign_up_form.picture.data)

        uploaded_file = SignUpUser(request.files)
        f = uploaded_file.picture.data

        if f != None:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['Upload_FOLDER'], filename))
            signup.set_picture(filename)
        signup_dict[signup.get_email()] = signup
        db['SignUp'] = signup_dict
        db.close()

        flash('Sign Up Successful!', 'success')
        return redirect(url_for('login'))
    return render_template('UserSignUp.html', form=sign_up_form)


@app.route('/Login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    loginUser = Login.Login(login_form.email.data, login_form.password.data)
    user_list = []
    for key in signup_dict:
        user = signup_dict.get(key)
        user_list.append(user)
    if request.method == 'POST' and login_form.validate():
        if login_form.email.data == 'admin@gmail.com' and login_form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('view_account'))
        else:
            for x in user_list:
                if request.method == 'POST' and login_form.validate():
                    if x.get_email() == loginUser.get_email():
                        if x.get_password() == loginUser.get_password():
                            email = request.form['email']
                            session['email'] = email
                            # password = request.form['password']
                            # session['password'] = password
                            flash('Log In Successful', 'success')
                            return redirect(url_for('homeUser'))
                        else:
                            flash('Login Unsuccessful, Either Email or Password is Wrong', 'warning')
                            return redirect(url_for('login'))
            else:
                flash('Invalid Credentials, Please sign up', 'danger')
                return redirect(url_for('sign_up'))
    db.close()
    # session['user_created'] = loginUser.get_email() and loginUser.get_password()
    return render_template('Login.html', form=login_form)


@app.route('/userProfile/<email>/')
def user_Profile(email):
    print("***", email)
    show_profile_form = SignUpUser(request.form)
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    # profile_em = signup_dict.get(email=session['email'])
    # users_list = []
    profile = signup_dict.get(email)
    p_fn = profile.get_first_name()
    p_ln = profile.get_last_name()
    p_em = profile.get_email()
    p_ad = profile.get_address()
    p_ph = profile.get_phone_number()
    p_un = profile.get_unit_number()
    p_pc = profile.get_postal_code()
    print(profile.get_first_name())

    # users_list = []
    # db = shelve.open('signup.db', 'w')
    # signup_dict: dict = db['SignUp']
    #
    # for key in signup_dict:
    #     signup = signup_dict.get(key)
    #     users_list.append(signup)
    #
    # db['SignUp'] = signup_dict
    # db.close()

    return render_template('test.html', first_name=p_fn, email=profile, last_name=p_ln, pemail=p_em, address=p_ad
                           , phone=p_ph, unit=p_un, postal=p_pc)


@app.route('/updateProfile/<email>/', methods=['GET', 'POST'])
def update_profile(email):
    update_profile_form = SignUpUser(request.form)
    # if request.method == 'POST':
    if request.method == 'POST' and update_profile_form.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'w')
        signup_dict = db['SignUp']

        profile = signup_dict.get(email)
        profile.set_first_name(update_profile_form.first_name.data)
        profile.set_last_name(update_profile_form.last_name.data)
        profile.set_email(update_profile_form.email.data)
        profile.set_address(update_profile_form.address.data)
        profile.set_phone_number(update_profile_form.phone_number.data)
        profile.set_unit_number(update_profile_form.unit_number.data)
        profile.set_postal_code(update_profile_form.postal_code.data)
        # Did not include the bottom two and the request.method validate because i need the
        # to change the users password as well, so perhaps if only my update user is when user calls for support,
        # then include the bottom two
        profile.set_password(update_profile_form.password.data)
        profile.set_password_confirm(update_profile_form.password_confirm.data)

        users_list = []
        db = shelve.open('signup.db', 'w')
        signup_dict: dict = db['SignUp']

        for key in signup_dict:
            signup = signup_dict.get(key)
            users_list.append(signup)

        db['SignUp'] = signup_dict
        db.close()

        return redirect(url_for("user_Profile", email=session['email'], users_list=users_list))
    else:
        signup_dict = {}
        db = shelve.open('signup.db', 'r')
        signup_dict = db['SignUp']
        db.close()

        profile = signup_dict.get(email)
        update_profile_form.first_name.data = profile.get_first_name()
        update_profile_form.last_name.data = profile.get_last_name()
        update_profile_form.email.data = profile.get_email()
        update_profile_form.address.data = profile.get_address()
        update_profile_form.phone_number.data = profile.get_phone_number()
        update_profile_form.unit_number.data = profile.get_unit_number()
        update_profile_form.postal_code.data = profile.get_postal_code()

        return render_template('updateProfile.html', form=update_profile_form, email=session['email'])


@app.route('/userAddress')
def user_Address():
    return render_template('userAddress.html')


@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect("/")


@app.route('/retrieveUsers')
def retrieve_users():
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    db.close()

    users_list = []
    for key in signup_dict:
        user = signup_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/updateUser/<email>/', methods=['GET', 'POST'])
def update_user(email):
    update_user_form = SignUpUser(request.form)
    # if request.method == 'POST':
    if request.method == 'POST' and update_user_form.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'w')
        signup_dict = db['SignUp']

        user = signup_dict.get(email)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_email(update_user_form.email.data)
        user.set_address(update_user_form.address.data)
        user.set_phone_number(update_user_form.phone_number.data)
        user.set_unit_number(update_user_form.unit_number.data)
        user.set_postal_code(update_user_form.postal_code.data)
        # Did not include the bottom two and the request.method validate because i need the
        # to change the users password as well, so perhaps if only my update user is when user calls for support,
        # then include the bottom two
        user.set_password(update_user_form.password.data)
        user.set_password_confirm(update_user_form.password_confirm.data)
        update_user_form.password.data = user.get_password()

        db['SignUp'] = signup_dict
        db.close()
        return redirect(url_for('retrieve_users'))
    else:
        signup_dict = {}
        db = shelve.open('signup.db', 'r')
        signup_dict = db['SignUp']
        db.close()

        user = signup_dict.get(email)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.email.data = user.get_email()
        update_user_form.address.data = user.get_address()
        update_user_form.phone_number.data = user.get_phone_number()
        update_user_form.unit_number.data = user.get_unit_number()
        update_user_form.postal_code.data = user.get_postal_code()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/deleteUser/<email>/', methods=['POST'])
def delete_user(email):
    signup_dict = {}
    db = shelve.open('signup.db', 'w')
    signup_dict = db['SignUp']

    signup_dict.pop(email)

    db['SignUp'] = signup_dict
    db.close()

    return redirect(url_for('preLogin', email=email))


# Add your codes below here


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


# @app.route('/createCart/<id>' , methods=['GET', 'POST'])
# def create_cart(id):
#     create_cart_order = CreateCartOrder(request.form)
#     if request.method == 'POST' and create_cart_order.validate():
#         cart_order_dict = {}
#         db = shelve.open('cart.db', 'c')
#
#         try:
#             cart_order_dict = db['Cart']
#         except:
#             print('Error in Retrieving Products from products.db')
#
#         cart_order = Cart(create_cart_order.name.data,create_cart_order.name.data,create_cart_order.name.data,
#                           create_cart_order.name.data,create_cart_order.name.data,create_cart_order.name.data,
#                           create_cart_order.name.data)
#         print(id, cart_order)
#         cart_order_dict[cart_order.get_id()] = cart_order
#         db['Cart'] = cart_order_dict
#
#         db.close()
#
#         session['cart_created'] = cart_order.get_name()
#
#         return redirect(url_for('cart'))
#
#     else:
#         products_dict = {}
#         db = shelve.open('products.db', 'r')
#         products_dict = db['Products']
#         db.close()
#
#         product = products_dict.get[id]
#         create_cart_order.name.data = product.get_name()
#         create_cart_order.name.data = product.get_name()
#         create_cart_order.name.data = product.get_name()
#         create_cart_order.name.data = product.get_name()
#         create_cart_order.name.data = product.get_name()
#         create_cart_order.name.data = product.get_name()
#
#         return render_template("createCart.html", form=create_cart_order)


if __name__ == '__main__':
    app.run()
