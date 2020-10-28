[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3513684&assignment_repo_type=AssignmentRepo)
# Exercise 5.3 Cube

Create a `Cube` class that represents a cube (i.e., a standard hexahedron). Create a `def __init__(self, edge_length)` constructor for the class, that takes the length of the cube's edge as its parameter.

Make a `def volume()` method for the cube, which calculates and returns the cube's volume. The volume of the cube is calculated with the formula `edge_length * edge_length * edge_length`. Moreover, make a `def __str__()` method for the cube, which returns a string representation of it. The string representation should take the form "`The length of the edge is l and the volume v`", where `l` is the length and `v` the volume - both the length and volume must be represented as integers.

Examples are provided underneath

```python
o_shea_jackson = Cube(4)
print(o_shea_jackson.volume())
print(o_shea_jackson)

print()

salt = Cube(2)
print(salt.volume())
print(salt)
```

```plaintext
64
The length of the edge is 4 and the volume 64

8
The length of the edge is 2 and the volume 8
```
