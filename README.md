Random User Data Generator

This repository hosts a Random User Data Generator web application, built using Flask. The application allows users to generate random dummy data, such as names, email addresses, phone numbers, and more. The user can also select specific types of data to generate, all of which is stored in a CSV file for future use.

Table of Contents
  Features
  Demo
  Installation
  Usage
  Technologies Used
  Contributing
  License
  Contact
  Features
Generate Random Data: Supports generating various types of user data like names, emails, addresses, phone numbers, job titles, and more.
Customizable Selection: Users can select the types of data they want to generate.
Export to CSV: The generated data is saved as a CSV file for easy download and use.
Country-Specific Data: Data can be generated for specific countries, such as the United States, India, Germany, and more.
Responsive Design: The web interface is mobile and desktop friendly with intuitive styling.

Demo
A live demo of the project is available Render .

Installation
Prerequisites
Python 3.x
Flask and other dependencies (listed in requirements.txt)
Steps to Run Locally

Clone the repository:
git clone https://github.com/120-Eye/random-user-data-generator.git

Navigate to the project directory:


cd random-user-data-generator
Create a virtual environment:

python3 -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Run the Flask app:

python main.py
Access the app in your browser: Open http://127.0.0.1:5000/ to see the application running.

Usage
Select the data types: Choose the types of random data to generate (e.g., name, email, address).
Choose the number of users: Input how many users’ data you want to generate.
Select a country: Choose the country from which the data will be generated (e.g., US, India).
Download the CSV: Once the data is generated, it will be available to download in CSV format.


Technologies Used
Flask: Web framework used to build the application.
HTML/CSS: Frontend design and layout.
Faker: Python library to generate random data.
CSV: Export data in a structured, easy-to-use format.
GitHub: Version control and code hosting.
Contributing
Contributions are welcome! If you'd like to make improvements or fix bugs, feel free to submit a pull request.

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions, feedback, or suggestions, please reach out:

GitHub: @120-Eye
