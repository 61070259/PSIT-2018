"""GUN VIOLENCE DATA"""
import csv
def counting_crime():
    """Count number of crimes that happened in each year and add them to dictionary."""
    gun_data = open("gun-violence-data_01-2013_03-2018.csv", encoding="utf8")
    data = csv.reader(gun_data)
    crime = [row for row in data]
    count_set = [0, 0, 0, 0, 0, 0]
    crimes_count = {"2013": 0, "2014": 0, "2015": 0, "2016": 0, "2017": 0, "2018": 0}
    for crime_data in range(1, len(crimes)):
        date = crimes[crime_data][1]
        if date[:4] == "2013":
            count_set[0] += 1
            crimes_count["2013"] = count_set[0]
        elif date[:4] == "2014":
            count_set[1] += 1
            crimes_count["2014"] = count_set[1]
        elif date[:4] == "2015":
            count_set[2] += 1
            crimes_count["2015"] = count_set[2]
