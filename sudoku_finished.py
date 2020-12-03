def done_or_not(board): #board[i][j]
  # your solution here
  # ..
  # return 'Finished!'
  # ..
  # or return 'Try again!'
  cols = []
  for c in range(9):
    cols.append(set())

  squares = []
  for s in range(9):
    squares.append(set())

  # look at each row
  for i in range(len(board)):
    row = board[i]
    print("row", row)
    nums = set()
    # look at each col of row
    for j in range(len(row)):
      num = board[i][j]
      print("num", num)
      if num in nums or num in cols[j]:
        print("Try again!")
        return
      else:
        nums.add(num)
        cols[j].add(num)
      print("nums row set", nums)
      print(f"col {j} set: {cols[j]}")
  
  print("Finished!")

done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])

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