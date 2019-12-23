# https://jinja.palletsprojects.com/en/2.10.x/templates/#macros
from jinja2 import Template
print(Template(
"""{% macro m1(in1) -%} saying {{ in1 }} within a macro {%- endmacro %}{{ m1("x") }}
"""
).render(in1='hello'))
