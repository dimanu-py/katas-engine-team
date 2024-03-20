# :robot: Simple Mars Rover Kata :robot:

## Resources

These instructions where extracted from Codurance Kata Catalogue. You can find the original instructions in the link below.

[![Web](https://img.shields.io/badge/Codurance-Website-14a1f0?style=for-the-badge&logo=web&logoColor=white&labelColor=101010)](https://www.codurance.com/katas/simple-mars-rover)

## Description

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their onboard cameras can get a complete view of the surrounding terrain to send back to Earth.

Your task is to develop an API that moves the rovers around on the plateau.

In this API, the plateau is represented as a 10x10 grid, and a rover has state consisting of two parts:

- The position on the grid (represented by an X,Y coordinate pair)
- The direction the compass is facing (represented by a letter, one of  'N', 'S', 'E', 'W')
- The starting position of the rover is '0:0:N'

### Input

The input to the program is a string of one-character move commands:

- 'L' and 'R' rotate the direction the rover is facing
- 'M' moves the rover one grid point forward in the direction it is currently facing

If a rover reaches the end of the plateau, it wraps around the end of the grid.

### Output

The program should output the final position of the rover after all the move commands have been executed.

The position is represented as a coordinate pair and a direction, joined by colons, with the direction letters in uppercase. For example:
a rover whose position is `2:3:W` is at square (2,3), facing west.

### Example

The input string `MMRMMLM` for the rover starting at `0:0:N` will output `2:3:N`.

Given an input `MMMMMMMMMM` for the rover starting at `0:0:N` will output `0:0:N` due to wrap-around.

## Objective

The objective of this kata is to practice the following TDD concepts:

- Baby steps
- Fake it ('til you make it)
- 3 Repetition rule (triangulation)
- Test parameterization