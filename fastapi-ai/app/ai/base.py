from abc import ABC, abstractmethod

class AIPlatform(ABC):
    @abstractmethod
    def chat(self,prompt:str)->str:
        """sends a promt to the ai and return the response text."""
        pass