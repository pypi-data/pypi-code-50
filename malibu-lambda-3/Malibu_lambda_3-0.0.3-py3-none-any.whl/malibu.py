# Modify this function to return a list of strings as defined above
def list_benefits():
    return "Vacations", "Bonos", "Free food", "10 Free day in the year"

# " is a benefit of Job!"
def Job_benefit(benefit):
    return "%s is a benefit to work in this company!" % benefit


def name_the_benefits_of_job():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(Job_benefit(benefit))

name_the_benefits_of_job()