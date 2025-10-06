# 🧪 AQA Pytest

Este repositorio demuestra el uso de **Pytest** para **Automated Quality Assurance (AQA)** en entornos controlados con **Docker**.

---

## ⚙️ Proceso de instalación

Instala Pytest y el complemento de cobertura:

```bash
pip install pytest
pip install pytest-cov
```

---

## 🧩 Configuración de Pytest

Pytest se configura mediante el archivo `pytest.ini` ubicado en la raíz del proyecto. A continuación se describen las principales secciones y opciones que pueden incluirse:

### 🔍 Descubrimiento de tests

* **`testpaths`**: Directorios donde se buscarán los tests.
* **`python_files`**: Patrones para identificar archivos de test (por ejemplo, `test_*.py`).
* **`python_functions`**: Patrones para identificar funciones de test.
* **`python_classes`**: Patrones para identificar clases de test.
* **`norecursedirs`**: Directorios que deben ignorarse durante la búsqueda de tests.

### ⚙️ Opciones predeterminadas

* **`addopts`**: Opciones adicionales que se aplicarán automáticamente en cada ejecución (por ejemplo, `-v --maxfail=1`).
* **`minversion`**: Versión mínima requerida de pytest.

### 🏷️ Marcadores

* **`markers`**: Definición de marcadores personalizados para categorizar tests (por ejemplo, `@pytest.mark.integration`).

### ⚠️ Control de advertencias

* **`filterwarnings`**: Configuración para ignorar o mostrar advertencias específicas.

### 🧾 Configuración de logs

* **`log_cli`**: Activa o desactiva la salida de logs en consola.
* **`log_cli_level`**: Nivel de detalle de logs (`DEBUG`, `INFO`, etc.).
* **`log_format`**: Formato de los mensajes de log.
* **`log_date_format`**: Formato de fecha y hora en los logs.

### ⚡ Rendimiento y comportamiento

* **`timeout`**: Tiempo máximo de ejecución para tests (en segundos).
* **`xfail_strict`**: Define si los tests marcados como `xfail` deben considerarse fallidos si pasan.
* **`junit_family`**: Formato de salida para reportes JUnit.

### 📘 Doctest

* **`doctest_optionflags`**: Opciones para la ejecución de doctests (por ejemplo, `ELLIPSIS`, `NORMALIZE_WHITESPACE`).

---

## 🧱 Ejemplos de comandos Pytest

```ini
# Ejecutar tests con marcadores específicos
pytest -m "marca"

# Mostrar la duración de cada test
pytest --durations=0

# Detener la ejecución después del primer fallo
pytest -x

# Ejecutar tests en paralelo
pytest -n auto

# Ejecutar solo tests que fallaron en la última ejecución
pytest --last-failed

# Generar reporte XML para integración continua
pytest --junitxml=report.xml
```

---

## 🐳 Opciones de ejecución con Docker

Construye la imagen:

```bash
docker build -t pytest .
```

Levanta los servicios con Docker Compose:

```bash
docker-compose up
```

### 🧠 Comandos útiles

```bash
# Ejecutar todos los tests con salida detallada
docker-compose run --rm app pytest -v

# Mostrar cobertura de código
docker-compose run --rm app pytest --cov=app --cov-report=term-missing

# Ejecutar solo tests marcados como expected-to-fail
docker-compose run --rm app pytest -v -k xfail

# Ejecutar tests por archivo específico
docker-compose run --rm app pytest -v tests/test_auth.py

# Ejecutar una función de test específica
docker-compose run --rm app pytest -v tests/test_auth.py::test_login_success

# Mostrar información detallada de fallos
docker-compose run --rm app pytest -xvs

# Generar reporte HTML de cobertura
docker-compose run --rm app pytest --cov=app --cov-report=html
```
