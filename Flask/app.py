# imports
from flask import Flask, render_template, request, flash, redirect, url_for
'''
    1. create an instance of the Flask
    2. WSGI(Web Server Gateway Interface) application
'''
# step-1: initialize the app
app = Flask(__name__)

# step-2: Create a basic route
@app.route("/")  # @ is a decorator for define the route
def welcome():
    return "Welcome to this world of flask"

@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return render_template('about.html')


# for CRUD operations
@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')  # Using get() to handle missing keys gracefully
        description = request.form.get('description')
        link = request.form.get('link')

        if not name or not description or not link:
            flash("All fields are required. Please fill out the form completely.", "error")
            return redirect(url_for('form'))

        return (f"<h2>Thank you, {name}!</h2>"
                f"<p>Your project has been successfully uploaded.</p>"
                f"<p><strong>Description:</strong> {description}</p>"
                f"<p><strong>Project Link:</strong> <a href='{link}' target='_blank'>{link}</a></p>")
    
    return render_template('form.html')


# start or entry point of this project
if __name__ == "__main__":
    app.run(debug=True)  # debug for alawys update without restart