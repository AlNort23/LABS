import math
from typing import List, Tuple


class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = 0.0
        self.y = 0.0

    def get_mass(self) -> float:
        return self.mass

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def __str__(self) -> str:
        return f"Sun({self.name}, radius={self.radius}, mass={self.mass}, temp={self.temp})"


class Planet:
    def __init__(self, name: str, radius: float, mass: float,
                 distance: float, x: float, y: float, color: str):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = x
        self.y = y
        self.color = color
        self.vel_x = 0.0
        self.vel_y = 0.0

    def get_mass(self) -> float:
        return self.mass

    def get_distance(self) -> float:
        return self.distance

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def get_x_vel(self) -> float:
        return self.vel_x

    def get_y_vel(self) -> float:
        return self.vel_y

    def set_x_vel(self, new_x_vel: float) -> None:
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float) -> None:
        self.vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float) -> None:
        self.x = new_x
        self.y = new_y
        self._update_distance()

    def _update_distance(self) -> None:
        self.distance = math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self) -> str:
        return f"Planet({self.name}, radius={self.radius}, mass={self.mass}, distance={self.distance}, color={self.color})"


class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets = []

    def add_planet(self, new_planet: Planet) -> None:
        self.planets.append(new_planet)

    def add_sun(self, the_sun: Sun) -> None:
        self.the_sun = the_sun

    def show_planets(self) -> List[dict]:
        return [
            {
                'name': planet.name,
                'position': (planet.get_x_pos(), planet.get_y_pos()),
                'velocity': (planet.get_x_vel(), planet.get_y_vel()),
                'distance': planet.get_distance(),
                'color': planet.color
            }
            for planet in self.planets
        ]

    def move_planets(self) -> None:
        G = 6.67430e-11
        for planet in self.planets:
            dx = self.the_sun.get_x_pos() - planet.get_x_pos()
            dy = self.the_sun.get_y_pos() - planet.get_y_pos()
            r = math.sqrt(dx ** 2 + dy ** 2)

            a_mag = G * self.the_sun.get_mass() / (r ** 2)

            ax = a_mag * dx / r
            ay = a_mag * dy / r

            planet.set_x_vel(planet.get_x_vel() + ax)
            planet.set_y_vel(planet.get_y_vel() + ay)
            planet.move_to(
                planet.get_x_pos() + planet.get_x_vel(),
                planet.get_y_pos() + planet.get_y_vel()
            )


class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods

    def run(self) -> None:
        for _ in range(self.num_periods):
            self.solar_system.move_planets()
            current_state = self.solar_system.show_planets()
            print(f"Current state: {current_state}")


if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 1, 25, 5.0, 200.0, "green")
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, .1, 62, 10.0, 125.0, "red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()