# https://jinja.palletsprojects.com/en/2.10.x/intro/#basic-api-usage

from jinja2 import Template
template = Template('Hello {{ name }}')
print(template.render(name='user')) # prints "Hello user"
