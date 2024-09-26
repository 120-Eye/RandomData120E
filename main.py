from flask import Flask, render_template, request, send_file
import pandas as pd
from faker import Faker

app = Flask(__name__)


def generate_random_user_data(num_users, selected_fields, locale):
    fake = Faker(locale)  
    data = []

    for _ in range(num_users):
        user_data = {}
        if 'name' in selected_fields:
            user_data['Name'] = fake.name()
        if 'email' in selected_fields:
            user_data['Email'] = fake.email()
        if 'address' in selected_fields:
            user_data['Address'] = fake.address()
        if 'phone_number' in selected_fields:
            user_data['Phone Number'] = fake.phone_number()
        if 'job' in selected_fields:
            user_data['Job'] = fake.job()
        if 'company' in selected_fields:
            user_data['Company'] = fake.company()
        if 'birthdate' in selected_fields:
            user_data['Birthdate'] = fake.date_of_birth()
        if 'username' in selected_fields:
            user_data['Username'] = fake.user_name()
        if 'ssn' in selected_fields:
            user_data['SSN'] = fake.ssn()

        data.append(user_data)

    return data

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate the CSV file and allow download
@app.route('/generate', methods=['POST'])
def generate():
    num_users = int(request.form['num_users'])
    selected_fields = request.form.getlist('fields')  # Get selected fields
    country = request.form['country']  # Get the selected country/locale

    user_data = generate_random_user_data(num_users, selected_fields, country)

    # Convert to DataFrame
    df = pd.DataFrame(user_data)

    # Save the data to a CSV file
    csv_file = 'dummy_user_data.csv'
    df.to_csv(csv_file, index=False)

    # Provide the file for download
    return send_file(csv_file, as_attachment=True)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
