from fastapi import APIRouter

router = APIRouter()

@router.get('/albums')
def health():
    return {'albums': 'albums woohoo'}