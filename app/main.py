from fastapi import FastAPI, Response, status

from .routers.events import router as events_router
from .routers.content import router as content_router
from .routers.stats import router as stats_router
from .routers.users import router as users_router


app = FastAPI(
    title="High-Load Counter Service",
    version="0.0.1",
    description="""
**High-Load Counter Service** — универсальный микросервис для подсчета событий (просмотров, кликов, 
лайков, уникальных посещений и т. д.).

## Возможности
- Мгновенная запись \"горячих\" событий;
- Получение агрегированных данных по контенту;
- Данные действий пользователей (фильтрация, рекомендации);
- Общая статистика по контенту и действиям.
"""
)


app.include_router(events_router)
app.include_router(content_router)
app.include_router(users_router)
app.include_router(stats_router)
