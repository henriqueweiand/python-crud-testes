from app import app

#import routes
from app.routes import *

#import models
from app.models import user

if __name__ == '__main__':
    app.run(debug=True)
