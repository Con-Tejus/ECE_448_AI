import numpy as np
import copy

#AC3
def getKey(item):
    return len(item[1])

def format(thing):
    sorted_thing = sorted(thing)
    # print(sorted_thing)
    formatted = []
    # for row in reversed(sorted_thing):
    #     formatted.append([x for x in reversed(row[1])])
    for row in sorted_thing:
        formatted.append(row[1])
    return formatted

def solve(constraints):
    # print(constraints[0])
    possible_row = [(idx,gen_row(len(constraints[1]),x)) for idx,x in enumerate(constraints[0])]
    sorted_possible_row = sorted(possible_row,key=getKey)
    possible_col = [gen_row(len(constraints[0]),x) for x in constraints[1]]
    # print(len(sorted_possible_row),len(possible_col))
    for idx,curr in enumerate(possible_col):
        if curr == []:
            possible_col[idx] = [[0]*len(possible_col)]
    rowsSoFar = []
    target = len(possible_row)
    to_be_formatted = solveR(rowsSoFar,sorted_possible_row,possible_col,target)
    print(to_be_formatted)
    sol = np.array(format(to_be_formatted))
    print(sol)
    return sol

def solveR(rowsSoFar, sorted_possible_row, possible_col,target): #recursive
    print('solveR')
    if len(rowsSoFar) == target:
        return rowsSoFar
    curr_row_set = sorted_possible_row[0]
    # print(curr_row_set)
    num_row = curr_row_set[0]
    # print(len(curr_row_set[1]))
    for curr_row in curr_row_set[1]:
        rowsSoFar.append((num_row,curr_row))
        # print(rowsSoFar)
        ret = isSafe(rowsSoFar, possible_col)
        if ret[0]:
            child_ret = solveR(copy.deepcopy(rowsSoFar),sorted_possible_row[1:],ret[1],target)
            if child_ret[0]:
                return child_ret
        rowsSoFar = rowsSoFar[:-1]
    return False, None


def isSafe(rowsSoFar, given_possible_col):
    possible_col = copy.deepcopy(given_possible_col)
    # print(possible_col)
    if len(rowsSoFar) == 0:
        return True, possible_col
    for row in rowsSoFar:
        num_row = row[0]
        curr_row = row[1]
        for row_idx, row_val in enumerate(curr_row):
            curr_col_options = possible_col[row_idx]
            for col_idx, curr_col in enumerate(curr_col_options):
                if curr_col[num_row] != row_val:
                    curr_col_options[col_idx] = None
            curr_col_options = [x for x in curr_col_options if x != None]
            if len(curr_col_options) == 0:
                return False, None
            possible_col[row_idx] = curr_col_options
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
