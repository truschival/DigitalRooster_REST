#!/usr/bin/python

from DigitalRooster import Configuration
from restutil import read_slice 

def read_all(**kwargs):
    cfg = Configuration.Configuration('./digitalrooster.json');
    return read_slice(cfg.get_podcasts(),kwargs)    

def read_one(uid):
    cfg = Configuration.Configuration('./digitalrooster.json');
    return cfg.get_podcast_by_uid(uid), 200

def create(**kwargs):
    podcast = kwargs['body']
    cfg = Configuration.Configuration('./digitalrooster.json');
    if 'UpdateInterval' in podcast:
        period =  podcast['UpdateInterval']
    else:
        period = None
        
    try:
        cfg.podcast_append(url = podcast['url'] , 
                         name =podcast['name'],
                         update_interval = period)
    except ValueError:
        return 404

    try:
        cfg.write()
    except Exception:
        return 500

    return 200


def update_one(uid, **kwargs):
    podcast = kwargs['body']
    cfg = Configuration.Configuration('./digitalrooster.json');
    try:
        cfg.podcast_update(uid = uid, 
                         url = podcast['url'] , 
                         name =podcast['name'],
                         update_interval = podcast['UpdateInterval'])
    except ValueError:
        return "Bad format", 404
    except IndexError:
        return "Item not found", 404

    try:
        cfg.write()
    except Exception:
        return "Write failed", 500

    return read_one(uid)
    
def delete(uid):
    cfg = Configuration.Configuration('./digitalrooster.json');
    try:
        cfg.podcast_delete(uid)
    except ValueError:
        return "Bad format for uid", 404
    except IndexError:
        return "Item not found", 404

    try:
        cfg.write()
    except Exception:
        return "Write failed", 500
    
    return "Item deleted", 200