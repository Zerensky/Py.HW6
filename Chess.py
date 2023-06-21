from random import shuffle

SIZE = 8


def check_position(queens_positions: list) -> bool:
    for queen_index in range(len(queens_positions)):
        for another_queen_index in range(queen_index + 1, len(queens_positions)):
            is_horizontal = queens_positions[queen_index][0] == queens_positions[another_queen_index][0]
            is_vertical = queens_positions[queen_index][1] == queens_positions[another_queen_index][1]
            is_diagonal_up = queens_positions[queen_index][0] - queens_positions[another_queen_index][0] == \
                             queens_positions[queen_index][1] - queens_positions[another_queen_index][1]
            is_diagonal_down = queens_positions[another_queen_index][0] - queens_positions[queen_index][0] == \
                               queens_positions[queen_index][1] - queens_positions[another_queen_index][1]
            if is_diagonal_up or is_diagonal_down or is_horizontal or is_vertical:
                return False
    return True


def generate_solution(board_size: int) -> list:
    is_generated = False
    columns = [i for i in range(1, board_size + 1)]
    while not is_generated:
        rows = [i for i in range(1, board_size + 1)]
        shuffle(rows)
        if check_position([x for x in zip(columns, rows)]):
            is_generated = True
    return [x for x in zip(columns, rows)]


def generate_n_different_solution(board_size: int, num_solution: int, tries_until_stop=100) -> list:
    tried = 0
    solutions = []
    while len(solutions) < num_solution and tried < tries_until_stop:
        position = generate_solution(board_size)
        tried += 1
        if not (position in solutions):
            tried = 0
            solutions.append(position)
    if len(solutions) < num_solution:
        print(f"Managed to find only {len(solutions)} under the specified amount of retries")
    return solutions


if __name__ == "__main__":
    solution = [(1, 5), (2, 1), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]
    not_solution = [(1, 5), (2, 1), (3, 8), (4, 7), (5, 3), (6, 6), (7, 2), (8, 4)]
    print(generate_n_different_solution(SIZE, 4))