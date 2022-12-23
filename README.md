# 🎄 Advent of Code 2022 🎄

![AoC2022 logo](https://raw.githubusercontent.com/orfeasa/advent-of-code-2022/master/header.png)

## Summary

[Advent of Code](http://adventofcode.com/) is an annual Advent calendar of programming puzzles.
This year I am doing it in Python.

## Running the code

To run the code of a specific day from the root directory run the following, replacing `xx` with the day number, `01` - `25`. Make sure you use Python 3.10+.

```sh
python3 day_xx/main.py
```

You may want to replace `python3` with `python3.10` if the command above doesn't work.

To run the code of all days run the script:

```sh
./run_all.sh
```

Make sure you have given permission to execute (`chmod +x run_all.sh`).

## Overview

| Day | Name                                                            | Stars |
| --- | --------------------------------------------------------------- | ----- |
| 01  | [Calorie Counting](https://adventofcode.com/2022/day/1)         | ⭐⭐  |
| 02  | [Rock Paper Scissors](https://adventofcode.com/2022/day/2)      | ⭐⭐  |
| 03  | [Rucksack Reorganization](https://adventofcode.com/2022/day/3)  | ⭐⭐  |
| 04  | [Camp Cleanup](https://adventofcode.com/2022/day4)              | ⭐⭐  |
| 05  | [Supply Stacks](https://adventofcode.com/2022/day5)             | ⭐⭐  |
| 06  | [Tuning Trouble](https://adventofcode.com/2022/day6)            | ⭐⭐  |
| 07  | [No Space Left On Device](https://adventofcode.com/2022/day7)   | ⭐⭐  |
| 08  | [Treetop Tree House](https://adventofcode.com/2022/day8)        | ⭐⭐  |
| 09  | [Rope Bridge](https://adventofcode.com/2022/day9)               | ⭐⭐  |
| 10  | [Cathode-Ray Tube](https://adventofcode.com/2022/day10)         | ⭐⭐  |
| 11  | [Monkey in the Middle](https://adventofcode.com/2022/day11)     | ⭐⭐  |
| 12  | [Hill Climbing Algorithm](https://adventofcode.com/2022/day12)  | ⭐⭐  |
| 13  | [Distress Signal](https://adventofcode.com/2022/day13)          | ⭐⭐  |
| 14  | [Regolith Reservoir](https://adventofcode.com/2022/day14)       | ⭐⭐  |
| 15  | [Beacon Exclusion Zone](https://adventofcode.com/2022/day15)    |       |
| 16  | [Proboscidea Volcanium](https://adventofcode.com/2022/day16)    |       |
| 17  | [Pyroclastic Flow](https://adventofcode.com/2022/day17)         |       |
| 18  | [Boiling Boulders](https://adventofcode.com/2022/day18)         |       |
| 19  | [Not Enough Minerals](https://adventofcode.com/2022/day19)      |       |
| 20  | [Grove Positioning System](https://adventofcode.com/2022/day20) | ⭐⭐  |
| 21  | [Monkey Math](https://adventofcode.com/2022/day21)              | ⭐⭐  |
| 22  | [Monkey Map](https://adventofcode.com/2022/day22)               | ⭐    |
| 23  | [Unstable Diffusion](https://adventofcode.com/2022/day22)       | ⭐    |
| 24  |                                                                 |       |
| 25  |                                                                 |       |

## New Day

To generate the directory for the current day, save your browser cookie in a file called `cookie.txt` at the root level and run the new day script:

```sh
./new_day.sh
```

### How to get your cookie

A session cookie is a small piece of data used to authenticate yourself to the
Advent of Code web servers. It is not human-readable and might look something
like this `53616c7465645f5fbd2d445187c5dc5463efb7020021c273c3d604b5946f9e87e2dc30b649f9b2235e8cd57632e415cb`.

To learn more about authentication cookies check [this Wikipedia article](https://en.wikipedia.org/wiki/HTTP_cookie)

To get your cookie, go to the [Advent of Code site](https://adventofcode.com/), and while logged in.

- For Firefox: right and select "Inspect Element" and in the "Storage" tab select "Cookies" → "https://adventofcode.com"
- For Chrome: right and select "Inspect" and in the "Application" tab select "Cookies" → "https://adventofcode.com"

Then find the row with "session" as name, copy the value and paste it in your newly created `cookie.txt` file

## Linting

```sh
black . && isort . && pylint ** && flake8 --max-line-length=100
```
