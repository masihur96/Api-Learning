from fastapi import APIRouter

auth_router=APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.get('/',description="This is our Base Route.")
async def base_get_route():
    return {"Message":"Hello Auth"}

@auth_router.post('/')
async def post():
    return {"Message":"Hello Auth Post Route"}

@auth_router.put('/')
async def put():
    return {"Message":"Hello Auth Put Route"}