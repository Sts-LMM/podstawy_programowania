class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.items:
            self.items[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}
            print(f"Item {item_name} added to inventory.")
        else:
            print("Item with this ID already exists.")

    def update_item(self, item_id, **kwargs):
        if item_id in self.items:
            for key, value in kwargs.items():
                if key in self.items[item_id]:
                    self.items[item_id][key] = value
            print(f"Item {self.items[item_id]['item_name']} updated.")
        else:
            print("Item with this ID does not exist.")

    def check_item_details(self, item_id):
        if item_id in self.items:
            print("Item Details:")
            for key, value in self.items[item_id].items():
                print(f"{key}: {value}")
        else:
            print("Item with this ID does not exist.")

inventory = Inventory()

inventory.add_item("001", "Laptop", 10, 1200)
inventory.add_item("002", "Printer", 5, 300)
inventory.add_item("003", "Mouse", 20, 20)

inventory.update_item("002", stock_count=8, price=350)

inventory.check_item_details("002")
