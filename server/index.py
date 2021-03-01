from flask import Flask
app = Flask(__name__)

@app.route('/v1/health')
def health_check():
    return 'Health check passed!'

@app.route('/v1/runtime/new')
def health_check():
    print('Creating new runtime')
    return 'Created new runtime'
    
@app.route('/v1/runtime/terminate')
def health_check():
    print('Terminating runtime')
    return 'Terminated runtime'