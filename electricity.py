import csv
import random

if __name__ == '__main__':
    fieldnames = ['Current batch', 'Voltage in techniques', 'Voltage in workplace', 'Votage in garage',
                  'Voltage in kitchen', 'Voltage in hall']
    with open('data/electricity.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        previous = {0: 220, 1:220, 2:220, 3:220, 4:220}
        random_number = random.randint(1, 100)
        for i in range(1, 501):
            values = {}
            for pos in range(5):
                sign = 1 if random.random() > 0.5 else -1

                if random.random() > 0.9:
                    values[pos] = round(previous[pos] + sign * random.randint(1, 10), 3)
                else:
                    values[pos] = round(previous[pos] + sign * random.random(), 3)

            previous = values
            writer.writerow({f'{fieldnames[0]}': f'{i}', f'{fieldnames[1]}': f'{values[0]}',
                             f'{fieldnames[2]}': f'{values[1]}', f'{fieldnames[3]}': f'{values[2]}',
                             f'{fieldnames[4]}': f'{values[3]}', f'{fieldnames[5]}': f'{values[4]}'})