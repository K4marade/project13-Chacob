# Welcome to Chacob project !


Chacob is a web application developed with [Django](https://www.djangoproject.com/) framework.  
By using this program, you will be able to search for a vet, add a pet to your account and set a reminder for your vet appointments.  
More features are to come in the near future.  
Please don't hesitate to contribute !

### Installation 

* If you're on MacOS, you can install Pipenv easily with Homebrew:

    `$ brew install pipenv`

Otherwise, refer to [Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) documentation for instructions.

* Once you installed pipenv, clone project repository and install from Pipfile:

    `$ pipenv install`


* Next, activate the Pipenv shell:

    `$ pipenv shell`
    
    This will spawn a new shell subprocess, which can be deactivated by using `exit`.  



* Read the [Django documentation](https://docs.djangoproject.com/en/3.1/) to initiate your Django project

* You can set a [Cron Task](https://phoenixnap.com/kb/set-up-cron-job-linux#:~:text=The%20Cron%20daemon%20is%20a,other%20commands%20to%20run%20automatically) for the appointment reminder, using the custom django-admin command under mycalendar/management/commands/email_alert.py:  
`python3 manage.py email_alert send_email` . 

### Usage

_From localhost:_

* From project source directory, run `python manage.py runserver`

* Go to your browser and enter your localhost url

_You can deploy on Heroku servers_

* Create an account on [Heroku](https://id.heroku.com/login) and read the [documentation](https://devcenter.heroku.com/articles/getting-started-with-python)  
You can use several tutorials on how to deploy a Django project on Heroku, like this one from MDN : 
  [Django Deployment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

_Or from other IaaS, e.g. [Digital Ocean](https://www.digitalocean.com/)_
