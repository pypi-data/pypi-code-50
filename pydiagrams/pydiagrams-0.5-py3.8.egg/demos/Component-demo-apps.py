from pydiagrams.Component import *
from pydiagrams.helpers.PUML     import Helper
# from pydiagrams.helpers.Graphviz     import Helper


with ComponentContext(Helper) as x:
    F = x.Frame
    P = x.Package
    R = x.Rectangle

    # Group
    G = lambda l: F(l, fillcolor=grey1)
    # System Group
    Sg = lambda l: F(l, fillcolor=grey4)
    # Application 
    App = lambda s,l: R('**{s}**\\n{l}'.format(s=s, l=l), fillcolor=white)

    # Component
    C = lambda l: x.Component(l, fillcolor=white)
    # Package
    P = lambda s: F(s, fillcolor=grey3)

    # Company
    DJ = lambda s=None: x.Package('David Jones '+s, fillcolor=color1)
    CRG = lambda s=None: x.Package('CRG ' +s, fillcolor=color3)
    PX = lambda s=None: x.Package('Politix '+s, fillcolor=color5)

    # Stores and Operations
    with G('Stores and Operations'):
        with DJ('sop'):
            with Sg('POS'):
                vbs = App('VBS', 'Vision Bean Store')
                dj_pos = App('VOD', 'Vision On Demand')

            fsis = App('FSIS', 'Frontline Sales Incentive Scheme')
            with P('SIM') as sim:
                C('Logistics')
                C('Inventory')
                C('Items')
                C('Stocktake')
                C('In Store Ordering')
                C('Customer Orders')

            App('Reflexis', 'Store Rostering')

        with CRG('sop'):
            crg_pos = App('Magenta', 'Point of Sale')
            App('Dayforce', 'Store Rostering')
            App('LeaseEagle', 'Lease Management')

        with PX('sop'):
            px_pos = App('Futura', 'Futura POS')

    # Merchandise
    with G('Merchandise'):
        # with P('RMS') as rms:
        #     C('Merchandise Hierarchy')
        #     C('Location Management')
        #     C('Financial Management')
        #     C('Invoice Matching')
        #     C('Landed Costs')
        #     C('Items')
        #     C('Replenishment')
        #     C('Pricing')
        #     C('Suppliers')
        #     C('Consignments')
        #     C('Concession Stock')
        #     C('Ordering')
        with DJ('mer'):
            App('BOA', 'Buyers Ordering Assistant')
            dj_rms = App('RMS', 'Merchandising (DJ)')
            dj_rdf = App('RDF', 'Retek Demand Forecasting')
            dj_fls = App('FLS', 'Food Legislation System')
        with CRG('mer'):
            crg_rms = App('RMS', 'Merchandising (CRG)')
            crg_mfp = App('MFP', 'Merchandise Financial Planning')
        with PX('mer'):            
            App('Futura', 'Merchandising System')

    # Online and Digital
    with G('Online and Digital'):
        with DJ('onl'):
            dj_isams = App('iSAMS', 'eCommerce (DJ)')
            dj_osm = App('OSM', 'Online Store Management (DJ)')        
            cobra = App('COBRA', 'Product Masterfiling')
            App('Admation', 'Digital Asset Management')

        with CRG('onl'):
            crg_isams = App('iSAMS', 'eCommerce (CR,TR,WY,MI)')
            App('Gallery', 'DAM')
            crg_osm = App('OSM', 'Online Store Management')        
        with PX('onl'):
            App('SFCC', 'Saleforce Commerce Cloud')

    # Food
    with G('Food'):
        with DJ('fd'):
            amos = App('AMOS', 'Food Master Data')
            intactix = App('Intactix', 'Space Planning')
            episys = App('Episys', 'Ticket Printing')
            atria= App('Atria', 'Scales')
    
    with G('Marketing and CRM'):
        sfmc = App('SFMC', 'Salesforce Marketing Cloud')
        sfdc = App('SFDC', 'Salesforce.com')


    with G('Finance'):
        with DJ('fin'):
            dj_orafin = App('Finacials', 'Oracle Financials (Cloud)')
            dj_epm = App('EPM', 'Financial Reporting')
            dj_eftrec = App('EFTREC', 'EFT Reconciliation')
            dj_tm1 = App('TM1', 'Financial Reporting')
            dj_quantum = App('Quantum', 'Treasury')
        with CRG('fin'):
            crg_orafin = App('Finacials', 'Oracle Financials (EBS)')
            crg_epm = App('EPM', 'Financial Reporting')

    with G('Human Resources'):
        with DJ('hr'):
            dj_empower = App('Empower', 'HR & Payroll')
            App('PageUp', 'Recruitment (DJ)')
            App('IPM', 'Employee Performance Management (DJ)')

        with CRG('hr'):
            crg_payglobal = App('PayGlobal', 'HR & Payroll')
            App('PageUp', 'Recruitment (CRG)')
            App('IPM', 'Employee Performance Management')
            App('eLearn', 'Training')

    with G('Product Design'):
        with CRG('pdd'):
            crg_plm = App('Lectra', 'Product Lifecycle Management')

    with G('Supply Chain'):
        with DJ('sc'):
            dj_wms = App('Manhattan', 'Manhattan WMOS (DJ)')
            dj_sps = App('SPS', 'EDI Gateway')

        with CRG('sc'):
            crg_wms = App('Manhattan', 'Manhattan WMOS (CRG,PX)')
            App('Shaefer', 'Warehouse Control System')
            App('Damco', 'Freight Forwarding')
            App('IPT', 'EDI Gateway')

    with G('IT Administration'):
        App('ServiceNow', 'IT Service Management')
        App('JIRA', 'Project Management')
        App('Clarity', 'Time Management')


    # Links
    dj_rms >> dj_isams
    crg_rms >> crg_isams
    cobra >> dj_rms
    crg_osm >> crg_rms
    dj_osm >> dj_rms
    dj_empower >> dj_orafin
    crg_payglobal >> crg_orafin
    dj_rms >> dj_orafin
    dj_pos >> dj_rms
    crg_pos >> crg_rms
    dj_rms >> dj_wms
    crg_rms >> crg_wms
    crg_plm >> crg_rms