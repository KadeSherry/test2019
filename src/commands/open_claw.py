#!/usr/bin/env python3
'''Open the claw.'''

from wpilib.command import Command

class OpenClaw(Command):
    '''Open the claw.'''

    def __init__(self, robot):
        """Save the robot object and pull in the claw subsystem."""
        super().__init__()

        self.robot = robot
        self.requires(self.robot.claw)

        

    def initialize(self):
        """Called just before this Command runs the first time"""
        print("open_claw:initialize()")

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        print("open_claw:execute()")
        self.robot.claw.open()

    def isFinished(self):
        """Make this return true when this Command no longer needs
        to run execute()"""
        print("open_claw:isFinished()")
        return True

    def end(self):
        """Called once after isFinished returns true"""
        print("Open claw ended.")
        print("open_claw:end()")

    def interrupted(self):
        """Called when another Command which requires one or more
        of the same subsystems is scheduled to run."""
        print("open_claw:interrupted()")
        self.end()
