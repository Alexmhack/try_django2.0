1. create a folder for your project

2. create virtaulenv inside the folder using
	
	> env virtualenv

3. before installing any module don't forget to activate the venv

	> env\Scripts\activate

4. install the version of django you want to work with using pip

	> pip install django==2.0.7
	django latest is the 2.0.8

5. to check the modules installed with their versions

	> pip freeze

6. To find the version of django and any other modules from the terminal then run

	> python -c "import django; print(django.VERSION)"

7. if everything does not go as planned then delete the virtualenv folder and recreate everything

8. THREE WAYS TO CREATE virtualenv

	> virtualenv env
	> virtualenv env -p python3 or python2
	> virtualenv env-p <path to python version>
	> virtualenv . -p python3

9. create a django project using the command

	> cd project-folder
	> env\Scripts\activate
(env)> django-admin startproject trydjango

10. to run the server for you django project

	> cd trydjango
	> python manage.py runserver

11. on running the server you can see some errors saying to migrate the project, you can migrate
	using the command

	> python manage.py migrate

12. you can visit the admin site by placing admin after the main url, but you have to create the 
	admin for your project first using the command

	> python manage.py createsuperuser
	fill in the form and press enter, fill those details in the admin site and you are in!

13. Now to create a app, here app means a web app in your project,

	> python manage.py startapp products
	here 'products' is the name of our app

14. Then in the products app, we have created a Product class inside the models.py, for our 
	products app which has fields for many purposes

15. now to tell django that our app exists we need to add the 'products' in the INSTALLED_APPS
	of our settings.py and after that you need to makemigrations

	> python manage.py makemigrations
	> python manage.py migrate

16. now we again make changes to our models and add a summary field, and run the makemigrations
	again, this would ask us for adding a default value, there we enter 2 for second option and
	inside the summary text field we make a default value of any text, and run the makemigrations
	again.

17. If we make any changes inside the models of our apps we need to run makemigrations and migrate
	both in sequence

18. Now for our models to reflect in the admin site we need to register our models in the admin.py

19. We use the python django shell that tinkers around with our apps, you can run shell using

	> python manage.py shell
	>>> from products.models import Product
	here we are importing the Product class from our products app which has models in it

	you access many things from shell API like fetching all the Product objects

	>>> Product.objects.all()
	>>> Product.objects.create(title='', description='', price='', summary='')

20. you can also delete the sqlite db and any files inside the migrations folder except the init.py
	file, this can be done for checking purposes

21. Now we are changing the Field in our models.py class and referencing the django docs
	https://docs.djangoproject.com/en/2.0/ref/models/fields/#decimalfield

22. you can set the models fileds null = True to make those fields left with no value at all
	or else you can set the default value which will be there whenever you create an object

	default='some default value' for BooleanField default will be True/False

	you can code the default value or let django do that when it asks for a prompt for a default
	value for the field, run makemigrations after making changes in the code and prompt will appear

23. When we set any field with blank=True that field becomes less important in the form, or that
	field is not bold anymore in the admin site, whereas blank=False sets the field bold, you
	can set null=True so that the field is not null anymore

24. blank option in the field is related to how form is rendered, and null is related to DB
	null=True means that DB value for that field can be zero/null in the database and vice-versa

25. you can create URLS and URL ROUTING using the urls.py in the main folder, but first you have	to create a view for the url, that view goes into views.py in form of a function and then place
	the url in the urls.py with the function from the views

26. If we print the request that is argument to our view function then we can see the request that
	is passed for the request of the view and we can also look at the user that is logged in by
	printing the request.user

27. now we create templates, first we direct our view function to the html page and then we create
	a html file but we need to tell django all this, for that we tell django the path to our 
	templates inside the settings.py file

28. then we use extends tag in the html files and extend the base.html file and include the
	navbar.html in the base.html itself, this is very useful when our project gets bigger

29. We can also use context of the django render, which is a dict and then show the values
	of the dict in html using template tags, the forloop.counter shows the count of item in list

30. templates can also have if else tags, elif tags, tag filters like |add:100 which adds 100

31. |safe filter renders html in html format, |capfirst, |upper, |title, |slugify slugifies text
	check the docs for templates filter in django

32. Inside the interactive shell you can look import the Product model and then store the first
 	Product object in a variable and dir(var) to get all the methods we have for the object

 	>>> from products.models import Product
 	>>> obj = Product.objects.get(id=1)
 	>>> dir(obj)

33. Now we will render the context by getting data from our database for our products views
	we can render our context and send our object with it and then use the .description, 
	.title of the object, we can also put a if tag for description

34. 