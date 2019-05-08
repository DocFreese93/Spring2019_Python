# -*- coding: utf-8 -*-
"""
Milo Freese
DAT119: Python 1
May 8th, 2019
Final Project

"""

import csv
import pandas as pd
import statistics

def main():
    
    # call functions to get results
    age_data_results()
    gender_results()
    neighborhood_results()
    
# This function analyzes the age portion of the csv file and
# writes the result onto a text file
def age_data_results():
    
    # Open File
    citations = open('Non Traffic Citations.csv')

    # Declare variable for file to be read
    data = csv.reader(citations)

    # Declare age list
    age = []

    # add items from file to list
    for row in data:
        age.append(row[4])

    # Delete data header
    del age[0]

    # Declare variables
    age_total = 0   # age total
    int_count = 0   # row counter
    mean = 0
    mode = 0
    median = 0
    highest = 0
    
    # accumulate age values
    for item in age:
        if item.strip():
            age_total += int(item)
            # increment counter variable
            int_count += 1

    # Declare variable and open file
    data_reader = pd.read_csv ('Non Traffic Citations.csv')
    
    # calculate mean, median, mode, max
    mean = age_total / int_count
    mode = statistics.mode(age)
    median = statistics.median(age)
    highest = data_reader['AGE'].max()
    
    # Close file
    citations.close()
    
    # Open file
    crime_data = open('Summary Offense Analysis.txt', 'a', encoding = 'utf-8')

    # write the header to the file
    crime_data.write('Summary of Offenders'' Age\n')
    crime_data.write('--------------------------\n')
    
    # write in data results
    crime_data.write('Average Age: ')
    crime_data.write('{:.2f}'.format(mean))
    crime_data.write('\n')
    crime_data.write('Mode: ')
    crime_data.write(mode)
    crime_data.write('\n')
    crime_data.write('Median: ')
    crime_data.write(median)
    crime_data.write('\n')
    crime_data.write('Highest Age: ')
    crime_data.write(str(highest))
    crime_data.write('\n')
    crime_data.write('\n')

    # Close file
    crime_data.close() 
    
# This function analyzes the gender portion of the csv file and
# writes the results onto a text file
def gender_results():
    
    # Declare variable and open file
    citation_file = open('Non Traffic Citations.csv')

    # Declare variable as readable file
    data_reader = csv.reader(citation_file)

    # Declare list variable
    gender = []

    # Add values to list
    for row in data_reader:
        gender.append(row[2])
        
    # delate column header
    del gender [0]

    # delcare gender count variables
    male_count = 0
    female_count = 0
    total = 0
    male_percent = 0
    female_percent = 0
    
    # Determine gender count
    for item in gender:
        if 'F' == item:
            female_count += 1
        elif 'M' == item:
            male_count += 1
        
    # determine total count of offenders
    total = male_count + female_count

    # calculate percentage of genders
    male_percent = male_count / total
    female_percent = female_count / total

    # close file
    citation_file.close()

    # Open file
    crime_data = open('Summary Offense Analysis.txt', 'a', encoding = 'utf-8')

    # write the header to the file
    crime_data.write('Summary of Offenders'' Gender\n')
    crime_data.write('-----------------------------\n')
    
    # write in data results
    crime_data.write('Number of Male Offenders: ')
    crime_data.write(str(male_count))
    crime_data.write('\n')
    crime_data.write('Number of Female Offenders:' )
    crime_data.write(str(female_count))
    crime_data.write('\n')
    crime_data.write('Percentage of Male Offenders: ')
    crime_data.write('{:.2f}'.format(male_percent * 100))
    crime_data.write('%\n')
    crime_data.write('Percentage of Female Offenders: ')
    crime_data.write('{:.2f}'.format(female_percent * 100))
    crime_data.write('%\n')
    crime_data.write('\n')

    # Close the file
    crime_data.close() 

