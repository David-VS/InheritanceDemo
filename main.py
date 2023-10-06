import drink as d
import food as f
import circle as c
import swimmingPool as sp

coffee = d.Drink("coffee", 1.5)
irish_coffee = d.AlcoholicDrink("Irish Coffee", 6, 10)
snickers = f.Food("snickers", 2, 500)

print(coffee)
print(irish_coffee)
print(snickers)

circle1 = c.Circle(5)

print(circle1.circumference())
print(circle1.area())

radius_pool = int(input("Radius of your pool?"))
width_path = int(input("How wide is your path?"))
price_path = int(input("What type of surface for the path? Price for a m²"))
price_fence = int(input("What type of fence? price for a m"))

new_pool = sp.SwimmingPool(radius_pool, width_path, price_path, price_fence)
print("costs for the path:€", new_pool.costs_path())
print("costs for the fence:€", new_pool.costs_fence())
print("total costs:€", new_pool.costs_total())
