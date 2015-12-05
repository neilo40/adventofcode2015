from collections import deque


with open("inputs/day3.txt", 'r') as fh:
    directions = deque(fh.read())


class Santa(object): 
    def __init__(self):
        self.visited = {}
        self.x = 0
        self.y = 0

    def move(self, direction):
        if (self.x, self.y) in self.visited:
            self.visited[(self.x, self.y)] += 1
        else:
            self.visited[(self.x, self.y)] = 1

        if direction == "^":
            self.y += 1
        elif direction == ">":
            self.x += 1
        elif direction == "v":
            self.y -= 1
        elif direction == "<":
            self.x -= 1


if __name__ == "__main__":
    santa = Santa()
    robo_santa = Santa()
    while(directions):
        santa.move(directions.popleft())
        try:
            robo_santa.move(directions.popleft())
        except:
            pass  # last iter may only have one direction to pop
    visited = dict(santa.visited)
    visited.update(robo_santa.visited)
    print("Total houses delivered to: {}".format(len(visited)))
