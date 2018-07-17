__author__ = 'leamox'

import os
from pymongo import MongoClient
from utils.StringUtils import *


def insert(path):
    if os.path.exists(path):
        mongo_client = MongoClient("127.0.0.1", 27017)
        mo = mongo_client["celloud"]["BSIEnvSpecies"]
        mo.remove()
        f = open(path, "r")
        env_names = []
        for line in f.readlines():
            env_names.append(line.strip())
        env_species = {"names": env_names}
        mo.insert_one(env_species)

if __name__ == '__main__':
	insert("bsi_env_species.txt")


