if __name__ == "__main__":

	with open('input.txt','r') as f:
		data = f.readlines()

def priority(item):
    if item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 38
    return priority

# PART ONE 
def sum_priorities(contents):
    sum = 0
    for rucksack in contents:
        rucksack = rucksack.rstrip(rucksack[-1])    
        mid = int(len(rucksack)/2)
        comp_1 = set(rucksack[:mid])
        comp_2 = set(rucksack[mid:])
        # print(comp_1)
        # print(comp_2)
        common = list(comp_1.intersection(comp_2))[0]
        sum += priority(common)
    return sum

# PART TWO 
def badge_sum_priorities(contents):
    sum = 0
    group = []
    for i in range(0,len(data),3):
        group = [set(data[j].rstrip()) for j in range(i,i+3)]
        badge = list(set.intersection(*group))
        badge = badge[0]
        badge_priority = priority(badge)
        sum += badge_priority
        group = []
    return sum

print(f'The sum of the priorities is: {sum_priorities(data)} ')
print(f'The sum of the badge priorities is: {badge_sum_priorities(data)} ')
