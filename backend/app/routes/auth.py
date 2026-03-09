from fastapi import APIRouter

router = APIRouter()

@router.get('/auth')
def health():
    return {'auth': 'super secret password'}