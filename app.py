"""GUN VIOLENCE DATA"""
import csv
def counting_crime():
    """Count number of crimes that happened in each year and add them to dictionary."""
    gun_data = open("gun-violence-data_01-2013_03-2018.csv", encoding="utf8")
    data = csv.reader(gun_data)
    crime = [row for row in data]
    count_set = [0, 0, 0, 0, 0, 0]
    crimes_count = {"2013": 0, "2014": 0, "2015": 0, "2016": 0, "2017": 0, "2018": 0}