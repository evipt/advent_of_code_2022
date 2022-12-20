with open('input.txt', 'r') as f:
    input = f.readline().rstrip()

# the function takes as input the string and the 
# number of distinct characters that the 
# start-of-packet marker has 

def get_marker(signal, dist_char):
    l = len(signal)
    for i in range(l):
        start_of_packet = signal[i : i+dist_char]
        # list of the counts of each char 
        counts = [start_of_packet.count(ch) for ch in start_of_packet]
        if counts == [1]*dist_char:
            marker = start_of_packet
            loc = i + dist_char
            break
        
    return marker, loc

marker_1, loc_1 = get_marker(input,4)
marker_2, loc_2 = get_marker(input,14)
print(f'the marker in part 1 is {marker_1} and there are {loc_1} characters before the first start-of-message marker is detected')
print(f'the marker in part 2 is {marker_2} and there are {loc_2} characters before the first start-of-message marker is detected')