from django.apps import AppConfig

# app file? didn't get made with django 1.7...

class FormTestConfig(AppConfig): # Our app config class
    name = 'formtest'
    verbose_name = "Testing form generation"
