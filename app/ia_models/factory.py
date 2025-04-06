from typing import Dict, Type
from .base import AIModel
from .gemini import GeminiModel


class AIModelFactory:
    """Factory class for creating AI model instances."""

    _models: Dict[str, Type[AIModel]] = {
        'gemini': GeminiModel,
    }

    @classmethod
    def create_model(cls, model_type: str, **kwargs) -> AIModel:
        model_class = cls._models.get(model_type.lower())

        if not model_class:
            raise ValueError(f"Unsupported model type: {model_type}")

        return model_class(**kwargs) 