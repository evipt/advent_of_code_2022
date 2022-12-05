
def  most_calories(notes):
    
    calories = []  
    cur_elf_calories = 0

    for el in notes:  
        if el != '\n':
            cur_elf_calories += int(el)
        else:
            calories.append(cur_elf_calories)
            cur_elf_calories = 0 
    maximum = max(calories)
    index = calories.index(maximum)
    return index, maximum, calories


def get_top_three(loads):
    total = sum(sorted(loads, reverse=True,)[:3])
    return total




if __name__ == "__main__":

	with open('input.txt','r') as f:
		data = f.readlines()

		index, top_calories, calories_per_elf = most_calories(data)
		print(f'The {index+1}-th elf carrying the most calories:  {top_calories} calories ')

		top_three = get_top_three(calories_per_elf)
		print(f'The sum of the top three calories carried is: {top_three} ')