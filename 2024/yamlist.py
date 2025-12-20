import pprint

import yaml

if __name__ == '__main__':
	with open("index.yaml") as file:
		stuff = yaml.safe_load(file)
		pprint.pprint(stuff)
