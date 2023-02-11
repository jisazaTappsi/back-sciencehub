from typing import Dict
from fastapi import APIRouter

from . import views
from .models import *

router = APIRouter()

router.get(f'/', summary='hello.', tags=['hello'],
           response_model=Dict, name='hello', )(views.hello)
