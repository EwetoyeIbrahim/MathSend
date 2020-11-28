# This file contains the WSGI configuration required to serve up your
# web application at http://www.mathsend.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.

# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
import sys
#
## The "/home/ewetoye" below specifies your home
## directory -- the rest should be the directory you uploaded your Flask
## code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
## ...or uploaded files to the directory "myproject", then you should
## specify "/home/ewetoye/myproject"
'''path = '/home/ewetoye/MathSend'
if path not in sys.path:
    sys.path.append(path)
'''
from MathSend import app as application  # noqa
#
# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.
