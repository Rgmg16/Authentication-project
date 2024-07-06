from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername', 'myemail@mail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'Ezekiel'
user.last_name = 'Kibiego'
user.save()