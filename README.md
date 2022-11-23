# BRAIN GAMES

### Hexlet tests and linter status:

[![Actions Status](https://github.com/Aston585/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Aston585/python-project-49/actions)
<a href="https://codeclimate.com/github/Aston585/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/54757df8be7df3307d01/maintainability" /></a>

## Brief description of the project

BRAIN GAMES is a set of five console games built using popular mobile brain training apps. Each game asks questions that need to be answered. After three correct answers, the game is considered to be completed. Incorrect results end the game and return it again.

### Parity check

A random number is shown. You must answer "yes" if the number is even, or "no" if it is odd.

### Calculator

A random math expression will be shown. You must calculate and write the answer.

### Greatest Common Divisor

Two random numbers will be shown. You must calculate and enter the cumulative divisor of these numbers.

### Arithmetic progression

A series of numbers is shown, forming an arithmetic progression. You need to define a number replaced by two dots.

### Is it a prime number?

The number will be shown. Answer "yes" if given number is prime. Otherwise answer "no".

#### Games demo:

|                                                              Parity check                                                              |                                                               Calculator                                                               |                                                        Greatest Common Divisor                                                         |
| :------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------: |
| <a href="https://asciinema.org/a/536369" target="_blank"><img src="https://asciinema.org/a/536369.svg" width="250" height="250" /></a> | <a href="https://asciinema.org/a/537758" target="_blank"><img src="https://asciinema.org/a/537758.svg" width="250" height="250" /></a> | <a href="https://asciinema.org/a/537772" target="_blank"><img src="https://asciinema.org/a/537772.svg" width="250" height="250" /></a> |

|                                                         Arithmetic progression                                                         |                                                         Is it a prime number?                                                          |
| :------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------: |
| <a href="https://asciinema.org/a/538621" target="_blank"><img src="https://asciinema.org/a/538621.svg" width="250" height="250" /></a> | <a href="https://asciinema.org/a/538041" target="_blank"><img src="https://asciinema.org/a/538041.svg" width="250" height="250" /></a> |

---

## Installation and launch

### Get and install the project:

```
$ git clone https://github.com/Aston585/python-project-49.git
$ cd ./python-project-49
$ make install
```

### Install and launch games:

```
$ make build
$ make package-install
$ name-of-the-game
```

### Run game without installation:

```
$ make name-of-the-game
```

### Name of the game:

"Parity check" - brain-even  
"Calculator" - brain-calc  
"Greatest Common Divisor" - brain-gcd  
"Arithmetic progression" - brain-progression  
"Is it a prime number" - brain-prime
