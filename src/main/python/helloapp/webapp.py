from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    
    application.logger.info('/')
    # Render default page template
    return render_template('index.html')