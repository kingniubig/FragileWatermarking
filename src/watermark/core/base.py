from abc import ABC, abstractmethod
import numpy as np
from .result import EmbedResult, ExtractResult, DetectResult


class WatermarkBase(ABC):
    def __init__(self, name: str, config: dict | None = None):
        self.name = name
        self.config = config | {}

    @abstractmethod
    def embed(self, host_img: np.ndarray,
              watermark_payload: np.ndarray | None = None,
              key: bytes | None = None,
              **kwargs) -> EmbedResult:
        pass

    @abstractmethod
    def extract(self, watermarked_img: np.ndarray,
                embed_meta: dict | None =None,
                key: bytes | None = None) -> ExtractResult:
        pass

    @abstractmethod
    def detect(self, suspect_img: np.ndarray,
               reference: np.ndarray | None = None,
               embed_meta: dict | None = None) -> DetectResult:
        pass

    def _validate_image(self, img: np.ndarray, name: str = "image") -> None:
        if not isinstance(img, np.ndarray):
            raise TypeError(f"[{self.name}]{name}的类型必须是 np.ndarray")
        if img.dtype is not np.uint8:
            raise ValueError(f"[{self.name}]{name} dtype必须是 uint8，当前为{img.dtype}")
        if img.ndim not in (2, 3):
            raise ValueError(f"[{self.name}] {name} 维度必须为 2 或 3，当前为{img.ndim}")
        if img.ndim == 3 and img.shape[2] not in (1, 3):
            raise ValueError(f"[{self.name}] {name} 通道数必须为 1 或 3")