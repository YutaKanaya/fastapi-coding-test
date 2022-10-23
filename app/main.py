from fastapi import FastAPI, Depends
from routers import authentication, interview_sheet
from auth.oauth2 import oauth2_scheme

app = FastAPI()
app.include_router(authentication.router)
app.include_router(interview_sheet.router)

@app.get('/')
async def root(token: str = Depends(oauth2_scheme)):
    return {'message': 'Hello World'}