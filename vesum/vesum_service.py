from pymongo import MongoClient
from flask import current_app
import os
import logging
logger = logging.getLogger(__name__)

MONGO_URL = ('VESUM_MONGO_DB_URL' in os.environ and os.environ['VESUM_MONGO_DB_URL']) or 'localhost:27017'
DB_NAME = ('VESUM_DB_NAME' in os.environ and os.environ['VESUM_DB_NAME']) or'natasha-uk-database'
BUFFER_LIMIT = 10000
client = MongoClient(MONGO_URL, maxPoolSize=20)


class VesumService:
    def find_by_word_form(self, word_form):
        return client[DB_NAME]['vesum-entry'].find({'word': word_form})

    def init_vesum(self):
        if self.find_by_word_form('ящурні').count() > 0:
            return
        records_saved = 0
        buffer = []
        with open(os.path.dirname(os.path.abspath(__file__)) + '/dict_corp_lt.txt', encoding="utf8") as fp:
            for cnt, line in enumerate(fp):
                buffer.append(line)
                if len(buffer) == BUFFER_LIMIT:
                    save_vesum_lines(buffer)
                    records_saved += len(buffer)
                    logger.warning('lines processed: ' + str(records_saved))
                    buffer.clear()

        if len(buffer) > 0:
            save_vesum_lines(buffer)
            records_saved += len(buffer)
            logger.warning('lines processed: ' + str(records_saved))
        client[DB_NAME]['vesum-entry'].ensure_index('word')


def save_vesum_lines(lines):
    vesum_entries = list(map(lambda line: parse_vesum_line(line), lines))
    client[DB_NAME]['vesum-entry'].insert_many(vesum_entries)


def parse_vesum_line(line):
    line = line.strip()
    vesum_entry_arr = line.split(' ')
    return {
        'word': vesum_entry_arr[0],
        'mainForm': vesum_entry_arr[1],
        'tags': vesum_entry_arr[2].split(':')
    }


vesum_service = VesumService()
