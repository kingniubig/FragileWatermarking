from dataclasses import dataclass
from enum import Enum
import numpy as np

class MarkType(str, Enum):
    GRAYSCALE = "grayscale"
    BITSTREAM = "bitstream"

@dataclass
class EmbedResult:
    marked_img: np.ndarray
    embed_meta: dict

@dataclass
class DetectResult:
    is_tampered: bool
    tampered_mask: np.ndarray | None = None
    heatmap: np.ndarray | None = None
    similarity_score: float | None = None

@dataclass
class ExtractResult:
    mark_type: MarkType
    extracted_mark: np.ndarray | None = None
    mark_shape: tuple | None = None

    is_success: bool = True
    message: str = ""

    reference_mark: np.ndarray | None = None
    similarity: float | None = None             #灰度水印相似程度
    ber: float | None = None                    #误码率，密钥水印

    raw_bits: np.ndarray | None = None
    valid_mask: np.ndarray | None = None
    embed_meta: dict | None = None

    @property
    def bit_accuracy(self) -> float | None:
        return None if self.ber is None else 1.0 - self.ber

    @property
    def extracted_bits(self) -> np.ndarray | None:
        if self.extracted_mark is None:
            return None
        if self.mark_type is MarkType.BITSTREAM:
            return self.extracted_mark.ravel()
        return (self.extracted_mark > 127).astype(np.uint8).ravel()
