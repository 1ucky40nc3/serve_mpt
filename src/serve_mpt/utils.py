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

from typing import (
    Any,
    List,
    Dict,
    Callable
)

import json
from inspect import signature

from pydantic import BaseModel


DEFAULT_MODEL_CONFIG_PATH = "src/serve_mpt/configs/models/default.json"
DEFAULT_GENERATION_CONFIG_PATH = "src/serve_mpt/configs/generation/default.json"


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_model(path: str, model: BaseModel, **kwargs) -> BaseModel:
    data = load_json(path)
    return model(**{**data, **kwargs})


class GenerationConfig(BaseModel):
    top_k: int = 40
    top_p: float = 0.95
    temperature: float = 0.8
    repetition_penalty: float = 1.1
    last_n_tokens: int = 64
    seed: int = -1
    max_new_tokens: int = 256
    stop: List[str] = []
    stream: bool = False
    reset: bool = False
    batch_size: int = 8
    threads: int = -1
    context_length: int = -1
    gpu_layers: int = 0


class ModelConfig(BaseModel):
    name: str
    path: str
    type: str


def load_default_model_config() -> ModelConfig:
    return load_model(
        path=DEFAULT_MODEL_CONFIG_PATH,
        model=ModelConfig
    )


def load_default_generation_config() -> GenerationConfig():
    return load_model(
        path=DEFAULT_GENERATION_CONFIG_PATH,
        model=GenerationConfig
    )


class LLMParameters(BaseModel):
    prompt: str
    model_config: ModelConfig = load_default_model_config()
    generation_config: GenerationConfig = load_default_generation_config()


def call_safely(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        params = signature(func).parameters
        kwargs = {
            key: value
            for key, value in kwargs.items()
            if key in params
        }
        return func(*args, **kwargs)
    return wrapper