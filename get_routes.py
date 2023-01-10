from fastapi import APIRouter
from enum import Enum
from typing import Optional



get_router=APIRouter(
    prefix='/item',
    tags=['item']
)

class FoodEnum(str, Enum):
    fruits:"fruits"
    vegetables:"vegetables"
    dairy:"dairy"


@get_router.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if food_name==FoodEnum.vegetables:
        return {"food_name": food_name,"message":"You are helthy"}

    if food_name.value=="friuts":
        return {
            "food_name": food_name,
            "message":"You are astill helthy, But like sweet things",
            }
    return {"food_name":food_name,"message":"I like Chocolate Milk"}



fake_item_db = [{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"},]

@get_router.get("/items")
async def list_items(skip:int =0,limit:int=10):
    return fake_item_db[skip:skip+limit]

@get_router.get("/items/{item_id}")
async def get_item(item_id:str,q:str | None = None,short: bool=True):
    item={"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"Updated"})

    return item
