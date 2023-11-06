# from src.db.alchemy import SessionLocal, engine
# from pydantic import BaseModel
#
#
# class Message(BaseModel):
#     status_code: int
#     detail: str
#
#
# def get_db():
#     '''
#     does
#     :return:
#     '''
#     try:
#         db = SessionLocal()
#         # logging.info("get_db")
#         try:
#             # logging.debug("yeilding db")
#             yield db
#         finally:
#             # logging.debug("closing db")
#             db.close()
#     except Exception as e:
#         print(e)
#
#
# def get_raw_db():
#     '''
#     does
#     :return:
#     '''
#     try:
#         db = engine.raw_connection()
#
#         # logging.info("get_db")
#         try:
#             # logging.debug("yeilding db")
#             yield db
#         finally:
#             # logging.debug("closing db")
#             db.close()
#     except Exception as e:
#         print(e)