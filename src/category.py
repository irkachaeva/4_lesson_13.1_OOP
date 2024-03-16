class Category:
    name: str #название
    description: str #описание
    products: list #товары

    count_of_category = 0
    count_uniq_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.count_of_category = 1

        Category.count_of_category += 1
        Category.count_uniq_category += len(self.products)




