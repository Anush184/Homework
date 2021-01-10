class Country:
    def __init__(self, continent_name, country_name):
        self.continent_name = continent_name
        self.country_name = country_name

    def country_presentation(self):
        return f"""Continent: {self.continent_name}
Country: {self.country_name}"""


class Brand:
    def __init__(self, brand_name, start_date):
        self.brand_name = brand_name
        self.start_date = start_date

    def brand_presentation(self):
        return f"""Brand name: {self.brand_name}
Business start date: {self.start_date}"""


class Season:
    def __init__(self, season_name, temp):
        self.season_name = season_name
        self.average_temperature = temp

    def season_presentation(self):
        return f"""Season: {self.season_name}
Average temperature: {self.average_temperature}°C"""


class Product(Country, Brand, Season):
    def __init__(self, continent_name, country_name, brand_name, start_date,
                 season_name, temp, name, product_type, price,
                 quantity):
        Country.__init__(self, continent_name, country_name)
        Brand.__init__(self, brand_name, start_date)
        Season.__init__(self, season_name, temp)
        self.product_name = name
        self.product_type = product_type
        self.product_price = price
        self.product_quantity = quantity

    def get_product_name(self):
        return self.product_name

    def product_presentation(self):
        return f"""{self.product_name.upper()}
type: {self.product_type}
{self.country_presentation()}
{self.brand_presentation()}
{self.season_presentation()}
price: {self.product_price}$
quantity: {self.product_quantity}"""

    def discount_price(self, percent):
        return self.product_price - (self.product_price * percent) / 100

    def increase_quantity(self, count):
        return self.product_quantity + count


product1 = Product("USA", "California", "Skechers", "1992", "Summer", "25", "shoes", "baby", 65, 18)
print(product1.product_presentation())
product2 = Product("Europe", "Germany", "BMW", "1917", "Winter", "-15", "Car", "Sport", 35000, 8)
print(f"Discounted price of {product1.get_product_name()} is {product1.discount_price(15)}$")
print(f"Quantity of product {product1.get_product_name()} after adding is", product1.increase_quantity(10))
