# AQA Pytest
## Proceso de instalación

```bash
docker build -t pytest .
```
```bash
docker-compose up
```
```bash
# Run all tests with verbose output
docker-compose run --rm app pytest -v

# Show test coverage
docker-compose run --rm app pytest --cov=app --cov-report=term-missing

# Run only expected-to-fail tests
docker-compose run --rm app pytest -v -k xfail

# Run tests by test file
docker-compose run --rm app pytest -v tests/test_auth.py

# Run a specific test function
docker-compose run --rm app pytest -v tests/test_auth.py::test_login_success

# Show detailed failure information
docker-compose run --rm app pytest -xvs

# Generate HTML report
docker-compose run --rm app pytest --cov=app --cov-report=html
```