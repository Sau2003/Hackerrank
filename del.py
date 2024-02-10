Alice_friends = {'Alice','Magnus', 'Max', 'Charlie', 'Agatha', 'Bob'}
Bob_friends = {'Bob','Violet', 'Collei', 'Magnus', 'Charlie', 'Alice'}
Charlie_friends = {'Charlie','Alice', 'Bob', 'Violet', 'Agatha', 'Magnus'}

common_friends = Alice_friends & Bob_friends & Charlie_friends
non_common_friends = (Alice_friends | Bob_friends | Charlie_friends) - common_friends

print("Common friends:", common_friends)
print("Non-common friends:", non_common_friends)
