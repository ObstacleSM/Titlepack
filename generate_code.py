#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
import importlib

def gen_lib(env, name):
	module = importlib.import_module(f'Scripts.Libs.smokegun.{name}')
	template = env.get_template(f'./Scripts/Libs/smokegun/{name}.tmpl')
	output = template.render(module.model)

	output = f'// Generated from {name}.py and {name}.tmpl' + output

	with open(f'./Scripts/Libs/smokegun/{name}.Script.txt', 'w') as file:
		print(output, file=file)



if __name__ == "__main__":
	env = Environment(loader = FileSystemLoader(''),   trim_blocks=True, lstrip_blocks=True)
	gen_lib(env, 'Settings')