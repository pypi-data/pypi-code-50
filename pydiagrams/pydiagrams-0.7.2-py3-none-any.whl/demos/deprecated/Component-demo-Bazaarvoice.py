# Attempting an ideal syntax that uses local variables
# eg:
# instead of defining a component:
#   rms.Component('rms_prod', 'Products')
# do this:
#   rms_prod = rms.Component('Products')

# Lines:
#       >>  link (vertical arrow)
#       >>= dotted link (vertical dotted)
#       -   horizontal line (no arrows)
#       ==  vertical line  (no arrows)
# With Direction:
#       ^   up
#       >=  right
#       <=  left
#       |   down

from pydiagrams.Component import *

with ComponentContextPUML()  as x:

    with x.Database("RMS", fillcolor='adfcad') as rms:
        rms_prod    = rms.Component('Products')
        rms_sales   = rms.Component('Sales')
        rms_pf      = rms.Interface('[DR1] Product Feed')
        rms_sf      = rms.Interface("[DR2] Sales Feed")
        rms_cra     = rms.Interface('[DR3] Customer Review Authorisation')

        rms_prod >> rms_pf
        rms_sales >> rms_sf
        rms_sales >> rms_cra


    with x.Frame("Biztalk 2016") as bt:
        int_pf = bt.Interface('[DI1] Product Feed')


    with x.Cloud("Informatica Cloud") as ic:
        with ic.Frame("Data Integration", fillcolor=white) as di:
            int_sf = di.Interface('[DI2] Sales Feed')
            int_cf = di.Interface('[DI3] Client Feed')

        with ic.Frame("Application Integration", fillcolor=white) as ai:
            inf_cra = ai.Interface("[DA1] Customer Review Authorisation")


    with x.Cloud("BazaarVoice", fillcolor='d5adfc') as bv:
        bv_pie      = bv.Interface("Post-interaction email feed")
        bv_pf       = bv.Interface("Product Feed")
        bv_prod     = bv.Component("Products")
        bv_sales    = bv.Component("Post Interface Events")
        bv_reviews  = bv.Component("Reviews")
        bv_pie  >> bv_sales
        bv_pf   >> bv_prod
        bv_email    = bv.Interface("Outbound Emails")
        bv_scf      = bv.Interface("Standard Client Feed")

        bv_sales >> bv_email
        bv_prod  >> bv_email

        bv_reviews ^ bv_scf #Up arrow

    with x.Cloud("iSAMS", fillcolor='adfcfc') as isams:
        is_prod = isams.Component('Products')
        is_pdp  = isams.Interface('Product Detail Page')
        is_plp  = isams.Interface('Product Listing Page')
        is_pr   = isams.Interface('Product Review Page')

        is_prod ^ is_plp #Up
        is_prod ^ is_pdp #Up


    with x.Cloud("Google Cloud Platform / AWS S3", fillcolor='fcd5ad') as cloud:
        cloud_crm = cloud.Component('Customer Product Reviews')


    with x.Cloud('Salesforce') as sf:
        sf_crm  = sf.Component('Customer Product Reviews', note='Out of Scope')

    # main group
    c = x.Actor('Customer')

    bv_email >> c % "Email"

    rms_pf >> int_pf
    int_pf >> bv_pf % "SFTP"

    rms_sf >> int_sf
    int_sf >> bv_pie % 'SFTP'

    c >> is_pr % "Writes Review"
    is_pr >> bv_reviews

    bv_reviews >> is_plp % "Rating and Review"
    bv_reviews >> is_pdp % "Rating and Review"

    bv_scf ^ int_cf # Up
    int_cf ^ cloud_crm # Up

    sf_crm | cloud_crm %  "via API" #down

    # Customer Review Authorisation
    inf_cra >> rms_cra
    is_pdp >> inf_cra % 'Online Review Auth'


