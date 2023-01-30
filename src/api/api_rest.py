import logging

import uvicorn
from fastapi import FastAPI
from starlette_prometheus import metrics, PrometheusMiddleware

from src.api.entities.predict_model_request import PredictModelRequest
from src.api.music_prediction import predict_music

app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics)


class EndpointFilter(logging.Filter):
    # Uvicorn endpoint access log filter
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("GET /metrics") == -1


# Filter out /endpoint
logging.getLogger("uvicorn.access").addFilter(EndpointFilter())


@app.get("/")
async def read_main():
    return {"Server": "is working !"}


@app.post("/predict_music")
async def predict_genre_music(predict_request: PredictModelRequest):
    """
    :param predict_request:
    :return:
    """
    return predict_music(predict_request)


if __name__ == "__main__":
    # update uvicorn access logger format
    log_config = uvicorn.config.LOGGING_CONFIG
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=log_config)
