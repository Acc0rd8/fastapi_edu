from typing import Annotated
from fastapi import APIRouter, Path


router = APIRouter(
    prefix='/items',
    tags=['Item']
)


@router.get('/')
def list_items():
    return [
        'item1',
        'item2',
        'item3',
    ]


@router.get('/{item_id}')
def get_items(item_id: Annotated[int, Path(gt=0, lt=1_000_000)]):
    return {
        'item_id': item_id
    }
    
@router.get('/latest')
def get_latest_item():
    return {
        'item': {
            'id': 0,
            'name': 'latest'
        }
    }