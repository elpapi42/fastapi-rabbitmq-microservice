import asyncio
import logging
from typing import Optional

from fastapi import FastAPI
from aio_pika import Message

from source import rabbit


logger = logging.getLogger('uvicorn')

app = FastAPI()

@app.on_event("startup")
async def startup():
    await rabbit.install(app)

    asyncio.create_task(rabbit.consume(app))
    logger.info('Listening on queue default')

@app.get('/')
def read_root():
    return {'hello': 'world'}
