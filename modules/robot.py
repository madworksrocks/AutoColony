import sys, importlib, os
path_insert = sys.path.insert
import_module = importlib.import_module

class Main:

    def __init__(self, main):
        self.main = main

    def load_script(self, save_file, scriptfname):
        self.save_file = save_file
        self.scriptfname = scriptfname
        path_insert(0, self.save_file)

        self.script = import_module(scriptfname)

        self.robots = self.main.data["robots"]

        self.robots.init(self.robots)

    def step(self):
        instructions = self.script.step()
        result = self.process_instructions(instructions)
        self.script.result(result)

    def process_instructions(self, instructions):
        result = []
        for inst, robot in zip(instructions, self.robots):
            result = inst[0](robot, *inst[1:])
        return result

robot_commands = {}
def robot_command(func):
    global robot_commands
    robot_commands[func.__name__] = func

    return func

@robot_command
def forward(robot):
    return True

@robot_command
def turn_left(robot):
    return True

@robot_command
def turn_right(robot):
    return True
