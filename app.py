from flask import Flask, render_template, redirect, url_for, session
from Model.Server import User, Instances
from flask_oauth import OAuth

# GLOBAL DECLARATIONS

GOOGLE_CLIENT_ID = '1021204286636-jv2mrvtn5fl4et2fmau6hkan8rridu65.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'S9YxrnE0nn7hP6Ie75TcvW9Y'
REDIRECT_URI = '/loggedin'

SECRET_KEY = 'development key'

app = Flask(__name__)
app.secret_key = SECRET_KEY
oauth = OAuth()

google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)


@app.route('/')
def index():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError

    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()

    return res.read()


@app.route('/login')
def login():
    callback = url_for('authorized', _external=True)
    return google.authorize(callback=callback)


@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))


@google.tokengetter
def get_access_token():
    return session.get('access_token')


# @app.route("/")
# def home():
#     return render_template("home.html")


# @app.route("/login")
# def login():
#     return render_template("login.html")


# @app.route("/admin")
# def admin():
#     return render_template("admin.html")


if __name__ == "__main__":
    app.debug = True
    app.run(ssl_context=('cert.pem', 'key.pem'))
