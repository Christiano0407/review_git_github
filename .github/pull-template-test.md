---
name: "Pull Request Test To Fast API"
about: Template To Explain all Process in an PullRequest To API With FastAPI and Python
title: "PullRequest Testing"

---

# ✅ Pruebas Automatizadas y Corrección de Bug en FastAPI

Este documento describe el proceso para realizar pruebas a la API desarrollada en FastAPI, así como la detección y corrección de un bug relacionado con `response_model` y el uso correcto de `HTTPException`.

---

## 🗂️ Estructura del Proyecto

backend/
├── init.py
├── api/
│ ├── init.py
│ └── api_python.py ← Contiene la aplicación FastAPI
└── test/
├── init.py
└── test_api.py ← Contiene las pruebas automatizadas

yaml
Copiar
Editar

---

## ⚙️ Dependencias necesarias

Instala `pytest`, `fastapi` y `httpx` con:

```bash
pip install pytest fastapi httpx

> Passed Test

```bash
collected 6 items

backend/test/test_api.py::test_read_root               PASSED
backend/test/test_api.py::test_read_items              PASSED
backend/test/test_api.py::test_read_item_found         PASSED
backend/test/test_api.py::test_read_item_not_found     PASSED ✅
backend/test/test_api.py::test_create_item             PASSED
backend/test/test_api.py::test_calculate_total         PASSED
