from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from datetime import datetime
from app.database import Base

class AuditRecord(Base):
    """
    This class defines how an 'Audit' row looks in our database table.
    SQLAlchemy will use this to automatically create the table 'audits'.
    """
    __tablename__ = "audits"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    
    # Numerical scores
    seo_score = Column(Integer)
    content_score = Column(Integer)
    accessibility_score = Column(Integer)
    
    # The AI-generated advice
    ai_summary = Column(Text)
    
    # Storing the full detailed JSON so we don't lose any info
    detailed_data = Column(JSON)
    
    # When this audit was performed
    created_at = Column(DateTime, default=datetime.utcnow)
