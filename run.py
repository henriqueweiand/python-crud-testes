from app import app

#import routes
from app.routes import *

if __name__ == '__main__':
    app.run(debug=True)
