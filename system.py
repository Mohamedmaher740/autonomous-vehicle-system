
import math


class Vehicle:
    def __init__(self, x=0, y=0, speed=0, direction=0):
        self.position = {'x': x, 'y': y}
        self.speed = speed
        self.direction = direction
        self.command_log = []

    def move(self, distance):
        
        # Method 1 >> canceled because bugs in the code
        """
        self.position['x'] += round((math.sin(self.direction))*distance , 2)
        self.position['y'] += round((math.cos(self.direction))*distance , 2)
        """

        # Method 2
        
        if self.direction == 0:
            self.position['y'] += distance
        elif self.direction == 180:
            self.position['y'] -= distance
        elif self.direction == 90:
            self.position['x'] += distance
        elif self.direction == 270:
            self.position['x'] -= distance
    

        self.command_log.append(f"Moved {distance} units")

    def change_speed(self, new_speed):
        self.speed = new_speed
        self.command_log.append(f"Speed Set to {self.speed}")

    def turn(self, new_direction):
        self.direction += new_direction
        self.command_log.append(f"Turned {new_direction} degrees")
        if self.direction > 360:
            self.direction -= 360

    def __str__(self):
        return f"Vehicle at ({self.position['x']}, {self.position['y']}), Speed: {self.speed}, Direction: {self.direction}"
    

class CommandHandler:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def execute_command(self, command):
        try:
            type = command['type']
            if type == 'move':
                self.vehicle.move(command['value'])
            elif type == 'speed':
                #check the value of speed
                if command['value'] > 0:
                    self.vehicle.change_speed(command['value'])
                else:
                    print(f"Error Processin Command {command}: Speed cannot be negative.")
            elif type == 'turn':
                self.vehicle.turn(command['value'])
            else:
                print(f"Error Processin Command {command}: Unknown Command Type: {command['type']}")
        except KeyError as e:
            print(f"Missing key: {e}")

    def process_commands(self, commands):
        for command in commands:
            self.execute_command(command)

        print(self.vehicle)
        print("History:", self.vehicle.command_log)


vehicle = Vehicle()
handler = CommandHandler(vehicle)

commands = [
    {'type': 'speed', 'value': 5},
    {'type': 'move', 'value': 100},
    {'type': 'turn', 'value': 90},
    {'type': 'move', 'value': 50},
    {'type': 'speed', 'value': -10},
    {'type': 'turn', 'value': 360},
    {'type': 'move', 'value': 50},
    {'type': 'fly', 'value': 10}
]

handler.process_commands(commands)


