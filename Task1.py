with open('nginx_logs.txt') as file:
    data = []
    for line in file:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(data)