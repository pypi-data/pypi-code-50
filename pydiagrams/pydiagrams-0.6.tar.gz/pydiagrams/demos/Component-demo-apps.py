from pydiagrams.Component import *
# from pydiagrams.helpers.PUML     import Helper
from pydiagrams.helpers.Graphviz     import Helper
from pydiagrams.helpers.GraphML     import Helper

Helper.output_format = 'svg'

with ComponentContext(Helper) as x:
    F = x.Frame
    P = x.Package
    R = x.Rectangle

    # Group
    G = lambda l: F(l, fillcolor=grey1)
    # System Group
    Sg = lambda l: F(l, fillcolor=grey4)

    # Application
    if Helper.name == 'PUML': 
        app_format = '**{s}**\\n{l}'
    elif Helper.name == 'Graphviz':
        Helper.html_labels = True
        app_format = '<table border="0" cellpadding="0"><tr><td align="center"><B>{s}</B></td></tr><tr><td>{l}</td></tr></table>'
    else:
        app_format = '{s}\\n{l}'

    node_properties = {
        'GraphML':{'width':210, 'height':30}
    }

    App = lambda s,l: R(app_format.format(s=s, l=l), fillcolor='#FFFFFF', **node_properties.get(Helper.name, {}))

    # Component
    C = lambda l: x.Component(l, fillcolor=white)
    # Package
    P = lambda s: F(s, fillcolor=grey3)

    # Company
    if Helper.name == 'PUML':
        cobu_format = '{co} ({bu})'
    else:
        cobu_format = '{co}'

    Company_BusinessUnit = lambda company_name, business_unit, fill: x.Package(cobu_format.format(co=company_name, bu=business_unit), fillcolor=fill)
    # Define region functions for the Companies to use
    DJ   = lambda s=None: Company_BusinessUnit('David Jones', s, color1)
    CRG  = lambda s=None: Company_BusinessUnit('CRG', s, color3)
    PX   = lambda s=None: Company_BusinessUnit('Politix', s, color7)

    # -------------------------------------------------------------------------------------------------------------------

    # Stores and Operations
    with G('Stores and Operations'):
        with DJ('sop'):
            with Sg('POS'):
                vbs = App('VBS', 'Vision Bean Store')
                dj_pos = App('VOD', 'Vision On Demand')

            fsis = App('FSIS', 'Frontline Sales Incentive Scheme')
            sim = App('SIM', 'Store Inventory Management')
            # with P('SIM') as sim:
            #     C('Logistics')
            #     C('Inventory')
            #     C('Items')
            #     C('Stocktake')
            #     C('In Store Ordering')
            #     C('Customer Orders')

            App('Reflexis', 'Store Rostering')

            episys = App('Episys', 'Ticket Printing (Food)')
            atria= App('Atria', 'Scales (Food)')

        with CRG('sop'):
            crg_pos = App('Magenta', 'Point of Sale')
            App('Dayforce', 'Store Rostering')
            App('LeaseEagle', 'Lease Management')

        with PX('sop'):
            px_pos = App('Futura', 'Futura POS')

    # Merchandise
    with G('Merchandise'):

        with DJ('mer'):
            dj_boa = App('BOA', 'Buyers Ordering Assistant')
            dj_rms = App('RMS', 'Merchandising (DJ)')
            dj_rdf = App('RDF', 'Retek Demand Forecasting')
            dj_fls = App('FLS', 'Food Legislation System')
            amos = App('AMOS', 'Food Master Data')
            intactix = App('Intactix', 'Space Planning')

            dj_boa >> dj_rms
            dj_rms >> [dj_rdf, dj_fls, amos]


        with CRG('mer'):
            crg_rms = App('RMS', 'Merchandising (CRG)')
            crg_mfp = App('MFP', 'Merchandise Financial Planning')
        with PX('mer'):            
            px_rms = App('Futura', 'Merchandising System')

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
            px_sfcc = App('SFCC', 'Saleforce Commerce Cloud')

    with G('Marketing and CRM'):
        sfmc = App('SFMC', 'Salesforce Marketing Cloud')
        sfdc = App('SFDC', 'Salesforce.com')


    with G('Finance'):
        with DJ('fin'):
            with Sg('Oracle Financials (Cloud)'):
                dj_orafin_gl = App('GL', 'General Ledger')
                dj_orafin_ar = App('AR', 'Accounts Receivable')
                dj_orafin_ap = App('AP', 'Accounts Payable')

            #dj_orafin = App('Finacials', 'Oracle Financials (Cloud)')
            dj_epm = App('EPM', 'Financial Reporting')
            dj_eftrec = App('EFTREC', 'EFT Reconciliation')
            dj_tm1 = App('TM1', 'Financial Reporting')
            dj_quantum = App('Quantum', 'Treasury')

            dj_orafin_gl >> [dj_epm, dj_tm1, dj_quantum]
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
            dj_edi = App('SPS', 'EDI Gateway')

        with CRG('sc'):
            crg_wms = App('Manhattan', 'Manhattan WMOS (CRG,PX)')
            crg_sc_wcs = App('Shaefer', 'Warehouse Control System')
            crg_sc_ff = App('Damco', 'Freight Forwarding')
            crg_sc_edi = App('IPT', 'EDI Gateway')

    with G('IT Administration'):
        App('ServiceNow', 'IT Service Management')
        App('JIRA', 'Project Management')
        App('Clarity', 'Time Management')


    # Links
    # Online
    dj_rms >> dj_isams
    crg_rms >> crg_isams
    dj_osm >> dj_rms

    cobra >> dj_rms
    crg_osm >> crg_rms
    px_rms >> px_sfcc

    # HR
    dj_empower >> dj_orafin_gl
    crg_payglobal >> crg_orafin

    # RMS
    dj_rms >> dj_orafin_gl
    crg_rms >> crg_orafin

    dj_pos >> dj_rms
    px_pos >> px_rms
    crg_pos >> crg_rms

    # WMS
    dj_rms >> dj_wms
    dj_wms >> dj_edi
    crg_rms >> crg_wms
    crg_wms >>  [crg_sc_wcs, crg_sc_ff, crg_sc_edi]

    crg_plm >> crg_rms

    dj_rms >> amos
    
    dj_rms >> sfdc
    sfdc   >> dj_isams
