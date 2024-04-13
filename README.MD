# Django ChatApp

A simple Chat App with user registration and a chat window

## Table of Contents

- [Django ChatApp](#django-chatapp)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
- [Installing a Basic Django Project](#installing-a-basic-django-project)
  - [Usage](#usage)

## Installation

# Installing a Basic Django Project

Follow these steps to set up a basic Django project using the `requirements.txt` file:

1. **Install Python**:
   Ensure Python is installed on your system. Download it from [python.org](https://www.python.org).

2. **Create a Virtual Environment**:
   Open your terminal or command prompt, navigate to your project directory, and run the following command to create a virtual environment named *myenv*.
   
   ```
   python -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   - For Windows:
     ```myenv\Scripts\activate```
   - For macOS/Linux:
    ```source myenv/bin/activate```
  
4. **Install Required Packages**:
   Install the packages specified in the `requirements.txt` file by running: `pip install -r requirement.txt?` This will install all the necessary packages and dependencies specified in the requirement.txt file.

5. **Create a Django Project**:
   Create a new Django project named `myproject` by running: `django-admin startproject myproject` . This will create a new Django project named myproject.

6. **Navigate to the Project Directory**:
   Change into your project directory by running: `cd myproject`

7. **Run the Django Development Server**:
   Start the development server by executing: `python manage.py runserver`

   You should see output indicating that the server is running.

8. **Verify Installation**:
   Open your web browser and visit `http://localhost:8000`. You should see the default Django welcome page, confirming a successful installation.


## Usage

On the homepage `http://127.0.0.1:8000/` click "Register" to register a user in the Django DB. Then click "back to login" to login. 
Now you can start chatting.


