# Employee Self Care System

The Employee Self Care System is a web application designed to empower employees to manage their profiles and well-being efficiently. It's built using Python, Flask, PostgreSQL, and integrates ChatGPT for advanced query generation.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Integrating ChatGPT](#integrating-chatgpt)
- [Contributing](#contributing)
- [License](#license)

## About

The Employee Self Care System simplifies the process of employees managing their profiles and accessing resources related to their well-being. It offers features like profile creation, updates, login, and a comprehensive search engine to find resources and colleagues.

Key features include:

- User registration and login.
- Profile creation and updates.
- Advanced resource search functionality.
- Export search results to Excel.
- Employee profile deletion.
- ChatGPT integration for query generation.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- PostgreSQL installed and running.
- [Prerequisite 3]

### Installation

To install and run the Employee Self Care System, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/employee-self-care-system.git

2. Navigate to the project directory:
   cd employee-self-care-system
3. Create a virtual environment:
   python3 -m venv venv
4. Activate the virtual environment:
On Windows:
    venv\Scripts\activate
On macOS and Linux:
  source venv/bin/activate
5. Install the project dependencies:
   pip install -r requirements.txt
  
6. Set up the database:
    Create a PostgreSQL database and update the database configuration in config.py.

7. Initialize the database:
  python manage.py db init
  python manage.py db migrate
  python manage.py db upgrade

9. Start the Flask application:
    flask run
   
The application should now be running locally. Open your web browser and visit http://localhost:5000 to access the Employee Self Care System.

### Usage

Here's how you can use the Employee Self Care System:

1. User Registration: Employees can register by providing their email, name, and password.
2. User Login: Registered users can log in to their accounts.
3. Profile Creation/Update: Users can create and update their profiles, including details like employee ID, name, email, gender, designation, experience, tools, and area 
  of interest.
4. Advanced Resource Search: Users can search for resources based on various criteria, making it easier to find the information they need.
5. Export Search Results: Users can export search results to an Excel file for further reference.
6 .Profile Deletion: Users can delete their profiles.

### Integrating ChatGPT

The Employee Self Care System leverages ChatGPT for advanced query generation. Here's how it works:

  - When a user wants to search for specific resources or information (e.g., Python problems), they can interact with ChatGPT.

  - ChatGPT generates complex search queries based on the user's natural language input.

  - The generated query is then executed, and profile details are fetched from the database.

  - This integration enhances the user experience by allowing them to use conversational language to find the information they need.
    
### Features
    1.User registration and authentication.
    2.Employee profile management.
    3.Advanced resource search with multiple filters.
    4.Export search results to Excel.
    5.User-friendly web interface.
    6. ChatGPT integration for natural language query generation.
    
### Contributing

We welcome contributions from the community to enhance the Employee Self Care System. To contribute, follow these steps:

    1.Fork the project.
    2.Create a new branch for your feature or bug fix.
    3.Make your changes and commit them.
    4.Push to your fork and submit a pull request.

Please read CONTRIBUTING.md for more details on our code of conduct and the process for submitting pull requests.
### License

This project is licensed under the MIT License.
