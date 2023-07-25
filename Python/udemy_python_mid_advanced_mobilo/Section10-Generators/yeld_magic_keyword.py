import time

def combinations(products, promotions, customers):
    # current_product = 0
    # current_promotion = 0
    # current_customer = 0

    # for _ in range(0, len(products) * len(promotions) * len(customers)):
    #     if current_customer >= len(customers):
    #         current_customer = 0
    #         current_promotion += 1

    #     if current_promotion >= len(promotions):
    #         current_promotion = 0
    #         current_product += 1

    #     if current_product >= len(products):
    #         current_product = 0
        
    #     item_to_return = "{} - {} - {}".format(products[current_product], promotions[current_promotion], customers[current_customer])

    #     current_customer += 1
    #     yield item_to_return

    for prod in products:
        for promo in promotions:
            for cust in customers:
                yield "{} - {} - {}".format(prod, promo, cust)
    
 
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

for c in combinations(products, promotions, customers):
    # here an analysis will be done - currently, just nothing happens :)
    print(c)
print("Processing done.")