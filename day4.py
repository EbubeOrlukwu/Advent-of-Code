def count_xmas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    length = len(target)
    count = 0
    
    # All 8 directions: (row_delta, col_delta)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if we can fit the word in this direction
                end_r = r + (length - 1) * dr
                end_c = c + (length - 1) * dc
                
                if 0 <= end_r < rows and 0 <= end_c < cols:
                    # Build the word in this direction
                    word = ""
                    for i in range(length):
                        nr = r + i * dr
                        nc = c + i * dc
                        word += grid[nr][nc]
                    
                    if word == target:
                        count += 1
    
    return count

def solve_puzzle():
    # Read input from Advent of Code
    print("Paste your word search grid (press Ctrl+D when done):")
    
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break
    
    if not lines:
        print("No input provided!")
        return
    
    result = count_xmas_occurrences(lines)
    print(f"XMAS appears {result} times")
    return result

if __name__ == "__main__":
    solve_puzzle()
