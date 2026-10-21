from ..core import WatermarkBase, ExtractResult, DetectResult, EmbedResult, MarkType
import hmac
import hashlib
import numpy as np

class LSBHMACWatermark(WatermarkBase):
    def __init__(self, config: dict | None = None):
        super().__init__(name="fragile_lsb_hmac", config=config)
        self.block_size = self.config.get("block_size", 8)

    def embed(self, host_img, watermark_payload=None, key=None, **kwargs) -> EmbedResult:
        self._validate_image(host_img)
        if key is None:
            raise ValueError("缺少密钥")



    # def _block_auth(self, key: bytes, hash_bits: int) -> np.ndarray:


