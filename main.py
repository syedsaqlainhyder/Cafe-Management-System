import streamlit as st


cols = st.columns([1,1])
with cols[0]:
    st.image("WhatsApp Image 2025-03-04 at 3.01.34 PM.jpeg")

menu = {
    "Coffee": 3.0,
    "Tea": 2.5,
    "Sandwich": 5.0,
    "Croissant": 4.0,
    "Smoothie": 3.5
}


inventory = {
    "Coffee": 50,
    "Tea": 50,
    "Sandwich": 30,
    "Croissant": 30,
    "Smoothie": 40
}
img = [
    "WhatsApp Image 2025-03-05 at 3.32.55 PM (4).jpeg",
   
]

def calculate_total(order_items):
    total = sum([menu[item] * quantity for item, quantity in order_items.items()])
    return total


def update_inventory(order_items):
    for item, quantity in order_items.items():
        inventory[item] -= quantity


st.title("Cafe Management System")

index = 0
st.header("Menu")
for item, price in menu.items():
    cols = st.columns([1,6])
    with cols[0]:
        st.image(img[index])
        st.write(f"{item}: ${price:.2f}")
    index = index +1

st.header("Place Your Order")
order_items = {}
for item in menu:
    quantity = st.number_input(f"How many {item}s would you like?", min_value=0, max_value=10, step=1)
    if quantity > 0:
        order_items[item] = quantity


if order_items:
    total = calculate_total(order_items)
    st.subheader(f"Total: ${total:.2f}")

    if st.button("Place Order"):

        update_inventory(order_items)
        st.success("Order placed successfully!")
        st.write("Updated Inventory:")
        for item, stock in inventory.items():
            st.write(f"{item}: {stock} items left")
else:
    st.warning("Please add items to your order.")


st.header("Inventory Management")
st.write("Admin Section to manage inventory.")
if st.button("Restock Inventory"):

    for item in inventory:
        inventory[item] = 50
    st.success("Inventory has been restocked to default levels.")
    st.write("Updated Inventory:")
    for item, stock in inventory.items():
        st.write(f"{item}: {stock} items left")
