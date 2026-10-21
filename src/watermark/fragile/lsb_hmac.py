from hmac import digest
from pickletools import uint8

from ..core import WatermarkBase, ExtractResult, DetectResult, EmbedResult, MarkType
import hmac
import hashlib
import numpy as np

class LSBHMACWatermark(WatermarkBase):
    def __init__(self, config: dict | None = None):
        super().__init__(name="fragile_lsb_hmac", config=config)
        self.block_size = self.config.get("block_size", 8)
        if not isinstance(self.block_size, int) or self.block_size <= 0:
            raise ValueError("")

    def embed(self, host_img, watermark_payload=None, key=None, **kwargs) -> EmbedResult:
        self._validate_image(host_img)
        if key is None:
            raise ValueError("缺少密钥")

        work = host_img.copy()
        h, w = work.shape[:2]
        bs = self.block_size

        for by in range(0, h, bs):
            for bx in range(0, w, bs):
                block = work[by:by+bs, bx:bx+bs]
                digest_ = hmac.new(key, block.tobytes(), hashlib.sha256).digest()
                mask = np.frombuffer(digest_, dtype=np.uint8)




    # def _block_auth(self, key: bytes, hash_bits: int) -> np.ndarray:


