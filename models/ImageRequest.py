from pydantic import BaseModel

class ImageRequest(BaseModel):
  name: str
  b64: str
