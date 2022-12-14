""" Color module """

from logger import logger

class _Color:
    default = '0xFFFFFF'
    def __init__(self, value: tuple):
        self.rgb = value

    def hex_value(self) -> str:
        try:
            return f'{self.rgb[0]:02x}{self.rgb[1]:02x}{self.rgb[2]:02x}'
        except Exception as e:
            logger.info(f"can't convert to hex value getting error: {e}")
            return _Color.default

    @property
    def value(self):
        return self.rgb

class Colors:
    RED = _Color((255, 0, 0))
    GREEN = _Color((0, 255, 0))
    BLUE = _Color((0, 0, 255))

    WHITE = _Color((255, 255, 255))
    BLACK = _Color((0, 0, 0))
