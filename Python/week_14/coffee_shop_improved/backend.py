class CoffeeShopError(Exception):
    """Base class for CoffeeShop-related errors."""


class CapacityError(CoffeeShopError):
    """Raised when adding a customer would exceed max capacity."""


class CustomerNameError(CoffeeShopError):
    """Raised when a customer name is invalid."""


class CustomerIndexError(CoffeeShopError):
    """Raised when an index is invalid/out of range."""


class CoffeeShop:
    def __init__(self, max_capacity=10):
        self.customers = []
        self.max_capacity = int(max_capacity)

        if self.max_capacity <= 0:
            raise ValueError("max_capacity must be a positive integer")

    def get_num_customers(self):
        return len(self.customers)

    def add_customer(self, name):
        if name is None:
            raise CustomerNameError("Customer name cannot be None")

        name = str(name).strip()
        if name == "":
            raise CustomerNameError("Customer name cannot be empty")

        if len(self.customers) >= self.max_capacity:
            raise CapacityError(f"Coffee shop is full (max {self.max_capacity} customers).")

        self.customers.append(name)

    def get_customer_at(self, index):
        if not isinstance(index, int):
            raise CustomerIndexError("Customer index must be an integer")

        if index < 0 or index >= len(self.customers):
            raise CustomerIndexError(f"Customer index {index} is out of range")

        return self.customers[index]

    def remove_customer_at(self, index):
        if not isinstance(index, int):
            raise CustomerIndexError("Customer index must be an integer")

        if index < 0 or index >= len(self.customers):
            raise CustomerIndexError(f"Customer index {index} is out of range")

        del self.customers[index]