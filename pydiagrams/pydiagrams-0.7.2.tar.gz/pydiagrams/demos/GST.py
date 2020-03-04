from pydiagrams.Component import *
from pydiagrams.helpers.PUML import Helper

with ComponentContext(Helper)  as x:
    # Define some shortcuts for functions
    F=x.Frame
    C=x.Component
    I=x.Interface
    N=x.Node
    D=x.Database
    Cl=x.Cloud


    Online = I('Online')
    POS = I('POS')
    BP = I('BP')


    with x.Rectangle("EDW") as edw:
        XML3 = I('XML3')
        edw_stg = C("Stg")
        edw_rds = D("RDS")
        edw_dds = D("DDS")

        XML3 >> edw_stg >> edw_rds >> edw_dds

    POS >> XML3     
    Online >> XML3 % 'via AIT'

    with x.Rectangle("RMS") as rms:
        rms_dj_pos = D("DJ_POS_SALES_REALTIME")
        rms_dj_pos_hist = D("DJ_POS_SALES_HISTORY")
        rms_if_tran_data = D("IF_TRAN_DATA")
        rms_tran_data = D("TRAN_DATA")

        rms_tran_data_history = D("TRAN_DATA_HISTORY")

        rms_dj_pos >> rms_tran_data % "posupld"
        rms_tran_data >> rms_if_tran_data % "salstage"
        rms_tran_data >> rms_tran_data_history

        rms_dj_pos >> rms_dj_pos_hist

        BP_in = I('BP_in')
        BP_in >> XML3


    with x.Rectangle("Orafin") as orafin:
        fin_gl = D("General Ledger")


    edw_stg >> rms_dj_pos % 'XML'

    rms_if_tran_data >> fin_gl 
    BP >> BP_in