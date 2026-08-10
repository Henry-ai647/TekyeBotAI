const API_URL = "http://localhost:8000";


async function loadOrders() {

    try {

        const response = await fetch(
            `${API_URL}/orders`
        );

        const data = await response.json();

        displayOrders(data);

    } catch (error) {

        console.log(
            "Backend is not running yet."
        );

    }
}


function displayOrders(orders) {

    const ordersList =
        document.getElementById("ordersList");

    if (orders.length === 0) {

        ordersList.innerHTML =
            "<p>No orders yet.</p>";

        return;
    }


    ordersList.innerHTML = "";


    orders.forEach(order => {

        const orderElement =
            document.createElement("div");

        orderElement.className = "order";

        orderElement.innerHTML = `
            <strong>
                Order #${order.id}
            </strong>

            <p>
                Customer: ${order.customer}
            </p>

            <p>
                ${order.quantity} × ${order.meal}
            </p>

            <p>
                Status: ${order.status}
            </p>
        `;

        ordersList.appendChild(
            orderElement
        );

    });

}


loadOrders();
