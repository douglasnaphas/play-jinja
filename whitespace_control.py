# https://jinja.palletsprojects.com/en/2.10.x/templates/#whitespace-control

from jinja2 import Template
t = Template(
"""Hello {{ name }}
"""
)
print(t.render(name="multiline"))
print("without - before %:")
print(Template(
"""{% for item in seq %}
    {{ item }}
{% endfor %}
"""
).render(seq=list(range(10))))
print("with:")
print(Template(
"""{% for item in seq -%}
    {{ item }}
{%- endfor %}
"""
).render(seq=list(range(10))))
