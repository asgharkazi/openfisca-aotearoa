all: test

uninstall:
	pip freeze | grep -v "^-e" | xargs pip uninstall -y

clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

deps:
	pip install --upgrade pip build twine

install: deps
	@# Install OpenFisca-Aotearoa for development.
	@# `make install` installs the editable version of OpenFisca-Aotearoa.
	@# This allows contributors to test as they code.
	pip install --editable ".[dev]" --upgrade
	pip install --editable git+https://github.com/openfisca/openfisca-core.git@add-weeks#egg=OpenFisca-Core[web-api]

build: clean deps
	@# Install OpenFisca-Aotearoa for deployment and publishing.
	@# `make build` allows us to be be sure tests are run against the packaged version
	@# of OpenFisca-Aotearoa, the same we put in the hands of users and reusers.
	python -m build
	find dist -name "*.whl" -exec pip install --force-reinstall {}[dev] \;

check-syntax-errors:
	python -m compileall -q .

format-style:
	@# Do not analyse .gitignored files.
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	pyupgrade `git ls-files | grep "\.py$$"`
	autopep8 `git ls-files | grep "\.py$$"`

check-style:
	@# Do not analyse .gitignored files.
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	flake8 `git ls-files | grep "\.py$$"`
	pylint `git ls-files | grep "\.py$$"`


test: clean check-syntax-errors
ifdef yaml
	openfisca test -c openfisca_aotearoa openfisca_aotearoa/tests/$(yaml)
else
	openfisca test --country-package openfisca_aotearoa openfisca_aotearoa/tests
endif

serve:
	openfisca serve --country-package openfisca_aotearoa -b 0.0.0.0:5000 --reload

lint:
	yamllint . && flake8
