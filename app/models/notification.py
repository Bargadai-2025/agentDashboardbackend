from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.models.pyobjectid import PyObjectId

class NotificationModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    agentId: PyObjectId
    agentName: str
    customerId: Optional[PyObjectId] = None
    customerName: Optional[str] = None
    type: str # 'arrival', 'cash_collected', 'deviation'
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    read: bool = False

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
