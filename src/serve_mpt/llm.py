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

import functools

from ctransformers.llm import LLM
from ctransformers import AutoModelForCausalLM

from serve_mpt.utils import (
    LLMParameters,
    call_safely
)


@functools.cache
def load_model(path: str, type: str, **kwargs) -> LLM:
    return AutoModelForCausalLM.from_pretrained(
        path,
        model_type=type
    )


def generate(params: LLMParameters) -> str:
    model_kwargs = params.model_config.dict()
    model = load_model(**model_kwargs)
    generation_kwargs = params.generation_config.dict()
    return call_safely(model)(params.prompt, **generation_kwargs)