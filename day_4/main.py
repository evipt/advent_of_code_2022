if __name__ == "__main__":

	with open('input.txt','r') as f:
		data = f.readlines()

#  Format the data in list of pairs
for i in range(len(data)):
    data[i] = data[i].rstrip().split(',')
#  Format the list of pairs in table of 4 integers, each line for one assignment pair
new_data = []
for pair in data:
    split_pair = pair[0].split('-') + pair[1].split('-')
    new_data.append(split_pair)

# Count of the pairs that one range fully contains the other (subsets) and the pairs that just overlap (overlaps)
def counter(sections):
    count_subsets = 0
    count_overlaps = 0   #this line was added for the Second Part

    for pair in sections:
        min_left = int(pair[0])
        max_left = int(pair[1])
        min_right = int(pair[2])
        max_right = int(pair[3])
        if min_left >= min_right and max_left <= max_right:
            # print(f'the left set {min_left} - {max_left} is a subset of the right set {min_right} - {max_right} ')
            count_subsets += 1 
            count_overlaps += 1	 #this line was added for the Second Part
        elif min_left <= min_right and max_left >= max_right:
            # print(f'the right set {min_right} - {max_right} is a subset of the left set {min_left} - {max_left} ')
            count_subsets += 1
            count_overlaps += 1   #this line was added for the Second Part
        else:
            set1 = set(range(min_left, max_left + 1))    #this line was added for the Second Part
            set2 = set(range(min_right, max_right + 1))  #this line was added for the Second Part
            if set1.intersection(set2) != set():         #this line was added for the Second Part
                count_overlaps +=1                       #this line was added for the Second Part
            # print(f'the left {min_left} - {max_left} and right pairs {min_right} - {max_right} are not contained in one another ')
    return count_subsets, count_overlaps
subsets, overlaps = counter(new_data)
print(f'the assignments pairs in which the one fully contains the other are: {subsets} and they just overlap are: {overlaps} ')