# This function analyzes the neighborhood portion of the csv file and
# writes the result onto a text file
def neighborhood_results():
    
    # Declare variable and open file
    citation_file = open('Non Traffic Citations.csv')

    # Declare variable as readable file
    data_reader = csv.reader(citation_file)

    # Declare list
    neighborhood = []

    # Add values to list
    for row in data_reader:
        neighborhood.append(row[8])
    
    # remove column header
    del neighborhood[0]

    # Declare neighborhood variables
    allegheny_center = 0
    allegheny_west = 0
    allentown = 0
    arlington = 0
    arl_heights = 0
    banksville = 0
    bed_dwells = 0
    beechview = 0
    beltzhoover = 0
    bloomfield = 0
    bluff = 0
    bon_air = 0
    brighton_heights = 0
    brookline = 0
    carrick = 0
    cen_bus_dist = 0
    cen_larry = 0
    cen_north = 0
    cen_oak = 0
    chateau = 0
    chartiers = 0
    crafton_heights = 0
    duq_heights = 0
    e_allegheny = 0
    e_carnegie = 0
    e_hills = 0
    e_lib = 0
    elliot = 0
    esplen = 0
    fairywood = 0
    fineview = 0
    friendship = 0
    garfield = 0
    glen_hazel = 0
    greenfield = 0
    hays = 0
    hazelwood = 0
    highland_park = 0
    homewood_n = 0
    homewood_s = 0
    homewood_w = 0
    knoxville = 0
    larimer = 0
    lincoln_place = 0
    lower_larry = 0
    manchester = 0
    middle_hill = 0
    morningside = 0
    mt_oliver = 0
    mt_wash = 0
    new_homestead = 0
    n_oak = 0
    n_point_breeze = 0
    n_shore = 0
    northview_heights = 0
    oakwood = 0
    overbrook = 0
    perry_north = 0
    perry_south = 0
    point_breeze = 0
    n_point_breeze = 0
    polish_hill = 0
    regent_sq = 0
    ridgemont = 0
    shadyside = 0
    sheraden = 0
    s_oak = 0
    s_shore = 0
    s_side_flats = 0
    s_side_slopes = 0
    spring_garden = 0
    squirrel_hill_north = 0
    squirrel_hill_south = 0
    st_clair = 0
    stanton_heights = 0
    strip_dist = 0
    summer_hill = 0
    swisshelm_park = 0
    terrace_village = 0
    troy_hill = 0
    upper_hill = 0
    upper_larry = 0
    w_end = 0
    w_oak = 0
    westwood = 0
    windgap = 0
    
    # Determine Neighborhood count
    for item in neighborhood:
        
        if 'Allegheny Center' == item:
            allegheny_center += 1
        elif 'Allegheny West' == item:
            allegheny_west += 1
        elif 'Allentown' == item:
            allentown += 1
        elif 'Arlington' == item:
            arlington += 1
        elif 'Banksville' == item:
            banksville += 1
        elif 'Bedford Dwellings' == item:
            bed_dwells += 1
        elif 'Beechview' == item:
            beechview += 1
        elif 'Beltzhoover' == item:
            beltzhoover += 1
        elif 'Bloomfield' == item:
            bloomfield += 1
        elif 'Bluff' == item:
            bluff += 1
        elif 'Bon Air' == item:
            bon_air += 1
        elif 'Brighton Heights' == item:
            brighton_heights += 1
        elif 'Brookline' == item:
            brookline += 1
        elif 'Carrick' == item:
            carrick += 1
        elif 'Central Business District' == item:
            cen_bus_dist += 1
        elif 'Central Lawrenceville' == item:
            cen_larry += 1
        elif 'Central North Side' == item:
            cen_north += 1
        elif 'Central Oakland' == item:
            cen_oak += 1
        elif 'Chartiers' == item:
            chartiers += 1
        elif 'Chateau' == item: 
            chateau += 1
        elif 'Crafton Heights' == item:
            crafton_heights += 1
        elif 'Duquesne Heights' == item:
            duq_heights += 1
        elif 'East Allegheny' == item:
                e_allegheny += 1
        elif 'East Carnegie' == item:
            e_carnegie += 1
        elif 'East Hills' == item:
            e_hills += 1
        elif 'East Liberty' == item:
            e_lib += 1
        elif 'Elliot' == item:
            elliot += 1
        elif 'Esplen' == item:
            esplen += 1
        elif 'Fairywood' == item:
            fairywood += 1
        elif 'Fineview' == item:
            fineview += 1
        elif 'Friendship' == item:
            friendship += 1
        elif 'Garfield' == item:
            garfield += 1
        elif 'Glen Hazel' == item:
            glen_hazel += 1
        elif 'Greenfield' == item:
            greenfield += 1
        elif 'Hays' == item:
            hays += 1
        elif 'Hazelwood' == item:
            hazelwood += 1
        elif 'Highland Park' == item:
            highland_park += 1
        elif 'Homewood North' == item:
            homewood_n += 1
        elif 'Homewood South' == item:
            homewood_s += 1
        elif 'Homewood West' == item:
            homewood_w += 1
        elif 'Knoxville' == item:
            knoxville += 1
        elif 'Larimer' == item:
            larimer += 1
        elif 'Lincoln Place' == item:
            lincoln_place += 1
        elif 'Lower Lawrenceville' == item:
            lower_larry += 1
        elif 'Manchester' == item:
            manchester += 1
        elif 'Middle Hill' == item:
            middle_hill += 1
        elif 'Morningside' == item:
            morningside += 1
        elif 'Mount Oliver' == item:
            mt_oliver += 1
        elif 'Mount Washington' == item:
            mt_wash += 1
        elif 'New Homestead' == item:
            new_homestead += 1
        elif 'North Oakland' == item:
            n_oak += 1
        elif 'North Point Breeze' == item:
            n_point_breeze += 1
        elif 'North Shore' == item:
            n_shore += 1
        elif 'Northview Heights' == item:
            northview_heights += 1
        elif 'Oakwood' == item:
            oakwood += 1
        elif 'Perry North' == item:
            perry_north += 1
        elif 'Perry South' == item:
            perry_south += 1
        elif 'Point Breeze' == item:
            point_breeze += 1
        elif 'Point Breeze North' == item:
            n_point_breeze += 1
        elif 'Polish Hill' == item:
            polish_hill += 1
        elif 'Regent Square' == item:
            regent_sq += 1
        elif 'Ridgemont' == item:
            ridgemont += 1
        elif 'Shadyside' == item:
            shadyside += 1
        elif 'Sheraden' == item:
            sheraden += 1
        elif 'South Oakland' == item:
            s_oak += 1
        elif 'South Shore' == item:
            s_shore += 1
        elif 'South Side Flats' == item:
            s_side_flats += 1
        elif 'South Side Slopes' == item:
            s_side_slopes += 1
        elif 'Spring Garden' == item: 
            spring_garden += 1
        elif 'Squirrel Hill North' == item:
            squirrel_hill_north += 1
        elif 'Squirrel HIll South' == item:
            squirrel_hill_south += 1
        elif 'St. Clair' == item:
            st_clair += 1
        elif 'Stanton Heights' == item:
            stanton_heights += 1
        elif 'Strip District' == item:
            strip_dist += 1
        elif 'Summer Hill' == item:
            summer_hill += 1 
        elif 'Swisshelm Park' == item:
            swisshelm_park += 1
        elif 'Terrace Village' == item:
            terrace_village += 1
        elif 'Troy Hill' == item:
            troy_hill += 1
        elif 'Upper Hill' == item:
            upper_hill += 1
        elif 'Upper Lawrenceville' == item:
            upper_larry += 1
        elif 'West End' == item:
            w_end += 1
        elif 'West Oakland' == item:
            w_oak += 1
        elif 'Westwood' == item:
            westwood += 1
        elif 'Windgap' == item:
            windgap += 1

    # Establish dictionary and assign keys/values
    neighborhood_count = {'Allegheny Center': allegheny_center,
                          'Allegheny West': allegheny_west,
                          'Allentown': allentown,
                          'Arlington': arlington,
                          'Arlington Heights': arl_heights,
                          'Banksville': banksville,
                          'Bedford Dwellings': bed_dwells,
                          'Beechview': beechview,
                          'Beltzhoover': beltzhoover,
                          'Bloomfield': bloomfield,
                          'Bluff': bluff,
                          'Bon Air': bon_air,
                          'Brighton Heights': brighton_heights,
                          'Brookline': brookline,
                          'Carrick': carrick,
                          'Central Business District': cen_bus_dist,
                          'Central Lawrenceville': cen_larry,
                          'Central Northside': cen_north,
                          'Central Oakland': cen_oak,
                          'Chartiers': chartiers,
                          'Chateau': chateau,
                          'Crafton Heights': crafton_heights,
                          'Duquesne Heights': duq_heights,
                          'East Allegheny': e_allegheny,
                          'East Carnegie': e_carnegie,
                          'East Hills': e_hills,
                          'East Liberty': e_lib, 
                          'Elliot': elliot,
                          'Esplen': esplen,
                          'Fairywood': fairywood,
                          'Fineview': fineview,
                          'Friendship': friendship,
                          'Garfield': garfield,
                          'Glen Hazel': glen_hazel,
                          'Greenfield': greenfield,
                          'Hays': hays,
                          'Hazelwood': hazelwood,
                          'Highland Park': highland_park,
                          'Homewood North': homewood_n,
                          'Homewood South': homewood_s,
                          'Homewood West': homewood_w,
                          'Knoxville': knoxville,
                          'Larimer': larimer,
                          'Lincoln Place': lincoln_place,
                          'Lower Lawrenceville': lower_larry,
                          'Manchester': manchester,
                          'Middle Hill': middle_hill,
                          'Morningside': morningside,
                          'Mount Oliver': mt_oliver,
                          'Mount Washington': mt_wash,
                          'New Homestead': new_homestead,
                          'North Oakland': n_oak,
                          'North Point Breeze': n_point_breeze,
                          'North Shore': n_shore,
                          'Northview Heights': northview_heights,
                          'Oakwood': oakwood,
                          'Overbrook': overbrook,
                          'Perry North': perry_north,
                          'Perry South': perry_south,
                          'Point Breeze': point_breeze,
                          'Polish Hill': polish_hill,
                          'Regent Square': regent_sq,
                          'Ridgemont': ridgemont,
                          'St. Clair': st_clair,
                          'Shadyside': shadyside,
                          'Sheraden': sheraden,
                          'South Oakland': s_oak,
                          'South Shore': s_shore,
                          'South Side Flats': s_side_flats, 
                          'South Side Slopes': s_side_slopes,
                          'Spring Garden': spring_garden,
                          'Squirrel Hill North': squirrel_hill_north,
                          'Squirrel Hill South': squirrel_hill_south,
                          'Stanton Heights': stanton_heights,
                          'Strip District': strip_dist,
                          'Summer Hill': summer_hill,
                          'Swisshelm Park': swisshelm_park,
                          'Terrace Village': terrace_village,
                          'Troy Hill': troy_hill,
                          'Upper Hill': upper_hill,
                          'Upper Lawrenceville': upper_larry,
                          'West End': w_end,
                          'West Oakland': w_oak,
                          'Westwood': westwood,
                          'Windgap': windgap}

    # Declare list
    neighborhood_list = []

    # add values to list
    for key in neighborhood_count:
        neighborhood_list.append(neighborhood_count[key])
    
    # determine neighborhood with highest crime count
    high_crime = max(neighborhood_count, key=neighborhood_count.get)

    # determine neighborhood with lowest crime count
    low_crime = min(neighborhood_count, key=neighborhood_count.get)
    
    # Declare variables
    high_crime_num = 0
    low_crime_num = 0

     # assign high/low crime number to variable
    for crime in neighborhood_count:
        if high_crime == crime:
            high_crime_num = neighborhood_count[crime]
    for crime in neighborhood_count:
        if low_crime == crime:
            low_crime_num = neighborhood_count[crime]
    
    # Close file
    citation_file.close()
    
    # Open file
    crime_data = open('Summary Offense Analysis.txt', 'a', encoding = 'utf-8')

    # write the header to the file
    crime_data.write('Summary of Offenders'' Neighborhoods\n')
    crime_data.write('------------------------------------\n')
    
    # write in results
    crime_data.write('Neighborhood with highest number of crimes: ')
    crime_data.write(high_crime)
    crime_data.write(' - ')
    crime_data.write(str(high_crime_num))
    crime_data.write('\n')
    crime_data.write('Neighborhood with lowest number of crimes: ')
    crime_data.write(low_crime)
    crime_data.write(' - ')
    crime_data.write(str(low_crime_num))
    crime_data.write('\n')

    # Close the file
    crime_data.close()  

# Execute the main function
if __name__ == "__main__":
    main()