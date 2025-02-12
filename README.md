# MCI-Test
A simple MCR system with these features:


Customer Management: CRUD operations for customers.

Product Management: CRUD operations for products.

Employee Management: CRUD operations for employees.

Task Management: CRUD operations for tasks, with filtering by status and assigned employee.

User Authentication: Register, login, and JWT-based authentication.

Admin Interface: Customizable Django admin interface for managing data.

API Documentation: Swagger UI for API documentation.


**Requirements**
Python, pip and git


**How to use my project**
1. Clone the res: (can use git bash)
   git clone https://github.com/your-username/your-repo-name.git

   cd your-repo-name
3. Create virtual environment: py -m venv venv
4. Install Libraries or Dependacies: pip install django djangorestframework djangorestframework-simplejwt drf-spectacular
Those for REST API, JWT and SWAGGER library needed for the project
5. Create database: py manage.py makemigrations then type py manage.py migrate
6. Create a superuser (or admin in django interface):  py manage.py createsuperuser
7. Run server and test: py manage.py runserver
***This tips only for beginers**
If you are new to django please use virtual environment first:
py -m venv FolderName   <==== That's to create virtual environment by using venv, which is included in Python
Now activate it:
FolderName\Scripts\activate.bat
The result should look like this:
(myworld) C:\Users\Your Name>
Then install django:
py -m pip install Django

*For prof, I  think you guys can open my folder :>
