# EG3 — Librería de Gestión de Cuentas Bancarias (uc3m_money)

## Descripción

Librería Python (`uc3m_money`) que implementa la lógica de negocio de un pequeño sistema bancario, construida siguiendo un diseño en capas con validación estricta de los datos de entrada y una suite de **pruebas unitarias** extensa. Expone tres operaciones principales a través de un `AccountManager` implementado como **Singleton**:

- **`transfer_request`** — Registra una solicitud de transferencia entre dos IBAN (importe, concepto, tipo y fecha), validando cada campo y generando un código de transferencia único.
- **`deposit_into_account`** — Registra un ingreso a partir de un fichero JSON de entrada, firmando el depósito con un hash **SHA-256** sobre sus datos (algoritmo, tipo, IBAN, importe y fecha).
- **`calculate_balance`** — Calcula el saldo de un IBAN a partir del histórico de transacciones almacenado.

## Arquitectura

```
src/main/python/uc3m_money/
├── account_manager.py               # Fachada / Singleton con las 3 operaciones públicas
├── account_deposit.py               # Modelo de un depósito (incluye firma SHA-256)
├── transfer_request.py              # Modelo de una solicitud de transferencia
├── iban_balance.py                  # Cálculo de saldo a partir del histórico de transacciones
├── account_management_exception.py  # Excepción de dominio
├── account_management_config.py     # Configuración (rutas de los ficheros de almacenamiento)
├── data/attr/                       # Value Objects con validación de cada atributo:
│   ├── iban_code.py                 #   IBAN (formato y dígito de control)
│   ├── deposit_amount.py            #   Importe de depósito
│   ├── transfer_amount.py           #   Importe de transferencia
│   ├── transfer_type.py             #   Tipo de transferencia
│   ├── transfer_date.py             #   Fecha de la transferencia
│   └── concept.py                   #   Concepto de la transferencia
└── storage/                         # Persistencia en ficheros JSON
    ├── json_store.py                #   Clase base de almacenamiento
    ├── transfer_json_store.py
    ├── deposits_json_store.py
    └── balances_json_store.py
```

Cada dato de entrada (IBAN, importe, fecha, tipo, concepto...) se modela como un **value object independiente** en `data/attr/`, responsable de validar su propio formato y lanzar `AccountManagementException` si no es correcto. Esto permite testear cada regla de validación de forma aislada.

## Pruebas

El proyecto incluye una suite de **pruebas unitarias** (`src/unittest/python/`) muy completa, con decenas de ficheros JSON de prueba (`src/unittest/JSONFiles/`) que cubren tanto casos válidos como distintas formas en que un fichero de depósito puede estar mal formado (claves duplicadas, eliminadas, modificadas, comillas o comas incorrectas, importes a cero...), siguiendo un enfoque de **pruebas basadas en mutación de datos**:

- `test_calculate_balance_tests.py`
- `test_deposit_tests.py`
- `test_singleton_tests.py`
- `test_transfer_request_tests.py`

## Build y ejecución

El proyecto usa **[PyBuilder](https://pybuilder.io/)** como sistema de construcción (`build.py`, `pyproject.toml`).

```bash
pip install -r requirements.txt

# Construir el proyecto y ejecutar los tests + cobertura
python build.py
```

## Tecnologías

- Python 3
- PyBuilder (build, tests y cobertura)
- `pylint` para el análisis estático de estilo de código
- `freezegun` para controlar el tiempo en los tests
- Persistencia simple en ficheros JSON


## Documentación adicional

`doc/doc.docx` contiene la memoria/documentación de diseño entregada para esta práctica.
