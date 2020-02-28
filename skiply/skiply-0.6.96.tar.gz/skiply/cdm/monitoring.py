#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from skiply.cdm.associationContractService import AssociationContractService
from skiply.cdm.service import Service

import skiply.cdm.service


class Monitoring(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_monitoring'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    monitoring_type = Column('type', int(), default='OTHERS')
    monitoring_last_alert = Column('last_alert', DateTime())
    monitoring_quittance = Column('quittance', Boolean(), default=False)

    device_skiply_id = Column('devicename', String(), ForeignKey("so_boitier.devicename"))

    #services = relationship('AssociationContractService', back_populates="contract")

    def __init__(self, monitoring_type, monitoring_last_alert, monitoring_quittance, device_skiply_id):#, service):
        self.monitoring_type = monitoring_type
        self.monitoring_last_alert = monitoring_last_alert
        self.monitoring_quittance = monitoring_quittance

        self.device_skiply_id = device_skiply_id

        #self.services = services

    def __repr__(self):
        return '<Monitoring %r - Alert %r>' % (self.device_skiply_id, self.monitoring_type)

def get_monitoring_alert(monitoring_id):
    session = db_session()
    try:
        results = session.query(Monitoring).filter(Monitoring.id == monitoring_id).first()
    except Exception as e:
        print("DB Request get_monitoring(monitoring_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_monitoring_alerts():
    session = db_session()
    try:
        results = session.query(Monitoring).all()
    except Exception as e:
        print("DB Request get_monitoring_alerts() Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_monitoring_alerts_for_device(device_skiply_id):
    session = db_session()
    try:
        results = session.query(Monitoring).filter(Monitoring.device_skiply_id == device_skiply_id).all()
    except Exception as e:
        print("DB Request get_monitoring_for_device(device_skiply_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_monitoring_alerts_for_devices(device_skiply_ids):
    session = db_session()
    try:
        results = session.query(Monitoring).filter(Monitoring.device_skiply_id.in_(device_skiply_ids)).all()
    except Exception as e:
        print("DB Request get_monitoring_for_device(device_skiply_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_monitoring_alerts_last_alerts(hours_start=None, hours_end=None, limit=1000):
    session = db_session()
    try:
        if service_id != None:
            results = session.query(Monitoring).filter(Monitoring.device_skiply_id == device_skiply_id).all()
        else: 
            results = None
    except Exception as e:
        print("DB Request get_contracts_for_services(service_ids) Failed with error : {}".format(e))
        results = None
    finally:
        session.close()

    return results