# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template


def greet(name, template="Hello <name>!"):
    greeting = template.replace("<name>", name)
    return greeting


print(greet("Johan"))
print(greet("Monique", "What's up, <name>..."))


# Part 2: Force

bodies = {
    "sun": 274,
    "jupiter": 24.92,
    "neptune": 11.15,
    "saturn": 10.44,
    "earth": 9.798,
    "uranus": 8.87,
    "venus": 8.87,
    "mars": 3.71,
    "mercury": 3.7,
    "moon": 1.62,
    "pluto": 0.58
}

# Weight of items in kilograms (kg)
items = {
    "apple": 0.1,
    "tv": 25,
    "car": 750
}


def force(mass="apple", body="earth"):
    gravity = bodies[body]
    weight = items[mass]
    formula = weight * round(gravity, 1)
    return formula


print(force())
print(force("tv", "mars"))
print(force("car", "pluto"))


# Part 3: Pull

def pull(m1=0.1, m2=5.972e24, d=6.371e6):
    gravitational_constant = 6.674e-11
    gravitational_pull = gravitational_constant * (((m1 * m2) / d ** 2))
    return gravitational_pull


print(pull())
print(pull(800, 1500, 3))
