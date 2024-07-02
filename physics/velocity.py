import os
import sys
from maths.trigonometry.defines import TWO_PI
from maths.trigonometry.circle import revolutions_to_radians, radians_to_revolutions

sys.path.extend([os.getcwd()])

def linear_velocity(time):
    def fn(distance):
        return distance / time
    return fn

def angular_velocity(time):
    def fn(radians):
        return radians / time
    return fn

def linear_velocity_from_angular_velocity(radius):
    def fn(angular_velocity):
        return radius * angular_velocity
    return fn

# Returns a value in radians.
def angular_velocity_from_linear_velocity(radius):
    def fn(linear_velocity):
        return linear_velocity / radius
    return fn

def angular_velocity_from_revolutions_per_second(revolutions):
    return revolutions_to_radians(revolutions)

# Returns angular velocity in radians per second.
def angular_velocity_from_revolutions_per_minute(revolutions):
    return revolutions_to_radians(revolutions) / 60

# Returns angular velocity in radians per second.
def angular_velocity_from_revolutions_per_hour(revolutions):
    return revolutions_to_radians(revolutions) / (60 * 60)

# Parameter should be expressed in radians per second.
def revolutions_per_second(angular_velocity):
    return radians_to_revolutions(angular_velocity)

# Parameter should be expressed in radians per second.
def revolutions_per_minute(angular_velocity):
    return radians_to_revolutions(angular_velocity) * 60

# Parameter should be expressed in radians per second.
def revolutions_per_hour(angular_velocity):
    return radians_to_revolutions(angular_velocity) * 60 * 60

# Parameter should be expressed in radians per second.
def revolutions_per_millisecond(angular_velocity):
    return radians_to_revolutions(angular_velocity) / 1000
