const dishesList = document.getElementById("dishes-list");

console.log("1. Список:", dishesList);

fetch("http://127.0.0.1:8000/api/dishes")
    .then(response => {
        console.log("2. HTTP-статус:", response.status);
        return response.json();
    })
    .then(dishes => {
        console.log("3. Данные от API:", dishes);

        dishes.forEach(dish => {
            const item = document.createElement("li");
            item.textContent = `${dish.name} — ${dish.price} ₽`;
            dishesList.appendChild(item);
        });

        console.log("4. Карточки добавлены");
    })
    .catch(error => {
        console.error("Ошибка:", error);
    });