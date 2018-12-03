"""GUN VIOLENCE DATA"""
import csv
def counting_crime():
    """Count number of crimes that happened in each year and add them to the list."""
    gun_data = open("gun-violence-data_01-2013_03-2018.csv", encoding="utf8")
    data = csv.reader(gun_data)
    crime = [row for row in data]
    count_crime = []
