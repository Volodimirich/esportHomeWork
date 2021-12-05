import csv
import random

if __name__ == '__main__':
    fieldnames = ['Batch', 'Techniques', 'Workplace', 'Garage', 'Kitchen', 'Hall']
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
                    values[pos] = previous[pos] + sign * random.randint(1, 10)
                else:
                    values[pos] = previous[pos] + sign * random.random()

            previous = values
            writer.writerow({'Batch': f'{i}', 'Techniques': f'{values[0]}',  'Workplace': f'{values[1]}',
                             'Garage': f'{values[2]}', 'Kitchen' : f'{values[3]}', 'Hall' : f'{values[4]}'})