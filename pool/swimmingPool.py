from pool import circle as c


class SwimmingPool:
    def __init__(self, radius_pool, path_width, price_path, price_fence):
        self.inner_circle = c.Circle(radius_pool)
        self.outer_circle = c.Circle(radius_pool + path_width)
        self.price_path = price_path
        self.price_fence = price_fence

    def costs_path(self):
        area = self.outer_circle.area() - self.inner_circle.area()
        return area * self.price_path

    def costs_fence(self):
        return self.outer_circle.circumference() * self.price_fence

    def costs_total(self):
        return self.costs_path() + self.costs_fence()
