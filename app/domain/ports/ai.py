from abc import ABC, abstractmethod


class AIIntegrationPort(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> dict:
        pass
