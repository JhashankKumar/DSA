# find the row with the maximum number of 1s in a binary matrix
def main():
    print("Enter the number of rows and columns in the binary matrix (space-separated):")
    rows, cols = map(int, input().split())
    
    print(f"Enter the elements of the binary matrix row by row (each row separated by a new line):")
    binary_matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        binary_matrix.append(row)
    
    max_row_index = find_row_with_max_1s(binary_matrix)
    
    if max_row_index != -1:
        print(f"The row with the maximum number of 1s is at index: {max_row_index}")
    else:
        print("No rows found with 1s.")

def find_row_with_max_1s(matrix):
    max_count = 0
    max_row_index = -1
    
    for i, row in enumerate(matrix):
        count_1s = sum(row)
        if count_1s > max_count:
            max_count = count_1s
            max_row_index = i
            
    return max_row_index


if __name__ == "__main__":
    main()