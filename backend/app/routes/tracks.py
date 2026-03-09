from fastapi import APIRouter

router = APIRouter()

@router.get('/tracks')
def health():
    return {'tracks': 'music woohoo'}