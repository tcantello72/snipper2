Set-up to run this app

Steps:
    1. From the command prompt run python -V If you get a version back you can skip
       to step 3

    2. If you got a message that python wa not found. Go to http://www.python.org and 
       download the lastest version of Python. Follow the install instructions on the site. Make sure to click the Add to PATH when asked.

    3. Clone the repo

    4. Open the repo in your IDE. The IDE that I used was Visual Studio Code

    5. Open a terminal to the command prompt and make sure you are in the root folder
       for the project when you do

    6. Now we need to set-up the virtual environment. At the command prompt run 
       pip install virtualenv

    7. Then run py -m venv venv (the second venv can be whatever you want to name the 
       virtual environment)

    8. To activate the virtual environment at the command prompt run 
       .\venv\Scripts\activate  (replace the venv with the name you gave the virtual environment) 
       Once the virtual environment is active you will see the name of your virtual environment 
       in front of the command prompt.

    9. Now that the virtual environment is active we need to install the required
       packages for this app. Now run pip -r requirements.txt

    10. After all the packages install you can run py app.py  This will start the app on the local server.
        Type the address of the local server in the browser. Will see a messages welcoming you to the 
        The API.

    11. Now in the address bar add /api/ui to the end of the URL. This will allow you to access the user 
        interface for the API allowing you to run all CRUD operations on the API

