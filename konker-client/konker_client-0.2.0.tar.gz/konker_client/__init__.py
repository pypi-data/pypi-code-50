# -*- coding: utf-8 -*-

"""Top-level package for Konker Client."""

__author__ = """Gustavo Esteves de Andrade"""
__email__ = 'gandrade@inmetrics.com.br'
__version__ = '0.2.0'

from konker_client.system import System
from konker_client.mqtt import Mqtt
from konker_client.request import Request
import time
import os
import logging
import logging.config
import json
import datetime


FOLDER_LOCATION = os.path.dirname(os.path.abspath(__file__))
FOLDER_LOCATION_LOGS = FOLDER_LOCATION


class KonkerClient():

    __client = None
    device = None
    client_name = None
    service_type = None

    def __init__(self, mode: str, device: str, user: str, password: str, client_name: str, service_type: str):
        self.setup_logging()
        self._logger = logging.getLogger(__name__)

        if mode == 'MQTT':
            self.__client = Mqtt(user, password)
        elif mode == 'REQUEST':
            self.__client = Request(user, password)
        else:
            raise Exception(f"{mode} NOT IMPLEMENTED")

        self.device = device
        self.client_name = client_name
        self.service_type = service_type

    def setup_logging(self, default_path=os.path.join(FOLDER_LOCATION_LOGS, 'logging.json'), default_level=logging.INFO, env_key='LOG_CFG'):
        """
        Função que executa a configuração de logs do Spiderling
        """
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
                for key, handler in config['handlers'].items():
                    if 'filename' in handler:
                        try:
                            os.mkdir('logs')
                        except OSError:
                            pass
                        handler['filename'] = os.path.join('logs', handler['filename'])

            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

    def __send_message(self, channel: str, message: dict):
        return self.__client.send_message(channel, message)

    def send_business_log_rpa(self, robot_name: str, business_description: str, value: int, business_datetime: str) -> bool:
        message = {
            "LOG_TYPE": "BUSINESS",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "DATA": {
                "ROBOT_NAME": robot_name,
                "BUSINESS_DESCRIPTION": business_description,
                "VALUE": value,
                "BUSINESS_DATETIME": business_datetime
            }
        }

        return self.__send_message('log', message)

    def send_business_log_qts_caso_teste(self, ct_data: dict) -> bool:
        message = {
            "LOG_TYPE": "BUSINESS",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "ENTITY_NAME": "CASO_TESTE",
            "DATA": {
                "ID": ct_data.get('id'),
                "NOME": ct_data.get('nome'),
                "FUNCIONALIDADE": ct_data.get('funcionalidade'),
                "DESCRICAO": ct_data.get('descricao'),
                "PRIORIDADE": ct_data.get('prioridade'),
                "CRITICIDADE": ct_data.get('criticidade'),
                "STATUS": ct_data.get('status'),
                "RESPONSAVEL": ct_data.get('responsavel'),
            }
        }

        return self.__send_message('log', message)

    def send_business_log_qts_projeto(self, data: dict) -> bool:
        message = {
            "LOG_TYPE": "BUSINESS",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "ENTITY_NAME": "PROJETO",
            "DATA": {
                "ID": data.get('id'),
                "NOME": data.get('nome'),
            }
        }

        return self.__send_message('log', message)

    def send_business_log_qts_sprint(self, data: dict) -> bool:
        message = {
            "LOG_TYPE": "BUSINESS",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "ENTITY_NAME": "SPRINT",
            "DATA": {
                "ID": data.get('id'),
                "NOME": data.get('nome'),
                "DATA_INICIAL": data.get('data_inicial'),
                "DATA_FIM": data.get('data_fim')
            }
        }

        return self.__send_message('log', message)

    def send_business_log_qts_caso_teste_execucao(self, data: dict) -> bool:
        message = {
            "LOG_TYPE": "BUSINESS",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "ENTITY_NAME": "CASO_TESTE_EXECUCAO",
            "DATA": {
                "ID": data.get('id'),
                "STATUS": data.get('status'),
                "DATA": data.get('data'),
                "DURACAO": data.get('duracao'),
                "RESPONSAVEL": data.get('responsavel'),
                "ID_CT": data.get('id_ct'),
                "ID_SPRINT": data.get('id_sprint'),
            }
        }

        return self.__send_message('log', message)

    def send_business_log_qts_defeito(self, data: dict) -> bool:
        message = {
            "LOG_TYPE": "BUSINESS",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "ENTITY_NAME": "DEFEITO",
            "DATA": {
                "ID": data.get('id'),
                "STATUS": data.get('status'),
                "DATA": data.get('data'),
                "CRIADO_POR": data.get('criado_por'),
                "FABRICA_DESENVOLVIMENTO_RESPONSAVEL": data.get('fabrica_desenvolvimento_responsavel'),
            }
        }

        return self.__send_message('log', message)

    def send_business_log_caso_teste_defeito(self, data: dict) -> bool:
        message = {
            "LOG_TYPE": "BUSINESS",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "ENTITY_NAME": "CASO_TESTE_DEFEITO",
            "DATA": {
                "ID_CT": data.get('id_ct'),
                "ID_DEF": data.get('id_def'),
            }
        }

        return self.__send_message('log', message)

    def send_execution_log(self, operation: str, execution_id: int, status: bool, execution_message: str, duration: int) -> bool:
        status = "Sucess" if status else "Failed"
        message = {
            "LOG_TYPE": "EXECUTION",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "OPERATION": operation,
            "EXECUTION_ID": execution_id,
            "STATUS": status,
            "MESSAGE": execution_message,
            "DURATION": duration
        }

        return self.__send_message('log', message)

    def send_health_log(self) -> bool:
        system = System()
        system.get_health()
        message = {
            "LOG_TYPE": "HEALTH",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "KONKER_ID": self.device,
            "HEALTH": 1,
            "HOST": {
                "NAME": system.hostname,
                "IP": system.ip,
                "MEMORY": {
                    "PERC": system.host_memory_perc,
                    "USED": system.host_memory_used
                },
                "SWAP": {
                    "PERC": system.host_swap_perc,
                    "USED": system.host_swap_used
                },
                "CPU": system.host_cpu,
                "DISKS": system.host_disks
            },
            "PROCESS": {
                "MEMORY": {
                    "PERC": system.process_memory_perc,
                    "USED": system.process_memory_used,
                },
                "SWAP": {
                    "PERC": system.process_swap_perc,
                    "USED": system.process_swap_used,
                },
                "CPU": system.process_cpu,
            }
        }

        return self.__send_message('health', message)

    def send_acknowledge_log(self, operation: str, execution_id: int) -> bool:
        message = {
            "LOG_TYPE": "ACK",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "OPERATION": operation,
            "EXECUTION_ID": execution_id,
        }

        return self.__send_message('ack', message)

    def send_report_log(self, execution_id: int, report_message: str) -> bool:
        message = {
            "LOG_TYPE": "REPORT",
            "CLIENT_NAME": self.client_name,
            "SERVICE_TYPE": self.service_type,
            "EXECUTION_ID": execution_id,
            "REPORT_MESSAGE": report_message
        }

        return self.__send_message('report', message)
