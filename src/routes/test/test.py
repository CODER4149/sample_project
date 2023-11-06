from fastapi import APIRouter, HTTPException


from loguru import logger

router = APIRouter()


@router.get("/tunnel/inwarding/get_box_data", tags=["inwarding"])
def get_box_data(
):
    try:

        return {"data": "success"}

    except HTTPException as e:
        logger.debug(f'{e}')
        raise e
    except Exception as e:
        logger.debug(f'{e}')
        raise HTTPException(status_code=500, detail=f'{e}')
