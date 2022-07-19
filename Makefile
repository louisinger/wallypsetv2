env:
	python3.9 -m venv venv

deps:
	pip install pytest wallycore-0.8.5-cp39-cp39-linux_x86_64.whl

test:
	pytest -s