"""PSIT PROJECT: GUN VIOLENCE DATA"""
import csv
import matplotlib.pyplot as plt
def gun_violence():
    """
    Create the required variables to use in another function and
    call them here.
    """
    gun_data = open("gun-violence-data_01-2013_03-2018_edited.csv", encoding="utf8")
    read = csv.reader(gun_data)
    case = [row for row in read]
    case_count = {"2014": 0, "2015": 0, "2016": 0, "2017": 0}
    case_with_victim = {"2014": 0, "2015": 0, "2016": 0, "2017": 0}
    victim = {"2014": 0, "2015": 0, "2016": 0, "2017": 0,}
    jan_mar = {"2014": 0, "2015": 0, "2016": 0, "2017": 0, "2018": 0}
    total_case = [0, 0, 0, 0]
    total_case_with_victim = [0, 0, 0, 0]
    total_victim = [0, 0, 0, 0]
    case_in_3_month = [0, 0, 0, 0, 0]
    all_case(case_count, total_case, case)
    with_victim(case_with_victim, total_case_with_victim, case)
    all_victim(victim, total_victim, case)
    three_month(jan_mar, case_in_3_month, case)
    graph(case_count, "case", total_case, "Amount of case", "-r^")
    graph(case_with_victim, "crime with victim", total_case_with_victim, "Case with victim", "-go")
    graph(victim, "victim", total_victim, "Victim", "-bs")
    graph(jan_mar, "case in 3 months", case_in_3_month, "Case in 3 months", "-yx")

def all_case(data_set, count, case):
    """Count number of case that happened from 1st January 2014 to 
    31th December 2017 and add them to dictionary."""
    for case_data in range(1, len(case)):
        date = case[case_data][0].split("/")
        if date[2] == "2014":
            count[0] += 1
            data_set["2014"] = count[0]
        elif date[2] == "2015":
            count[1] += 1
            data_set["2015"] = count[1]
        elif date[2] == "2016":
            count[2] += 1
            data_set["2016"] = count[2]
        elif date[2] == "2017":
            count[3] += 1
            data_set["2017"] = count[3]
    return data_set
    return sum(count)
    
def with_victim(data_set, count, case):
    """
    Count case with deaths and injured from 1st January 2014 to 
    31th December 2017 and add them to dictionary.
    """ 
    for case_data in range(1, len(case)):
        date = case[case_data][0].split("/")
        death = int(case[case_data][1])
        injured = int(case[case_data][2])
        if date[2] == "2014" and death+injured > 0:
            count[0] += 1
            data_set["2014"] = count[0]
        elif date[2] == "2015" and death+injured > 0:
            count[1] += 1
            data_set["2015"] = count[1]
        elif date[2] == "2016" and death+injured > 0:
            count[2] += 1
            data_set["2016"] = count[2]
        elif date[2] == "2017" and death+injured > 0:
            count[3] += 1
            data_set["2017"] = count[3]
    return data_set
    return sum(count)

def all_victim(data_set, count, case):
    """
    Count all deaths and injured from 1st January 2014 to 
    31th December 2017 and add them to dictionary.
    """
    for case_data in range(1, len(case)):
        date = case[case_data][0].split("/")
        death = int(case[case_data][1])
        injured = int(case[case_data][2])
        if date[2] == "2014":
            count[0] += death+injured
            data_set["2014"] = count[0]
        elif date[2] == "2015":
            count[1] += death+injured
            data_set["2015"] = count[1]
        elif date[2] == "2016":
            count[2] += death+injured
            data_set["2016"] = count[2]
        elif date[2] == "2017":
            count[3] += death+injured
            data_set["2017"] = count[3]
    return data_set
    return sum(count)

def three_month(data_set, count, case):
    """
    Count all cases from 1st January to 
    31th March in each year and add them to dictionary.
    """
    for case_data in range(1, len(case)):
        date = case[case_data][0].split("/")
        if date[2] == "2014" and int(date[1]) <= 3:
            count[0] += 1
            data_set["2014"] = count[0]
        elif date[2] == "2015" and int(date[1]) <= 3:
            count[1] += 1
            data_set["2015"] = count[1]
        elif date[2] == "2016" and int(date[1]) <= 3:
            count[2] += 1
            data_set["2016"] = count[2]
        elif date[2] == "2017" and int(date[1]) <= 3:
            count[3] += 1
            data_set["2017"] = count[3]
        elif date[2] == "2018" and int(date[1]) <= 3:
            count[4] += 1
            data_set["2018"] = count[4]
    return data_set
    return sum(count)

def graph(data, data_type, total, y_axis, style):
    """
    Draw graph from stored data
    """
    if len(data) < 5:
        x = ["2014", "2015", "2016", "2017"]
        y = [data["2014"], data["2015"], data["2016"], data["2017"]]
    else:
        x = ["2014","2015", "2016", "2017", "2018"]
        y = [data["2014"], data["2015"], data["2016"], data["2017"], data["2018"]]
    plt.plot(x, y, style)
    plt.xlabel("Year")
    plt.ylabel(y_axis)
    plt.show()
    print(data)
    print("Total %s: %d"%(data_type, sum(total)))

gun_violence()
