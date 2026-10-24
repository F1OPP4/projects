from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/categories")
def get_categories():
    return [
        {"id": 1, "name": "Пицца"},
        {"id": 2, "name": "Супы"},
        {"id": 3, "name": "Горячие блюда"},
        {"id": 4, "name": "Салаты"},
    ]
@app.get("/api/dishes")
def get_dishes(category_id: int | None = None):
    dishes = [
        {
            "id": 1,
            "name": "Пепперони",
            "price": 650,
            "category_id": 1,
            "description": "Пицца с пепперони и сыром",
        },
        {
            "id": 2,
            "name": "Борщ",
            "price": 350,
            "category_id": 2,
            "description": "Борщ со сметаной",
        },
        {
            "id": 3,
            "name": "Цезарь",
            "price": 420,
            "category_id": 4,
            "description": "Салат с курицей и соусом",
        },
    ]

    if category_id is None:
        return dishes

    return [
        dish for dish in dishes
        if dish["category_id"] == category_id
    ]
