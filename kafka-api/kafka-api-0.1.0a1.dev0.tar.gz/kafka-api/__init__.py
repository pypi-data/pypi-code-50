from kafka import KafkaProducer


def kafka_producer(cfg=None):
    """
        Создание продюсера - пока все подефолту
        TODO нужно научить работать с конфигурацией как в Spring
        """
    if not cfg:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    else:
        # TODO если передана конфигурация то ее подменить
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    return producer


def send_result_to(topic_name: str):
    """
    Декоратор для отправки результатов работы функции в топик
    :param topic_name: наименование топика
    :return: результат работы функции который будет отправлен в топик
    """
    producer = kafka_producer()

    def result_send_to(fun):
        def wrapper(*args, **kwargs):
            result = fun(*args, **kwargs)
            b_result = bytes(str(result), 'utf-8')
            producer.send(topic_name, b_result)
            producer.flush()
            return result

        return wrapper

    return result_send_to
