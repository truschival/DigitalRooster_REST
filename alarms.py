#!/usr/bin/python

from DigitalRooster import Configuration
from restutil import read_slice 

def read_all(**kwargs):
    cfg = Configuration.Configuration('./digitalrooster.json');
    return read_slice(cfg.get_alarms(),kwargs)    

def read_one(uid):
    cfg = Configuration.Configuration('./digitalrooster.json');
    return cfg.get_alarm_by_uid(uid), 200

def create(**kwargs):
    stream_info = kwargs['body']
    cfg = Configuration.Configuration('./digitalrooster.json');
    try:
        cfg.alarm_append(url = stream_info['url'] , 
                         period =stream_info['period'],
                         time = stream_info['time'])
    except ValueError:
        return 404

    try:
        cfg.write()
    except Exception:
        return  500

    return 200


def update_one(uid, **kwargs):
    stream_info = kwargs['body']
    cfg = Configuration.Configuration('./digitalrooster.json');
    try:
        cfg.alarm_update(uid = uid, 
                         url = stream_info['url'] , 
                         period =stream_info['period'],
                         time = stream_info['time'])
    except ValueError:
        return  404
    except IndexError:
        return  404

    try:
        cfg.write()
    except Exception:
        return 500

    return read_one(uid)
    
def delete(uid):
    cfg = Configuration.Configuration('./digitalrooster.json');
    try:
        cfg.alarm_delete(uid)
    except ValueError:
        return  404
    except IndexError:
        return 404

    try:
        cfg.write()
    except Exception:
        return 500
    
    return 200
