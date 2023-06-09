# Copyright 2023 Louis Wendler

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import logging
import argparse

import uvicorn

from fastapi import FastAPI

from serve_mpt.llm import generate
from serve_mpt.utils import (
    LLMParameters,
    DEFAULT_MODEL_CONFIG_PATH,
    DEFAULT_GENERATION_CONFIG_PATH
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# Create the FastAPI app instance
app = FastAPI()


@app.post("/")
async def root(params: LLMParameters):
    return generate(params)


def argument_parser() -> argparse.ArgumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_config",
        default="src/serve_mpt/configs/models/default.json",
        type=str,
        help="The path to a default model config file."
    )
    parser.add_argument(
        "--generation_config",
        default="src/serve_mpt/configs/generation/default.json",
        type=str,
        help="The path to a default generation config file."
    )
    parser.add_argument(
        "--cache",
        default=".cache",
        type=str,
        help="The path to the cache directory."
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        type=str,
        help="The host address of the local gradio server."
    )
    parser.add_argument(
        "--port",
        default=8000,
        type=int,
        help="The port of our local gradio server."
    )

    return parser


def main() -> None:
    parser = argument_parser()
    args = parser.parse_args()
    logger.info(f"Starting frontend with args:\n{json.dums(vars(args), indent=2)}")

    global DEFAULT_MODEL_CONFIG_PATH
    DEFAULT_MODEL_CONFIG_PATH = args.model_config
    global DEFAULT_GENERATION_CONFIG_PATH
    DEFAULT_GENERATION_CONFIG_PATH = args.generation_config

    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == '__main__':
    main()
