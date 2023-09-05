import pandas as pd
from flask import Flask, render_template, request, redirect, Response,send_file,session,url_for,flash,abort
from flask_login import current_user, login_required
from flask_login import LoginManager,current_user
from models import User, Profile
import config 
from ai_query_generator import generate_query
import os

app = Flask(__name__)

app.secret_key = config.SECRET_KEY

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        user = User(email, name, password)

        # Create the login_details table if it doesn't exist
        user.create_table()

        # Check if the email is already registered
        if user.user_exists():
            return "This email is already registered. Please use a different email."

        # Save user information in the login_details table
        user.save()

        return redirect(f'/success?email={email}')

    return render_template('register.html')


@app.route('/success')
def success():
    email = request.args.get('email')
    return render_template('success.html', email=email)

@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        name=request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        designation = request.form['designation']
        experience = int(request.form['experience'])
        tools = request.form['tools']
        area_of_interest = request.form['area_of_interest']

        profile = Profile(emp_id,name, email, gender, designation, experience, tools, area_of_interest)

        # Create the profile_details table if it doesn't exist
        profile.create_profile_table()

        # Save profile information in the profile_details table
        profile.save_profile()

        return redirect(f'/profile_updated?email={email}')

    return render_template('update_profile.html')


@app.route('/profile_updated')
def profile_updated():
    email = request.args.get('email')
    return render_template('profile_updated.html', email=email)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User(email, None, password)
        # Verify the password and check if the user exists
        if user.verify_password(password) and user.user_exists():
            #return redirect('/user_options')
            return redirect(f'/user_options?email={email}')
        else:
            return render_template('login.html', message="Invalid credentials. Please try again.")

    return render_template('login.html', message="")

@app.route('/logout')
def logout():
    # Clear the session data to log the user out
    session.clear()
    # Flash a logout success message
    flash('You have successfully logged out.', 'success')
    # Redirect the user to the login page
    return redirect('/login')


@app.route('/delete_profile', methods=['GET', 'POST'])
def delete_profile():
    if request.method == 'POST':
        email = request.form['email']
        user = User(email, None, None)
        user.delete()

        # You can also pass the email to the Profile class and delete the profile there if needed
        profile = Profile(None, None, email, None, None, None, None, None)
        profile.delete()

        flash('Profile deleted successfully.', 'success')
        return redirect('/login')

    elif request.method == 'GET':
        return render_template('user_options.html', email=request.args.get('email', ''))  # Pass the email to the template

    return "Invalid request method."

@app.route('/user_options')
def user_options():
    email = request.args.get('email', '')  # Get the email from the query parameters
    return render_template('user_options.html', email=email)  # Pass the email to the template



@app.route('/search_results', methods=['POST'])
def search_results():
    search_query = request.form['search_query']
    # Perform the search based on the entered query
    profiles = Profile.perform_search(search_query)
    return render_template('search_results.html', profiles=profiles)

# Global variable to store the search results
search_results_data = []

@app.route('/search_profiles', methods=['GET', 'POST'])
def search_profiles():
    global search_results_data
    if request.method == 'POST':
        search_query = request.form['search_query']
        # Perform the search based on the entered query
        search_results_data = Profile.perform_search(search_query)
        profiles = Profile.perform_search(search_query)
        # Redirect to the /export_excel route with the search query as a parameter
        return redirect(f'/export_excel?search_query={search_query}')
        #return render_template('search_results.html', profiles=profiles)

    return render_template('search_profiles.html')

@app.route('/export_excel', methods=['GET', 'POST'])
def export_excel():
    global search_results_data

    # If the request is POST, use the data from the search_results_data
    if request.method == 'POST':
        # Create a DataFrame from the profiles list
        df = pd.DataFrame(search_results_data, columns=['Employee ID', 'Name', 'Email', 'Gender', 'Designation', 'Experience', 'Tools', 'Area of Interest'])

        # Convert DataFrame columns to string type
        df = df.astype(str)

        # Specify the columns we want to include in the Excel file
        columns_to_include = ['Employee ID', 'Name', 'Email', 'Gender', 'Designation', 'Experience', 'Tools', 'Area of Interest']

        # Convert filtered DataFrame to Excel file
        excel_file_path = 'search_results.xlsx'
        df[columns_to_include].to_excel(excel_file_path, index=False)

        return send_file(excel_file_path, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', as_attachment=True)

    # If the request is GET and the URL has the 'search_query' parameter
    # Use it to display the search results on the search_results.html page
    search_query = request.args.get('search_query', '')
    if search_query:
        return render_template('search_results.html', profiles=search_results_data)

    # If no 'search_query' parameter is provided in the URL, return an empty response or handle it as you wish
    return "No search query provided."

@login_manager.user_loader
def load_user(email):
    # Load the user from the User model based on the email
    return User.get_by_email(email) 


@app.route('/problem', methods=['GET', 'POST'])
def search_problem():
    if request.method == 'POST':
        search_input = request.form['search_input']
        # Call the generate_query method from a.py with the user's search input as an argument
        problem_query = generate_query(search_input)
        # Execute the generated query and fetch data from the profile_details table
        results = Profile.execute_query(problem_query)
        if results:
            # If there are search results, pass them to the template
            return render_template('search_problem.html', results=results)
        else:
            # If no results are found, display an error message
            return render_template('search_problem.html', error_message="No results found.")

    return render_template('search_problem.html')



# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
