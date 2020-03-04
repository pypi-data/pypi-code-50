from pydiagrams.Component import *
from pydiagrams.helpers.PUML     import Helper


with ComponentContext(Helper) as x:
    F = x.Frame
    P = x.Package
    R = x.Rectangle

    G = lambda l: F(l, fillcolor=color1)
    Sg = lambda l: F(l, fillcolor=color3)
    App = lambda s,l: R('**{s}**\\n{l}'.format(s=s, l=l), fillcolor=white)

    C = lambda l: x.Component(l, fillcolor=white)
    P = lambda s: F(s, fillcolor=color3)

    # Stores and Operations
    with G('Stores and Operations'):
        with Sg('POS'):
            vbs = App('VBS', 'Vision Bean Store')
            vod = App('VOD', 'Vision On Demand')

        fsis = App('FSIS', 'Frontline Sales Incentive Scheme')
        with P('SIM') as sim:
            C('Logistics')
            C('Inventory')
            C('Items')
            C('Stocktake')
            C('In Store Ordering')
            C('Customer Orders')

    # Merchandise
    with G('Merchandise'):
        with P('RMS') as rms:
            C('Merchandise Hierarchy')
            C('Location Management')
            C('Financial Management')
            C('Invoice Matching')
            C('Landed Costs')
            C('Items')
            C('Replenishment')
            C('Pricing')
            C('Suppliers')
            C('Consignments')
            C('Concession Stock')
            C('Ordering')

    # Food
    with G('Food'):
        amos = App('AMOS', 'Food Master Data')
        intactix = App('Intactix', 'Space Planning')
        episys = App('Episys', 'Ticket Printing')
        atria= App('Atria', 'Scales')
    
    