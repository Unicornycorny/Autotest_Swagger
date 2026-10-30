from data.order_factory import make_order_data

first_order = make_order_data()
second_order = make_order_data()

print("First:", first_order)
print("Second:", second_order)

assert first_order is not second_order