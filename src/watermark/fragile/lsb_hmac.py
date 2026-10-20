from ..core import WatermarkBase, ExtractResult, DetectResult, EmbedResult, MarkType
import hmac
import hashlib
import numpy as np

class LSBHMACWatermark(WatermarkBase):
    def __init__(self, config: dict | None = None):
        super().__init__(name="fragile_lsb_hmac", config=config)

    def embed(self, host_img, watermark_payload=None, key=None, **kwargs) -> EmbedResult:
        pass
