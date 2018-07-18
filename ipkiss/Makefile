install:
	python setup.py develop

pipenv:
	pip install pipenv
	pipenv install --dev
	pipenv shell
	python setup.py develop


dependencies:
	pip install shapely
	pip install scipy
	pip install numpy scipy matplotlib shapely nose rednose
	echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc

venv:
	python3 -m venv env
	source env/bin/activate.fish
	pip3 install -e .
