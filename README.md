# serve_mpt
Quantize and Servie the MPT-7B models from Mosaic ML, Inc.

## Installation

Dependencies:
- [Python](https://www.python.org/)

Install the Python dependencies using the following commands:
```bash
python -m pip install virtualenv
python -m venv venv
```
If you are using windows:
```bash
venv\Scripts\activate
```
On linux-based systems:
```bash
source venv/bin/activate
```
Install the requirements:
```bash
python -m pip install -r requirements.txt
```
Install for development:
```bash
python -m pip install -e .
```

## Usage

### Manual Usage

You start and use the FastAPI app manually with the following commands:
```bash
python src/serve_mpt/main.py
```
```bash
uvicorn src.serve_mpt.main:app --reload
```
This starts a webserver at [`http://127.0.0.1:8000`](http://127.0.0.1:8000) with OpenAPI documentation [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) and ReDoc docs at [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc).