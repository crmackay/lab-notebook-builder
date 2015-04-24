# using Jinja2


def makeExPage(experiment):
	from jinja2 import *


	my_loader = FileSystemLoader('notebook_builder/templates/')

	env = Environment(loader=my_loader)
	exp_template = env.get_template('experiment.html')

	experiment_page = exp_template.render(exp=experiment)
	return experiment_page

'''
experiment_page = exp_template.render(project='PIR 1',experiment='sdfsdfds',entries=[entry1,entry2,entry3,entry4]
'''