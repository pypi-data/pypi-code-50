#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytz
from datetime import datetime
import time
import collections

import pkg_resources
import numpy as np

from sqlalchemy import Table, Column, Integer, String, Boolean, Sequence, ForeignKey
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base

from bob.db.base import File
from bob.db.base.sqlalchemy_migration import Enum, relationship
from bob.io.base import HDF5File

from .batl_config import BATL_CONFIG
from .loader import load_video_stream_from_hdf5, load_data_config, convert_arrays_to_frame_container
import logging

logger = logging.getLogger(__name__)

Base = declarative_base()

protocolPurpose_file_association = Table('protocolPurpose_file_association', Base.metadata,
  Column('protocolPurpose_id', Integer, ForeignKey('protocolPurpose.id')),
  Column('file_id',  Integer, ForeignKey('video_file.id')))

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    is_presenter = Column(Boolean)

    def __init__(self, id, is_presenter):
        self.id = id
        self.is_presenter = is_presenter

    def __repr__(self):
        return "<Client('%d', '%s')>" % (self.id, 'is presenter' if self.is_presenter else 'is not presenter' )

class RppgFile(Base, File):

    """A class containing file related information of the BATL database.

    Attributes
    ----------
    path : str
        A relative path to the file.
    """
    __tablename__ = 'rppg_file'

    id = Column(Integer, Sequence('RF_seq'), primary_key=True)
    path = Column(String(100), unique=True)

    def __init__(self, path):

        super(RppgFile, self).__init__(path=path)
        self.path = path

    def load(self, directory=None, extension='.txt'):
        """Summary

        Parameters
        ----------
        ``directory`` : :py:class:`str`
            If not empty or None, this directory is prefixed to the final
            file destination. Default: ``None``.
        ``extension`` : :py:class:`str`
            The extension of the file. Default for this database is
            '.txt'.

        Returns
        -------
        TYPE
            Description
        """
        filepath = self.make_path(directory, extension)
        with open(filepath, 'r') as rppg_file:
            for line_number, line in enumerate(rppg_file):
                if line_number == 3:
                    ln = line.strip().split()
                    date = ln[2]
                    t = ln[5]
                    timezone = pytz.timezone('Europe/Zurich')
                    dt = datetime.strptime("{} {}".format(date, t), "%d.%m.%Y %H:%M:%S")
                    dt = timezone.localize(dt)
                    timestamp = time.mktime(dt.timetuple()) + dt.microsecond / 1e6
                if line_number > 6:
                    break
            rppg_data = np.array([[float(s) for s in line.split(';')] for line in rppg_file])
            t = rppg_data[:,0]
            bvp = rppg_data[:,1]
            resp = rppg_data[:,2]
            ret = {'begin':timestamp, 'time':t, 'bvp':bvp, 'resp':resp}
        return ret

    def __repr__(self):
        return "<RppgFile(path={})>".format(self.path)

