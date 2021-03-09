install:
	pipenv install -e .
	pipenv shell
qa: format lint typecheck test
test:
	pipenv run test
lint:
	pipenv run lint
format:
	pipenv run format
typecheck:
	pipenv run typecheck
dev:
	pipenv install --dev
