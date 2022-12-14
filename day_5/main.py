import pandas as pd

# if __name__ == "__main__":

stacks_init = pd.read_fwf('input_stacks.txt', header = None, nrows = 8)  # Load the initial stacks of crates in a df 
splits = [(0,4),(4,7),(7,12),(12,14),(14,17),(17,25)]
steps = pd.read_fwf('input_instructions.txt', header = None, colspecs=splits).drop([0,2,4], axis='columns') # Load the rearrangement steps in a df (only the ints)
steps.columns = ['# to move','origin','destination'] # Set column names to define the steps 

rows, columns = stacks_init.shape



def CrateMover9000():
    stacks = []
    for i in range(rows + 1):
        stacks.append(list(reversed(list(stacks_init[i].dropna()))))

    step = steps.shape[0]

    move = list(steps['# to move']) 
    origin = list(steps['origin'])
    dest = list(steps['destination'])


    for i in range(step): # for every step of the instructions 
        for j in range(move[i]): # for the number of elements that need to be moved 
            temp_origin = stacks[origin[i]-1]
            temp_crane = temp_origin.pop()
            temp_dest = dest[i]-1
            stacks[temp_dest].append(temp_crane)
    return stacks

machine1 = CrateMover9000()

def CrateMover9001():
    stacks = []
    for i in range(rows + 1):
        stacks.append(list(reversed(list(stacks_init[i].dropna()))))

    step = steps.shape[0]

    move = list(steps['# to move']) 
    origin = list(steps['origin'])
    dest = list(steps['destination'])

    for i in range(step): # for every step of the instructions 
        temp_move = []
        for j in range(move[i]): # for the number of elements that need to be moved 
            temp_origin = stacks[origin[i]-1]
            temp_crane = temp_origin.pop()
            temp_move.append(temp_crane)
        temp_dest = dest[i]-1
        stacks[temp_dest] = stacks[temp_dest] + list(reversed(temp_move))
    return stacks

machine2 = CrateMover9001()

def top_cranes(final_stacks):        
    top_cranes = str()
    for i in range(len(final_stacks)):
        top_cranes += final_stacks[i][-1].strip('[]')
    return top_cranes

print(f'The top cranes after the first machine are: {top_cranes(machine1)}')
print(f'The top cranes after the second machine are: {top_cranes(machine2)}')

