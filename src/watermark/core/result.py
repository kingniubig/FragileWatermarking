from dataclasses import dataclass
import numpy as np

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
    extracted_mark: np.ndarray |