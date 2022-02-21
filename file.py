from queue import PriorityQueue as pq

file_object = open('weblog.txt')
top_three = pq()
frequency_distribution = {}

for request in file_object:
    client_type = request.split(',')[3]
    if client_type in frequency_distribution:
        frequency_distribution[client_type] += 1
    else:
        frequency_distribution[client_type] = 1
file_object.close()

print(frequency_distribution)

for client_type in frequency_distribution:
    if top_three.qsize() < 3:
        top_three.put((frequency_distribution[client_type], client_type))
    else:
        top_client = top_three.get()
        current_min = top_client[0]
        current_num = frequency_distribution[client_type]
        if current_num > current_min:
            top_three.put((current_num, client_type))
        else:
            top_three.put((current_min, top_client[1]))

while top_three.qsize():
    print(top_three.get())


# to get list of words froma file
file = open('weblog.txt', 'r')
content = ','.join(line for line in file.read().splitlines())
# print(content)
content = content.split(',')
word_count = {}
for word in content:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
file.close()
count_list = []
file  = open('word_count.txt', 'w')
for count in word_count:
    count_entry = count + ', ' + str(word_count[count]) + '\n'
    count_list.append(count_entry)
file.writelines(count_list)