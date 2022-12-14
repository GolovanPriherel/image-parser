import logging
from typing import List

from fastapi import APIRouter

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.models.postgres.rule34_images_info import Rule34ImagesInfoSchema
from src.operators.postgres import (
    rule34_send_data,
    rule34_url_parser
)
from src.modules import px500_parser, deviantart_parser, rule34_parser, rule34_urls_parser

router = APIRouter(prefix="")


@router.get("/")
async def root():

    return 'Сервис для парсинга фотографий с сайтов для дальнейшего обучения модели для генерации фотографий' \
           'Версия 0.0.1'


@router.get("/start_parsing")
async def start_parsing():
    # px500_parser.start_parsing()
    # deviantart_parser.start_parsing()
    rule34_parser.start_parsing()

    return "Успешно спаршено <ссылка на страницу>"


@router.get("/parsing_urls")
async def send_data():
    rule34_urls_parser.start_parsing()
