# django-girls-blog

If you are working in WINDOWS OS then do follows these steps -

If you want to work on some other django projects. You should follow steps stated below

1. Download and Install Python required version on your OS.
   
   https://www.python.org/downloads/

2. Install pip 

  $ python -m pip install --upgrade pip


Note: Make sure you have added python and pip in environment variables.

3. Read about virtualenv in Python. Create a virtual environment for your project.
Activate the environment in cmd.

4. Clone the GitHub project in your local directory with command git clone https://github.com/praveenup/nakshatra.git

5. Run the command in console 
    
    $ pip install -r requirements.txt 
    
Note: if requirements.txt is present in the current directory otherwise go to that directory and run the above command. 
      This command will install the necessary packages required to run the project.

6. Go the the directory where Django project is present and manage.py file is present.

7. Run following commands in the cmd
    
    $ python manage.py makemigrations  
    
    $ python manage.py migrate    //to make database tables
    
    $ python manage.py runserver

8. See if your project is running on your local host http://127.0.0.1

