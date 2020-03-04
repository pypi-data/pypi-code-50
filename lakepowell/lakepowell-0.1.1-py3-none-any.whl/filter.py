import pandas as pd

class Filter:
    # initialize filter object with pandas data frame
    def __init__(self, df):
        self.df = df.copy() #pandas data frame copied to avoid pointer problems

    # select columns of interest by name
    def selectColumns(self, cols):
        self.df = self.df[cols]

    #filter based of of values in given list
    def givenGear(self, gear):
        self.df = self.df[self.df.Gear.isin(gear)]

    #filter based of of values in given list
    def givenSpecies(self, species):
        self.df = self.df[self.df.Species.isin(species)]

    #male and female are True/False values
    def givenSexes(self, male, female):
        if male and female: #all data with Male or Female distinction
            self.df = self.df[self.df.Sex == "M" or self.df.Sex == "F"]
        elif male and not female: #only males
            self.df = self.df[self.df.Sex == "M"]
        elif not male and female: #only females
            self.df = self.df[self.df.Sex == "F"]

    #filter based of of values in given list
    def givenSites(self, sites):
        self.df = self.df[self.df.Site.isin(sites)]

    #inclusive range
    def rangeLength(self, low, high):
        self.df = self.df[self.df.Length >= low]
        self.df = self.df[self.df.Length <= high]

    #inclusive range
    def rangeMass(self, low, high):
        self.df = self.df[self.df.Mass >= low]
        self.df = self.df[self.df.Mass <= high]

    #inclusive range
    def rangeKtl(self, low, high):
        self.df = self.df[self.df.Ktl >= low]
        self.df = self.df[self.df.Ktl <= high]

    #filter Year column between given years
    def rangeYears(self, year1, year2):
        self.df = self.df[self.df.Year >= year1]
        self.df = self.df[self.df.Year <= year2]

    #filter Month column between given months
    def rangeMonths(self, month1, month2):
        self.df = self.df[self.df.Month >= month1]
        self.df = self.df[self.df.Month <= month2]

    #filter Day between given days
    def rangeDays(self, day1, day2):
        self.df = self.df[self.df.Day >= day1]
        self.df = self.df[self.df.Day <= day2]

    #filter rows only between the given dates - will work with bad dates as long
    #as they are numbers
    def betweenDates(self, d1, m1, y1, d2, m2, y2):
        self.rangeYears(y1, y2)
        self.df = self.df[(self.df.Month >= m1) & (self.df.Day >= d1)]
        self.df = self.df[(self.df.Month <= m2) & (self.df.Day <= d2)]

    #filter based on given months
    def givenMonths(self, months):
        self.df = self.df[self.df.Month.isin(months)]

    #filter based on given years
    def givenYears(self, years):
        self.df = self.df[self.df.Year.isin(years)]
