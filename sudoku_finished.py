def done_or_not(board): #board[i][j]
    # your solution here
    # ..
    # return 'Finished!'
    # ..
    # or return 'Try again!'
    
    # Create matrix for column sets
    cols = []
    for c in range(9):
        cols.append(set())
    
    # Create matrix for square sets
    squares = []
    for s in range(9):
        squares.append(set())

    # look at each row
    for i in range(len(board)):
        row = board[i]
        nums = set()
        # look at each col of row
        for j in range(len(row)):
            num = board[i][j]
        # Set num_sq to which square on board the num belongs to
            if 0 <= i <= 2 and 0 <= j <=2:
                num_sq = 0
            elif 0 <= i <= 2 and 3 <= j <= 5:
                num_sq = 1
            elif 0 <= i <= 2 and 6 <= j <=8:
                num_sq = 2
            elif 3 <= i <= 5 and 0 <= j <=2:
                num_sq = 3
            elif 3 <= i <= 5 and 3 <= j <=5:
                num_sq = 4
            elif 3 <= i <= 5 and 6 <= j <=8:
                num_sq = 5
            elif 6 <= i <= 8 and 0 <= j <=2:
                num_sq = 6
            elif 6 <= i <= 8 and 3 <= j <=5:
                num_sq = 7
            elif 6 <= i <= 8 and 6 <= j <=8:
                num_sq = 8

            if num in nums or num in cols[j] or num in squares[num_sq]:
                return "Try again!"
            else:
                nums.add(num)
                cols[j].add(num)
                squares[num_sq].add(num)

    return "Finished!"

# test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');
                        
# test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');