import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = (df[df['sex'] == 'Male']['age'].mean()).round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df[df['education'] == 'Bachelors']['education'].count()) * (100) / (df['education'].count())).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    SalaryofHigherEduPeople = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]['salary']
    higher_education = SalaryofHigherEduPeople.count()
    
    SalaryofLowerEduPeople = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]['salary']
    lower_education = SalaryofLowerEduPeople.count()

    # percentage with salary >50K
    HigherEducationRich = SalaryofHigherEduPeople[SalaryofHigherEduPeople == '>50K']
    NoOfHigherEducationRich = HigherEducationRich.count()
    higher_education_rich = (NoOfHigherEducationRich * 100 / higher_education).round(1)

    LowerEducationRich = SalaryofLowerEduPeople[SalaryofLowerEduPeople == '>50K']
    NoOfLowerEducationRich = LowerEducationRich.count()
    lower_education_rich = (NoOfLowerEducationRich * 100 / lower_education).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['salary']
    minHourWorker50K = num_min_workers[num_min_workers == '>50K']
    rich_percentage  = minHourWorker50K.count() * 100 / num_min_workers.count()

    # What country has the highest percentage of people that earn >50K?
    totalPeoplePerCountry = df['native-country'].value_counts()
    highEarners = df[df['salary'] == '>50K']
    highEarnerPerCountry = highEarners['native-country'].value_counts()
    percentageHighEarnersPerCountry = highEarnerPerCountry * 100 / totalPeoplePerCountry
    highest_earning_country = percentageHighEarnersPerCountry.idxmax()
    highest_earning_country_percentage = (percentageHighEarnersPerCountry.max()).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    highEarnersOccupationIndia = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = highEarnersOccupationIndia['occupation'].mode().item()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
# df = pd.read_csv('adult.data.csv')
calculate_demographic_data()