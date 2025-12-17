import yaml
import pprint


if __name__ == '__main__':
	with open("index.yaml", 'r') as file:
		stuff = yaml.safe_load(file)
		pprint.pprint(stuff)
