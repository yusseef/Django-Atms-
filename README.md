# Django-Atms
 Atms is python & django app for tracking employees.
 
 ## Installation
   *Install [python](https://www.python.org/downloads/release/python-391/)
 
 
   *Create your venv in the same directory of the project : 
 ```
python -m venv .
```

   *open the project with vscode or any idle.
   
   
   *open the terminal and activate venv :
     ```
     ./Scripts/activate .
                    ```
                    
   *install the requirments:
     ```
      pip install requirments.txt
                    ```
                    
                    
   *make the migrations:
      ```
      python manage.py makemigrations
                    ```
                    
     
   *migrate:  
     ```
      python manage.py migrate
                    ```
   
   
   
   *run the server:
       ```
      python manage.py runserver
                    ```


                     <div class="container">
        <div class="col-md-10 offset-md-1 mt-5">
            <div class="jumbotron">
                
                <hr class="my-4">
                {% block content %} 
                {% endblock content %}
              </div>


        </div>


    </div>
     

 
