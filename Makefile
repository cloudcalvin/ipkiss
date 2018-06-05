install:
	python setup.py develop

test:
	pytest

pipenv:
	pip install pipenv
	pipenv install --dev
	pipenv run python setup.py develop

activate:
	pipenv shell

dependencies:
	pip install shapely
	pip install scipy
	pip install numpy scipy matplotlib shapely nose rednose
	echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc

python-user:
	sudo chown -R $USER /usr/local
