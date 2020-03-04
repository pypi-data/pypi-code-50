from pydiagrams.Component import *

# Select from one of these Helpers (PUML recommended)
from pydiagrams.helpers.Graphviz import Helper
#from pydiagrams.helpers.PUML     import Helper
#from pydiagrams.helpers.GraphML     import Helper

SystemFill='#b9CDe5'
Helper.theme = r'w:\plantuml\theme-woolworths.iuml'

# Project attributes
connected_retail = {fillcolor:color3}
martech = {fillcolor:color7}

DPI=72
WIDTH=180/DPI

with ComponentContext(Helper) as x:
    x.attrs = {'width':WIDTH}
    with x.Frame('Amazon Web Services') as aws:
        F=aws.Frame
        with F('S3') as aws_s3:
            B=aws_s3.Node
            aws_s3_img = B('Image and Video Storage')

        with F('RDS') as aws_rds:
            D=aws_rds.Database
            aws_rds_inv = D('Inventory')

    with x.Frame('Data As a Service', fillcolor=SystemFill) as daas:
        
        G=daas.Frame # define a group function

        with G('API Gateway') as daas_api_gw:
            I=daas_api_gw.Interface

        with G('Services') as daas_services:
            F=daas_services.Frame
            with F('Personalisation', **connected_retail) as daas_pers:
                daas_pers_api = daas_api_gw.Interface('Personalisation APIs')
                prec = daas_pers.Component('Product Recs')
                offers = daas_pers.Component('Offers')
                daas_pers_api << daas_pers.all_except(shape=Interface)

            with F('Machine Learning', **martech) as daas_ml:
                daas_ml_api = daas_api_gw.Interface('ML APIs')
                cda = daas_ml.Component('Core Analytics')
                denrich = daas_ml.Component('Data Enrichment')
                seg = daas_ml.Component('Advanced Clustering')
                daas_ml_api << daas_ml.all_except(shape=Interface)

            with F('Customer Services', **connected_retail) as daas_cust:
                daas_cust_api = daas_api_gw.Interface('Customer APIs')
                uci = daas_cust.Component('Unified Customer Identity')
                daas_cust_api << daas_cust.all_except(shape=Interface)

            with F('Inventory', **connected_retail) as daas_inv:
                C=daas_inv.Component
                daas_inv_api = daas_api_gw.Interface('Inventory APIs')
                avail = C('Availability Service')
                inv = C('Inventory Service')
                find_in_store = C('Find In Store')
                if False: #Optionally show more detail
                    inv_monitor = C('Inventory Monitor')
                    inv_db = daas_inv.Database('Inventory DB')
                    inv << inv_monitor << inv_db
                inv << aws_rds_inv

                daas_inv_api << daas_inv.all_except(shape=Interface)

            with F('Pricing', **connected_retail) as daas_price:
                C=daas_price.Component
                daas_price_api = daas_api_gw.Interface('Pricing APIs')
                price = C('Price')
                order_calc = C('Order Calculation')
                promotions = C('Promotions')

                daas_price_api << daas_price.all_except(shape=Interface)


            with F('Product', **connected_retail) as daas_product:
                C=daas_product.Component
                daas_product_apis = daas_api_gw.Interface('Product APIs')

                image_service = C('Images')
                product_feed = C('Product Feeds')
                product_service = C('Product Service')

                daas_product_apis << daas_product.all_except(shape=Interface)

                image_service << aws_s3_img

            with F('Orders', **connected_retail) as daas_orders:
                C=daas_orders.Component
                daas_orders_apis = daas_api_gw.Interface('Order APIs')
                orders = C('Orders')
                fulfilment = C('Fulfillment')

                daas_orders_apis << daas_orders.all_except(shape=Interface)

        daas_dal      = daas.Component('Data Abstraction')
        daas_dal.attrs['width'] = len(daas_services.all()) * WIDTH 

        daas_dal.Id = 'daas_dal'
        daas_services.Id = 'daas_services'
        daas_api_gw.Id = 'daas_api_gw'

        daas_raw                = daas.Node('Raw')
        daas_business_layer     = daas.Node('Business Layer')
        daas_redshift           = daas.Database('Redshift')        
        
        daas_bi = daas.Interface('BI')
        daas_athena = daas.Interface('Athena')

        daas_raw ^ daas_business_layer ^ daas_redshift >= daas_bi
        daas_business_layer >= daas_athena

        daas_dal ^ daas_services.all()
        all_services = daas_services.all()
        daas_business_layer >> daas_dal

        # daas_dal ^ daas_services_in


    with x.Frame('Google Cloud Platform') as gcp:
        ga360 = gcp.Component('GA360')
        dv360 = gcp.Component('DV360')
        sa360 = gcp.Component('SA360')
        gcs = gcp.Node('Cloud Storage')
        gbq = gcp.Database('BigQuery')

        gcs ^ gcp.all_except(gcs) # Link gcs to all other Items in gcp

    with x.Frame('Systems of Engagement') as soe:
        with soe.Frame('Customer Engagement') as soe_ce:
            C=soe_ce.Component
            sfmc = C('SFMC')
            digm = C('[Digital Marketing]')
            dync = C('Movable Ink [Dynamic Content]')            
            cself = C('Customer Self Service')
            awsconn = C('Amazon Connect')

        with soe.Frame('POS / Smart Checkout') as soe_pos:
            C=soe_pos.Component
            pos = C('POS')
            sexp = C('Store Experience')

        with soe.Frame('Mobile') as soe_mobile:
            mobile = soe_mobile.Component('Customer Mobile App')

        with soe.Frame('Online Commerce') as soe_web:
            C=soe_web.Component
            ec = C('Headless UX')
            sli = C('SLI [Search]')
            ecp = C('eCommerce Content Personalisation')

        soe_int = soe.Interface('Interface')
        soe_api = soe.Interface('APIs')

        soe_api ^ soe.all_except(soe_int, soe_api) # Link apis to all SOE systems

    with x.Frame('Integration') as integration:
        C=integration.Component
        ait  = C('AIT')
        infm = C('Informatica')
        
        soe_int << integration.all() # link to all items


    with x.Frame('Systems of Record') as sor:

        F=sor.Frame

        cdc = sor.Interface('Change Database Capture (DMS)')
        saas_dal = sor.Interface('SaaS Connectors')
        dbconn = sor.Interface('Database Connectors')

        with F('Financials') as sor_fin:
            C=sor_fin.Component
            crgfin  = C('CRG OraFin')
            djfin   = C('DJ OraFin')

        with F('Merchandise & Supply Chain Systems') as sor_mer:
            C=sor_mer.Component
            djrms   = C('DJ RMS')
            crgrms  = C('CRG RMS')

        with F('Sales Transaction Systems') as sor_sales:
            C=sor_sales.Component
            edw     = C('EDW')
            djpos   = C('DJ POS')
            crgpos  = C('CRG POS')

        with F('Customer Systems', **martech) as sor_customer:
            sor_customer_int = sor_customer.Interface('Connectors')
            C=sor_customer.Component
            sfdc = C('SFDC')
            srvy = C('GetFeedback [Surveys]')
            cmpgn = C('[Campaign  Management]') 
            loyalty = C('[Loyalty]')           
            identity = C('[Identity and AccessManagement]', **connected_retail)

            sor_customer_int << sor_customer.all_except(sor_customer_int)

        with sor.Frame('eCommerce', **connected_retail) as sor_ecomm:
            sor_ecomm_int = sor_ecomm.Interface('Connectors')
            C=sor_ecomm.Component
            isams = C('iSAMS')
            pim = C('[Product Information Management]')
            dam = C('[Digital Asset Management]')
            search = C('SLI Search')
            cms = C('CMSaaS')
            payment = C('Payment Gateway')
            price_promo = C('[Price and Promotions Engine]')
            sor_ecomm_int << sor_ecomm.all_except(sor_ecomm_int)

        saas_dal <<  sor_ecomm_int
        saas_dal << sor_customer_int

        # link cdc to all items in sor_mer, sor_fin, sor_sales
        db_systems = sor_mer.all() + sor_fin.all_except(djfin) + sor_sales.all()
        #cdc << db_systems
        cdc << dbconn
        #dbconn << db_systems

        cdc ^ daas_raw

        dbconn << db_systems

        daas_dal << [dbconn , saas_dal]
        saas_dal << djfin

        sor_int = sor.Interface('SOR Interfaces')

        sor_int ^ integration.all()
        sor_int << dbconn

    daas_raw <= gcs
    gcs >> daas_raw 

    soe_int ^ sfmc 

    soe_api << daas_api_gw.all()

    infm >> gcs

