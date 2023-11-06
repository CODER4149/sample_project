from fastapi import APIRouter
# so_outward_api
from src.routes.test.test import router as test

router = APIRouter()

# db environment
router.include_router(test)
