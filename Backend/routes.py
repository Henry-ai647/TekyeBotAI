from fastapi import APIRouter

router = APIRouter()

@router.get("/restaurants")
def get_restaurants():
    return {
        "message": "Restaurant list will appear here."
    }
