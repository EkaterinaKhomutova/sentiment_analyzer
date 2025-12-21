from typing import List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from analyzer import SentimentAnalyzer
from storage import AnalysisStorage

app = FastAPI(
    title="Sentiment Analyzer API",
    version="2.0.0",
)

analyzer = SentimentAnalyzer()
storage = AnalysisStorage()


class TextRequest(BaseModel):
    texts: List[str]


class AnalysisResponse(BaseModel):
    analysis_id: str
    results: List[Dict[str, float | str]]
    statistics: Dict[str, int]


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_sentiment(request: TextRequest) -> AnalysisResponse:
    results = analyzer.analyze(request.texts)
    stats = analyzer.statistics(results)
    analysis_id = storage.save(request.texts, results)

    return AnalysisResponse(
        analysis_id=analysis_id,
        results=results,
        statistics=stats,
    )


@app.get("/analyses")
def list_analyses() -> List[Dict]:
    return storage.list_all()


@app.get("/analyses/{analysis_id}")
def get_analysis(analysis_id: str) -> Dict:
    analysis = storage.get(analysis_id)
    if analysis is None:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return analysis
