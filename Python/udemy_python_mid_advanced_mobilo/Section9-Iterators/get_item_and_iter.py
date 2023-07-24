class Combinations:
    def __init__(self, products, promotions, customers) -> None:
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.max_items_no = len(products) * len(promotions) * len(customers)

    def __getitem__(self, item):
        if item > self.max_items_no:
            raise StopIteration
        promo_customers_prod = len(self.promotions) * len(self.customers)
        pos_products = item // promo_customers_prod
        item = item % promo_customers_prod

        pos_promotions = item // len(self.customers)
        item = item % len(self.customers)
        pos_customers = item
        
        return "{}, {}, {}".format(self.products[pos_products], self.promotions[pos_promotions], self.customers[pos_customers])
    
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]
 
combinations = Combinations(products, promotions, customers)

# for i in range(1, len(products) * len(promotions) * len(customers)):
#     print(combinations[i])

combinations_iter = iter(combinations)

# first = next(combinations_iter)
# print("First: {}".format(first))

# while True:
#     try:
#         print(next(combinations_iter))
#     except StopIteration:
#         break

for c in combinations_iter:
    print(c)