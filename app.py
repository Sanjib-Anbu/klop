from flask import Flask, render_template, request

app = Flask(__name__)

# Global variable to store submitted text
submitted_text = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global submitted_text
    submitted_text = request.form['text']
    # Returning HTML with a GIF and border radius, shadow
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Submission Successful</title>
        <style>
            body {
                background-color: #ffeeba;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #ffffff;
                padding: 20px;
                text-align: center;
                border-radius: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h2 {
                margin-bottom: 20px;
            }
            img {
                border: 2px solid #333;
                border-radius: 10px; /* Adjust border radius as needed */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Text submitted successfully!</h2>
            <img src="https://i.pinimg.com/originals/2e/9d/5a/2e9d5aa87bf57a6047d49f1f3efcc9ad.gif" alt="GIF">
        </div>
    </body>
    </html>
    '''

@app.route('/view')
def view():
    return render_template('view.html', submitted_text=submitted_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
