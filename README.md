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

### Configuration

We try to make this project as modular and configurable as possible. We also provide configuration files to lower the barrier of entry. We provide the configuration for:

- The generation process
- Selecting the your PLM

You can set the generation config by providing a generation config JSON file. A general (default) example is the [generation/default.json](src/serve_mpt/configs/generation/default.json) file. Generation config files consist of key-value-pairs based in the [ctransformers generation config](https://github.com/marella/ctransformers#config).

Model config files are used to load our PLM. Each JSON model config file has 3 fields and follows the layout outlined below:
```json
{
    "name": "name_of_your_model",
    "path": "/path/to/your/model",
    "type": "mpt"
}
```

Default values for the mentioned configurations can be set with the `--model_config` and `--generation_config` flags of our [`main.py`](src/serve_mpt/main.py) script.

### Manual Usage

You start and use the FastAPI app manually with the following commands:
```bash
python src/serve_mpt/main.py
```
```bash
uvicorn src.serve_mpt.main:app --reload
```
This starts a webserver at [`http://127.0.0.1:8000`](http://127.0.0.1:8000) with OpenAPI documentation [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) and ReDoc docs at [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc).

### Usage with Docker Compose

You can start the FastAPI app by executing something like the following commands:
```bash
docker compose build
docker compose up
```


## Quantization

Quantization is a useful technique if you want to serve a large PLM with a small budget. We provide some examples on how to quantize and use the MPT models. Check out our:
- [Colab notebook](examples\notebooks\run_quant_mpt_with_ctransformers.ipynb) for MPT quantization with [ggml](https://github.com/ggerganov/ggml)