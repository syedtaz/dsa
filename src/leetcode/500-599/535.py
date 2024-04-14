from base64 import b64encode, b64decode

class Codec:
    def encode(self, longUrl: str) -> str:
        result = longUrl.encode("utf-8")
        return b64encode(result).decode("utf-8")

    def decode(self, shortUrl: str) -> str:
        result = b64decode(shortUrl)
        return result.decode("utf-8")