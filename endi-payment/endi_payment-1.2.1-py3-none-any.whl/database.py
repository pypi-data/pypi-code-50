# -*- coding: utf-8 -*-
"""
Specific session stuff used to store the payment history logs
"""
import traceback
import logging

from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
)


def get_session_factory(engine):
    """
    Build a session factory binding it to the given engine
    """
    factory = sessionmaker(autocommit=True)
    factory.configure(bind=engine)
    return factory

ModelBase = declarative_base()


class CriticalIntegrityError(Exception):
    """
    Error raised when we can't ensure the integrity of the current managed datas
    anymore
    """
    pass


class LocalSessionContext(object):
    def __init__(self):
        self.logger = logging.getLogger('endi_payment')

    @classmethod
    def set_session_factory(cls, factory):
        cls.session_factory = factory

    def __enter__(self):
        """
        Initialize a specific session
        """
        self.session = self.session_factory()
        self.session.begin(subtransactions=True)
        return self.session

    def __exit__(self, type, value, exception_traceback):
        if isinstance(type, Exception):
            self.logger.error(
                "We faced an exception while storing Payment history"
            )
            traceback.print_tb(exception_traceback)
            self.session.rollback()
            self.session.close()
        else:
            try:
                self.logger.debug(u"Persisting Payment History informations")
                self.session.commit()
                self.logger.debug("Committed")
            except:
                self.logger.debug("Rolling back")
                self.session.rollback()
                self.logger.exception(u"Error : Rolling back everything")
                raise CriticalIntegrityError(
                    u"Erreur critique rencontrée lors de la journalisation "
                    u"des évènements d'encaissement"
                )
            finally:
                self.logger.debug(u"Closing the session")
                self.session.close()


def configure_specific_payment_engine(config):
    """
    Configure un bindind spécifique (avec un utilisateur différent) pour la
    manipulation des instances de Payment

    Garder pour le principe mais ne sera peut être jamais utilisé.
    """
    settings = config.get_settings()
    if 'endi_payment_db.url' in settings:
        from sqlalchemy.orm import Session
        prefix = 'endi_payment_db.'

        engine = engine_from_config(settings, prefix=prefix)
        main_engine = engine_from_config(settings)

        class CustomSession(Session):
            def __init__(self, *args, **kwargs):
                Session.__init__(self, *args, **kwargs)

            def get_bind(self, mapper=None, clause=None):
                from endi.models.task.invoice import Payment
                if mapper is not None and issubclass(mapper.class_, Payment):
                    return engine
                else:
                    return main_engine

        from endi_base.models.base import DBSESSION
        DBSESSION.configure(class_=CustomSession)


def includeme(config):
    """
    Pyramid Include's mechanism
    Setup the library specific session
    """
    settings = config.get_settings()

    if 'endi_payment_db.url' in settings:
        # On a une connexion particulière pour l'édition des journaux
        prefix = 'endi_payment_db.'
        endi_payment_engine = engine_from_config(settings, prefix=prefix)

    else:
        # On utilise l'engine sqlalchemy par défaut (celui d'endi)
        endi_payment_engine = engine_from_config(settings)

    from endi_payment.models import EndiPaymentHistory  # NOQA

    session_factory = get_session_factory(endi_payment_engine)
    config.registry['endi_session_factory'] = session_factory

    LocalSessionContext.set_session_factory(session_factory)

    ModelBase.metadata.bind = endi_payment_engine
    ModelBase.metadata.create_all(endi_payment_engine)
    return True
