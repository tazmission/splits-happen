#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bowling score."""


def roll_value(i):
    """Return value for single character."""
    if i == '-':
        return 0
    if i == 'X':
        return 10
    return int(i)


def bowling(scoreboard):
    """Calculate the score."""
    scoreboard = scoreboard.replace(' ', '')

    score = 0
    frame = 0
    roll = 0
    for i in range(len(scoreboard)):
        c = scoreboard[i]
        roll += 1
        if roll == 2:
            roll = 0
            frame += 1
        if c == "/":
            score += 10 - roll_value(scoreboard[i-1]) + \
                roll_value(scoreboard[i+1])
        elif c == "X":
            roll = 0
            frame += 1
            if scoreboard[i+2] != '/':
                score += 10 + roll_value(scoreboard[i+1]) + \
                    roll_value(scoreboard[i+2])
            else:
                score += 20
        else:
            score += roll_value(c)
        if frame == 10:
            break
    return score

def main():
    print(bowling("XXXXXXXXXXXX"))
    print(bowling("9-9-9-9-9-9-9-9-9-9-"))
    print(bowling("5/5/5/5/5/5/5/5/5/5/5"))
    print(bowling("X7/9-X-88/-6XXX81"))
    
main()
