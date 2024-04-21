import csv
import statistics
import random
import webbrowser

try:
    year = int(input("Enter a year:"))

    with open("sets.csv", newline="") as data_file:
        reader = csv.reader(data_file)

        number_of_sets = 0
        number_of_elements = []
        sets_image_link = []

        next(reader)

        for row in reader:
            if int(row[2]) == year:
                number_of_sets += 1
                number_of_elements.append(int(row[4]))
                sets_image_link.append(row[5])

        if(number_of_sets) == 0:
            print(f"No sets found for the year {year}.")
        else:
            average_elements_in_set = sum(number_of_elements)/number_of_sets
            median_elements_in_set = statistics.median(number_of_elements)

            print(f"Number of sets in {year}: {number_of_sets}")
            print(f"Average number of elements in sets: {int(average_elements_in_set)}")
            print(f"Median number of elements in sets: {int(median_elements_in_set)}")

        random_picture = random.choice(sets_image_link)
        webbrowser.open(random_picture)


except ValueError:
    print("Input has to be a year")

except Exception as e:
    print("An error occurred:", e)
