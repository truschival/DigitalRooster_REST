import json
import uuid
import validators
from pprint import pprint

class Configuration(object):
    def __init__(self, config_file = './digitalrooster.json'):
        '''
        Constructor
        '''
        self.filename = config_file
        
        with open(config_file) as f:
            self.data = json.load(f)
            pprint(self.data)

    def write(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, 
                      sort_keys = True, 
                      indent = 4, 
                      ensure_ascii=False);

    def get_index_for_uid(self, lst, uid):
        index = [i for i in [0, len(lst) - 1] if uuid.UUID(lst[i]['id']) == uuid.UUID(uid)]
        return index[0]

    def get_braced_uid(self):
        return "{"+ uuid.uuid1().__str__() +"}"

########
# Iradio
########
    def iradio_append(self, url, name):
        newStream ={}
        newStream['url'] = url
        newStream['name'] = name
        newStream['id'] = self.get_braced_uid()
        self.data['InternetRadio'].append(newStream)
        return newStream['id']

    def get_iradio_stream_by_uid(self, uid):
        index = self.get_index_for_uid(self.data['InternetRadio'], uid)  
        return self.data['InternetRadio'][index]

    def get_iradio_streams(self):
        return self.data['InternetRadio']

    def iradio_delete(self,uid):
        index = self.get_index_for_uid(self.data['InternetRadio'], uid)
        del self.data['InternetRadio'][index]

    def iradio_update(self,uid, url, name):
        index = self.get_index_for_uid(self.data['InternetRadio'], uid)
        if not name or not url or not validators.url(url):
            raise ValueError
        
        self.data['InternetRadio'][index]['url'] = url
        self.data['InternetRadio'][index]['name'] = name
########
# Alarms
########
    def alarm_append(self, url, period, time):
        newAlarm ={}
        newAlarm['url'] = url
        newAlarm['period'] = period
        newAlarm['time'] = time
        newAlarm['id'] = self.get_braced_uid()
        self.data['Alarms'].append(newAlarm)
        return newAlarm['id']

    def get_alarm_by_uid(self, uid):
        index = self.get_index_for_uid(self.data['Alarms'], uid)  
        return self.data['Alarms'][index]

    def get_alarms(self):
        return self.data['Alarms']

    def alarm_delete(self,uid):
        index = self.get_index_for_uid(self.data['Alarms'], uid)
        del self.data['Alarms'][index]

    def alarm_update(self,uid, url, period, time, enabled):
        index = self.get_index_for_uid(self.data['Alarms'], uid)
        if not url or not validators.url(url):
            raise ValueError
        
        self.data['Alarms'][index]['url'] = url
        self.data['Alarms'][index]['period'] = period
        self.data['Alarms'][index]['time'] = time
        self.data['Alarms'][index]['enabled'] = enabled

########
# Podcasts
########
    def podcast_append(self, url, name, update_interval = 3600):
        podcast ={}
        podcast['url'] = url
        podcast['name'] = name
        podcast['UpdateInterval'] = update_interval
        podcast['id'] = self.get_braced_uid()
        self.data['Podcasts'].append(podcast)
        return podcast['id']

    def get_podcast_by_uid(self, uid):
        index = self.get_index_for_uid(self.data['Podcasts'], uid)  
        return self.data['Podcasts'][index]

    def get_podcasts(self):
        return self.data['Podcasts']

    def podcast_delete(self,uid):
        index = self.get_index_for_uid(self.data['Podcasts'], uid)
        del self.data['Podcasts'][index]

    def podcast_update(self,uid, url, name, update_interval = 3600):
        index = self.get_index_for_uid(self.data['Podcasts'], uid)
        if not url or not validators.url(url):
            raise ValueError
        
        self.data['Podcasts'][index]['url'] = url
        self.data['Podcasts'][index]['name'] = name
        self.data['Podcasts'][index]['UpdateInterval'] = update_interval
      

