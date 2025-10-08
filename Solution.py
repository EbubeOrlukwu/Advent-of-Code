def count_xmas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    count = 0
    
    # All 8 directions
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
                # Check if word fits in this direction
                if (0 <= r + 3*dr < rows and 
                    0 <= c + 3*dc < cols):
                    # Build the word
                    word = (grid[r][c] + 
                           grid[r+dr][c+dc] + 
                           grid[r+2*dr][c+2*dc] + 
                           grid[r+3*dr][c+3*dc])
                    if word == target:
                        count += 1
    return count

def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f]
    
    result = count_xmas_occurrences(grid)
    print(f"Answer: {result}")
    return result

if __name__ == "__main__":
    main()