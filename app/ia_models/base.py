from abc import ABC, abstractmethod

class AIModel(ABC):
    """Abstract base class for AI models."""
    
    @abstractmethod
    async def get_response(self, message: str) -> str:
        """Get a response from the AI model for the given message.

        Args:
            message: The input message to get a response for

        Returns:
            The model's response as a string
        """
        pass