# 🎄 Advent of Code 2022 🎄
[![GitHub Super-Linter](https://github.com/orfeasa/advent-of-code-2022/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

![AoC2022 logo](https://raw.githubusercontent.com/orfeasa/advent-of-code-2022/master/header.png)
## Summary

[Advent of Code](http://adventofcode.com/) is an annual Advent calendar of programming puzzles.
This year I am doing it in Python.

## Running the code

To run the code of a specific day from the root directory run the following, replacing `xx` with the day number, `01` - `25`. Make sure you use Python 3.9+.

```sh
python3 day_xx/main.py
```

You may want to replace `python3` with `python3.X` if the command above doesn't work.

To run the code of all days run the script:

```sh
./run_all.sh
```

Make sure you have given permission to execute (`chmod +x run_all.sh`).

## Overview

| Day                                        | Name                    | Stars |
| ------------------------------------------ | ----------------------- | ----- |
| [01](https://adventofcode.com/2022/day/1)  | |     |
| [02](https://adventofcode.com/2022/day/2)  | |     |
| [03](https://adventofcode.com/2022/day/3)  | |     |
| [04](https://adventofcode.com/2022/day/4)  | |     |
| [05](https://adventofcode.com/2022/day/5)  | |     |
| [06](https://adventofcode.com/2022/day/6)  | |     |
| [07](https://adventofcode.com/2022/day/7)  | |     |
| [08](https://adventofcode.com/2022/day/8)  | |     |
| [09](https://adventofcode.com/2022/day/9)  | |     |
| [10](https://adventofcode.com/2022/day/10) | |     |
| [11](https://adventofcode.com/2022/day/11) | |     |
| [12](https://adventofcode.com/2022/day/12) | |     |
| [13](https://adventofcode.com/2022/day/13) | |     |
| [14](https://adventofcode.com/2022/day/14) | |     |
| [15](https://adventofcode.com/2022/day/15) | |     |
| [16](https://adventofcode.com/2022/day/16) | |     |
| [17](https://adventofcode.com/2022/day/17) | |     |
| [18](https://adventofcode.com/2022/day/18) | |     |
| [19](https://adventofcode.com/2022/day/19) | |     |
| [20](https://adventofcode.com/2022/day/20) | |     |
| [21](https://adventofcode.com/2022/day/21) | |     |
| [22](https://adventofcode.com/2022/day/22) | |     |
| [23](https://adventofcode.com/2022/day/23) | |     |
| [24](https://adventofcode.com/2022/day/24) | |     |
| [25](https://adventofcode.com/2022/day/25) | |     |

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

To get your cookie, go to the [Advent of Code website](https://adventofcode.com/), and while logged in.

- For Firefox: right and select "Inspect Element" and in the "Storage" tab select "Cookies" → "https://adventofcode.com"
- For Chrome: right and select "Inspect" and in the "Application" tab select "Cookies" → "https://adventofcode.com"

Then find the row with "session" as name, copy the value and paste it in your newly created `cookie.txt` file

## Linting

```sh
black . && isort . && flake8 --max-line-length=100
```
