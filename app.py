"""GUN VIOLENCE DATA"""
import csv
def gun_violence():
    """Create the required variables to use in another function and call them here."""
    gun_data = open("gun-violence-data_01-2013_03-2018.csv", encoding="utf8")
    data = csv.reader(gun_data)
    case = [row for row in data]
    case_count = {"2013": 0, "2014": 0, "2015": 0, "2016": 0, "2017": 0, "2018": 0}
    all_case(case_count, case)
def all_case(data_set, case):
    """Count number of case that happened in each year and add them to dictionary."""
    count_set = [0, 0, 0, 0, 0, 0]
    for case_data in range(1, len(case)):
        date = case[crime_data][1]
        if date[:4] == "2013":
            count_set[0] += 1
            data_set["2013"] = count_set[0]
        elif date[:4] == "2014":
            count_set[1] += 1
            data_set["2014"] = count_set[1]
        elif date[:4] == "2015":
            count_set[2] += 1
            data_set["2015"] = count_set[2]
        elif date[:4] == "2016":
            count_set[3] += 1
            data_set["2016"] = count_set[3]
        elif date[:4] == "2017":
            count_set[4] += 1
            data_set["2017"] = count_set[4]
        elif date[:4] == "2018":
            count_set[5] += 1
            data_set["2018"] = count_set[5]
    print(data_set)
    print("Total case: %d"%sum(count_set))
gun_violence()
