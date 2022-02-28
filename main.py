# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
from dataclasses import replace


def greet (name, greeting_template = 'Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    return greeting


def force (mass, body = 'earth'):
    gravity = { 
        'sun' : 274,
        'jupiter' : 24.9,
        'neptune' : 11.2,
        'saturn' : 10.4,
        'earth' : 9.8,
        'uranus' : 8.9,
        'venus' : 8.9,
        'mars' : 3.7,
        'mercury' : 3.7,
        'moon' : 1.6,
        'pluto' : 0.6
    }
    force = float(mass) * gravity[body]
    return force

def pull (m1, m2, d):
    gravitational_constant = 6.674 * float(10**-11)
    pull = gravitational_constant * ((float(m1) * float(m2))/(float(d)**2))
    return pull

