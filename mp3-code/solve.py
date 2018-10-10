import numpy as np

#AC3
def getKey(item):
    return len(item[1])

def solve(constraints):
    possible_row = [(idx,gen_row(len(constraints[0]),x)) for idx,x in enumerate(constraints[0])]
    sorted_possible_row = sorted(possible_row,key=getKey)
    for i in possible_row:
        print(i)
    possible_col = [gen_row(len(constraints[1]),x) for x in constraints[1]]
    rowsSoFar = []

def solve(rowsSoFar, possible_row, possible_col): #recursive
    for row in possible_row[0]:
        rowsSoFar.append(row)
        ret = isSafe(rowsSoFar, possible_col)
        if ret[0]:
            if len(rowsSoFar) == target:
                return rowsSoFar
            return solve(rowsSoFar, possible_row[1:],ret[1])
        else:
            
        rowsSoFar = rowsSoFar[:-1]

def isSafe(rowsSoFar, possible_col):
    for row in rowsSoFar:
        num_row = row[0]
        row_val = row[1]
        for idx,row_val in enumerate(row_val):
            curr_col_options = possible_col[idx]
            for idx, curr_col in curr_col_options:
                if curr_col[num_row] != row_val:
                    curr_col_options[idx] = None
            #remove nones
            if len(curr_col_options) == 0:
                return False
            possible_col[idx]= curr_col_options
    return True, possible_col




    """
    Implement me!!!!!!!
    This function takes in a set of constraints. The first dimension is the axis
    to which the constraints refer to. The second dimension is the list of constraints
    for some axis index pair. The third demsion is a single constraint of the form
    [i,j] which means a run of i js. For example, [4,1] would correspond to a block
    [1,1,1,1].

    The return value of this function should be a numpy array that satisfies all
    of the constraints.


	A puzzle will have the constraints of the following format:


	array([
		[list([[4, 1]]),
		 list([[1, 1], [1, 1], [1, 1]]),
         list([[3, 1], [1, 1]]),
		 list([[2, 1]]),
		 list([[1, 1], [1, 1]])],
        [list([[2, 1]]),
		 list([[1, 1], [1, 1]]),
		 list([[3, 1], [1, 1]]),
         list([[1, 1], [1, 1]]),
		 list([[5, 1]])]
		], dtype=object)

	And a corresponding solution may be:

	array([[0, 1, 1, 1, 1],
		   [1, 0, 1, 0, 1],
		   [1, 1, 1, 0, 1],
		   [0, 0, 0, 1, 1],
		   [0, 0, 1, 0, 1]])



	Consider a more complicated set of constraints for a colored nonogram.

	array([
	   [list([[1, 1], [1, 4], [1, 2], [1, 1], [1, 2], [1, 1]]),
        list([[1, 3], [1, 4], [1, 3]]),
		list([[1, 2]]),
        list([[1, 4], [1, 1]]),
		list([[2, 2], [2, 1], [1, 3]]),
        list([[1, 2], [1, 3], [1, 2]]),
		list([[2, 1]])],
       [list([[1, 3], [1, 4], [1, 2]]),
        list([[1, 1], [1, 4], [1, 2], [1, 2], [1, 1]]),
        list([[1, 4], [1, 1], [1, 2], [1, 1]]),
		list([[1, 2], [1, 1]]),
        list([[1, 1], [2, 3]]),
		list([[1, 2], [1, 3]]),
        list([[1, 1], [1, 1], [1, 2]])]],
		dtype=object)

	And a corresponding solution may be:

	array([
		   [0, 1, 4, 2, 1, 2, 1],
		   [3, 4, 0, 0, 0, 3, 0],
		   [0, 2, 0, 0, 0, 0, 0],
		   [4, 0, 0, 0, 0, 0, 1],
		   [2, 2, 1, 1, 3, 0, 0],
		   [0, 0, 2, 0, 3, 0, 2],
		   [0, 1, 1, 0, 0, 0, 0]
		 ])


    """
    dim0 = len(constraints[0])
    dim1 = len(constraints[1])
    return np.random.randint(2, size=(dim0, dim1))

def gen_row(w, s):
    """Create all patterns of a row or col that match given runs."""
    def gen_seg(o, sp):
        if not o:
            return [[0] * sp]
        return [[0] * x + o[0] + tail
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]
    # return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]
    sum = 0
    for i in s:
        sum+= i[0]
    return [x[1:] for x in gen_seg([[i[1]] * i[0] for i in s], w + 1 - sum)]