class VideoFile(Base, File):
    """A class containing file related information of the BATL database.

    Attributes
    ----------
    path : str
        A relative path to the file.
    file_id : int
        A unique identifier of the file.
    client_id : int
        A unique identifier specifying the client.
    session_id : int
        Session identifier.
    presenter_id : int
        A unique identifier specifying the client presenting the PAI.
    type_id : int
        Identifier specifying the type of the attack.
    pai_id : int
        Identifier encoding the type of the PAI.
    """

    __tablename__ = 'video_file'

    id = Column(Integer, Sequence('VF_seq'), primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    path = Column(String(100), unique=True)
    session_id = Column(Integer)
    presenter_id = Column(Integer) # for SQLpresenter_id
    type_id = Column(Integer)
    pai_id = Column(Integer)
    # for python: a link to the file objects associated with this protcol
    rppgfile_id = Column(Integer, ForeignKey('rppg_file.id', ondelete='cascade'), nullable=True)
    rppgfile = relationship("RppgFile", backref=backref("video_file", uselist=False))

    def __init__(self, path, client_id, session_id, presenter_id, type_id, pai_id):

        super(VideoFile, self).__init__(path=path)
        self.path = path
        self.client_id = client_id
        self.session_id = session_id
        self.presenter_id = presenter_id
        self.type_id = type_id
        self.pai_id = pai_id

    def load(self, directory=None, extension='.h5', reference_stream_type='color',
             modality='all', warp_to_reference=False, convert_to_rgb=False,
             crop=None, max_frames=None):
        """
        Parameters
        ----------
        ``directory`` : :py:class:`str`
            If not empty or None, this directory is prefixed to the final
            file destination. Default: ``None``.
        ``extension`` : :py:class:`str`
            The extension of the file. Default for this database is
            '.h5'.
        ``reference_stream_type`` : :py:class:`str`
            Name of the reference stream (temporal and spatial alignment).
        ``modality`` : :py:class:`str`
            'all' for all modalities (default), otherwise the name of the modality or a list of
            modalities to consider. Modalities can be ['color', 'infrared', 'depth', 'thermal',
            'infrared_high_def', 'thermal_high_def']
        ``warp_to_color`` : :py:class:`bool`
            Warp the stream to the color stream. Default: ``False``.
        ``convert_to_rgb`` : :py:class:`bool`
            Convert the data to RGB format. Default: ``False``.
        ``crop`` : :py:class:`bool`
            A list with four parameters - startx = crop[0], starty = crop[1],
            width  = crop[2], height = crop[3]. If given, the video will be cropped.
            Default: ``None``.
        ``max_frames`` : :py:class:`bool`
            A maximum number of frames to load. If not given all frames will be
            loaded. Default: ``None``.

        Returns
        -------
        py:class:`dict`
            dictionary with a dictionary per modality containing the timestamps, the video and the
            masks
        """

        ## Hack for using two configurations based on date, later the markers should be made attributes in the HDF5 files


        date,month,year=self.path.split("/")[-2].split('.')

        month = int(month)
        date = int(date)


        if month<4:
            config_path = pkg_resources.resource_filename(__name__, 'config/default_data_config.json')
        elif month>4:
            config_path = pkg_resources.resource_filename(__name__, 'config/24_april_to_july.json')
        else:
            if date <= 17:
                config_path = pkg_resources.resource_filename(__name__, 'config/default_data_config.json')
            elif date >= 24:
                config_path = pkg_resources.resource_filename(__name__, 'config/24_april_to_july.json')
            else:
                config_path = pkg_resources.resource_filename(__name__, 'config/20_to_23_april_config.json')



        logger.debug("config_path: %s PATH: %s, %s, %s", config_path, self.path, date, month)

        ## rest is same

        config = load_data_config(config_path)
        filepath = self.make_path(directory, extension)
        ret = {}
        with HDF5File(filepath, 'r') as hdf5_file:
            if modality == 'all':
                modalities = list(config.keys())
                modalities.append('rppg')
            elif isinstance(modality, str):
                modalities = [modality]
            elif isinstance(modality, collections.iterable):
                modalities = list(modality)
            for mod in modalities:
                if mod == 'rppg':
                    ret[mod] = None if self.rppgfile is None else \
                               self.rppgfile.load(directory=directory)
                else:
                    video, timestamps, masks = \
                            load_video_stream_from_hdf5(hdf5_file, mod, reference_stream_type,
                                                        config,
                                                        warp_to_reference=warp_to_reference,
                                                        convert_to_rgb=convert_to_rgb, crop=crop,
                                                        max_frames=max_frames)
                    video = convert_arrays_to_frame_container(video)
                    ret[mod] = {'video':video,  'timestamps':timestamps,  'masks':masks}
            if len(modalities) == 1:
#                 ret = ret.values().pop()
                ret = ret[modality]
        return ret

    def is_attack(self):
        return self.type_id != 0

    def __repr__(self):
        return "<VideoFile(path={}, client_id={}, session_id={}, presenter_id={}, type={}, pai={})>"\
                .format(self.path, self.client_id, self.session_id, self.presenter_id,
                        BATL_CONFIG[self.type_id]['name'],
                        BATL_CONFIG[self.type_id]['pai'].get(self.pai_id, ''))


class Protocol(Base):
    __tablename__ = 'protocol'

    id = Column(Integer, Sequence('proto_seq'), primary_key=True)
    name = Column(String(20), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Protocol('%s')>" % (self.name)


class ProtocolPurpose(Base):
    """BATL protocol purposes"""
    __tablename__ = 'protocolPurpose'
    # Unique identifier for this protocol purpose object
    id = Column(Integer, Sequence('purpose_seq'), primary_key=True)
    # Id of the protocol associated with this protocol purpose object
    protocol_id = Column(Integer, ForeignKey('protocol.id')) # for SQL
    # Group associated with this protocol purpose object
    # Purpose associated with this protocol purpose object
    PURPOSES = ('real', 'attack')
    purpose = Column(Enum(*PURPOSES))
    GROUPS = ('train', 'validation', 'test')
    group = Column(Enum(*GROUPS))

    # For Python: A direct link to the Protocol object that this ProtocolPurpose belongs to
    protocol = relationship("Protocol", backref=backref("protocolpurpose", order_by=id))
    # For Python: A link to the File objects associated with this ProtcolPurpose
    files = relationship("VideoFile", secondary=protocolPurpose_file_association,
                          backref=backref("protocolPurpose", order_by=id))

    def __init__(self, group, purpose):
        self.group = group
        self.purpose = purpose

    def __repr__(self):
        return "ProtocolPurpose('%s', '%s', '%s')" % (self.protocol.name, self.group, self.purpose)
