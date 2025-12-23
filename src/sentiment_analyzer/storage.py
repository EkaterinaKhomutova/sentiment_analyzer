from typing import Dict, List
from uuid import uuid4
from datetime import datetime


class AnalysisStorage:
    """
    In-memory storage for analysis history.
    """

    def __init__(self) -> None:
        self._storage: Dict[str, Dict] = {}

    def save(self, texts: List[str], results: List[Dict]) -> str:
        analysis_id = str(uuid4())
        self._storage[analysis_id] = {
            "id": analysis_id,
            "timestamp": datetime.utcnow().isoformat(),
            "texts": texts,
            "results": results,
        }
        return analysis_id

    def get(self, analysis_id: str) -> Dict | None:
        return self._storage.get(analysis_id)

    def list_all(self) -> List[Dict]:
        return list(self._storage.values())
