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


