from queue import PriorityQueue

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan(state):
    distance = 0

    for i, value in enumerate(state):
        if value == 0:
            continue

        goal_index = goal.index(value)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_index, 3)

        distance += abs(x1 - x2) + abs(y1 - y2)
    
    return distance


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    x, y = divmod(zero, 3)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_zero = nx*3 + ny

            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def greedy_best_first(start):

    pq = PriorityQueue()
    pq.put((manhattan(start), start))

    visited = set()

    while not pq.empty():
        h, current = pq.get()

        if current in visited:
            continue

        visited.add(current)
        print(current)

        if current == goal:
            print("\nGoal Found!")
            return

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                pq.put((manhattan(neighbor), neighbor))


start = (
    1,2,3,
    4,0,6,
    7,5,8
)

greedy_best_first(start)