import logging
from fuckeverything import utils
from fuckeverything import event
from fuckeverything import heartbeat

_clients = []


@utils.gevent_func
def handle_client(identity=None, msg=None):
    _clients.append(identity)
    heartbeat.start(identity)


def is_client(identity):
    # TODO: Implement
    return False