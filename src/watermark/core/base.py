from abc import ABC, abstractmethod
from .result import EmbedResult, ExtractResult, DetectResult


class WatermarkBase(ABC):
    def __init__(self, name: str, config: dict | None = None):
        self.name = name
        self.config = config

@abstractmethod
def embed(self, host_img, watermark_payload) -> EmbedResult:
    pass

@abstractmethod
def extract(self, watermarked_img, embed_meta=None) -> ExtractResult:
    pass

@abstractmethod
def detect(self, suspect_img, reference=None, embed_meta=None) -> DetectResult:
    pass