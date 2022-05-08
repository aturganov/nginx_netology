from flask import Flask
app = Flask(__name__)

@app.route("/")
def hey():
    html = '''
        <html>
            <head>
            Hey, Netology
            </head>
            <body>
            <h1>I’m DevOps Engineer!</h1>
            </body>
        </html>
    '''
    return html

if __name__ == "__main__":
    app.run(port=5002, host='0.0.0.0')