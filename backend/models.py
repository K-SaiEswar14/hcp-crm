from sqlalchemy import Column, Integer, String, Text, Date, Time
from database import Base

class HCPInteraction(Base):
    __tablename__ = "hcp_interactions"
    id = Column(Integer, primary_key=True)
    hcp_name = Column(String(255))
    interaction_type = Column(String(100))
    interaction_date = Column(Date)
    interaction_time = Column(Time)
    attendees = Column(Text)
    topics_discussed = Column(Text)
    materials_shared = Column(Text)
    samples_distributed = Column(Text)
    sentiment = Column(String(20))
    outcomes = Column(Text)
    follow_up_actions = Column(Text)