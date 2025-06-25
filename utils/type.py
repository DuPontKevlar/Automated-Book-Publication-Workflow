from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Chapter:
    id: str
    title: str
    original_content: str
    spun_content: str = ""
    reviewed_content: str = ""
    final_content: str = ""
    human_feedback: list = field(default_factory=list)
    version: int = 1
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
