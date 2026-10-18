from abc import ABC, abstractmethod
from .result import


class WatermarkBase(ABC):
    def __init__(self, config: dict):
        self.config = config

@abstractmethod
def embed(self, host_img, watermark_payload) ->