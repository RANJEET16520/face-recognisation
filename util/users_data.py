import os
import json

from abs_path import abs_path
from lib.files import verify_file
from util.constants.string_constants import users_data


def write_file(file_name, data):
    jfile = open(file_name, 'w')
    json.dump(data,jfile,indent = 4,ensure_ascii = False)
    jfile.close()


def read_file(file_name):
    jfile = open(file_name)
    data = json.load(jfile)
    jfile.close()
    return data


def create_file(file_name):
    template =                                      \
    {                                               \
        "user_ids":{                                \
            "0":{                                   \
                "user_name":"Unknown",              \
                "first_name":"Unknown",             \
                "last_name":"Unknown",              \
                "password":"hell"                   \
            }                                       \
        },                                          \
        "user_names":{                              \
            "Unknown":"0"                           \
        }                                           \
    }
    write_file(file_name, template)


def extract_data():
    fille = abs_path(users_data)
    verify_file(fille)
    data = read_file(fille)
    if(not 'user_ids' in data.keys()):
        create_file(fille)
        data = read_file(fille)
    return data


def user_ids_edit():
    data = extract_data()
    user_ids = data['user_ids']

    mapp = print_indexed(paths)
    print("enter index number of user : ",end='')
    index = int(input())

    if(index <= 0 or index >= len(mapp)):
        print("invalid index")
        return
    else:
        print('yet to be implemeted')


def get_first_vacant_id():
    data = extract_data()
    user_ids = data['user_ids']
    ids = [int(key) for key in user_ids.keys() ]
    ids = sorted(ids)
    expected = 0
    for idd in ids:
        if(idd != expected):
            break
        expected += 1
    return str(expected)


def add_user(user_name):
    vac_id = get_first_vacant_id()
    data = extract_data()
    data['user_names'][user_name] = vac_id
    dummy_user = User(user_name)
    data['user_ids'][vac_id] = dummy_user.get_data()
    write_file(users_data, data)


def get_user_name(user_id):
    data = extract_data()
    user_ids = data['user_ids']
    user_id = str(user_id)

    if(user_id in user_ids):
        return user_ids[user_id]['name']
    else:
        return 'Unknown'


def get_user_id(user_name):
    data = extract_data()
    user_names = data['user_names']
    user_name = str(user_name)

    if(user_name in user_names):
        return user_names[user_name]
    else:
        return '0'


def print_indexed(mapp):
    dictt = [""]
    i = 1
    for key,value in mapp.items():
        print(Colour.CYAN,i,":",Colour.GREEN,key,Colour.END,":",value['user_name'])
        dictt.append(value['user_name'])
        i+=1
    return dictt


