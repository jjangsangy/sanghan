init:
	pip install -r requirements.txt

test:
	nosetests

.PHONY: clean

build:
	python setup.py build

publish:
	git push

clean:
	rm -rf app/*.pyc
	rm -rf app/__pycache__
	rm -rf *.pyc
	rm -rf __pycache__
	rm -rf *egg-info
