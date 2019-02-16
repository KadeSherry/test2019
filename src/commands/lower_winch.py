#!/usr/bin/env python3
'''Snag some cargo.'''

from wpilib.command import Command

class LowerWinch(Command):
    '''Lift winch'''
    def __init__(self, robot):
        '''Save the robot object and pull in the intake subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.intake_winch)

    def initialize(self):
        """Called just before this Command runs the first time"""
        self.robot.intake.lower()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run."""
        self.robot.intake.lower()

    def isFinished(self):
        """Make this return true when this Command no longer needs to
        run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.intake_winch.stop()

    def interrupted(self):
        """Called when another command which requires one or more of
        the same subsystems is scheduled to run"""
        self.end()