ids = {
        'Sarbjit Singh':'1500535',
        'Nimit Bhardwaj':'1500506',
        'Sourav Sahoo':'1500502',
        'Vishal Choudhary':'1500511',
        'Mukund Aggarwal':'15558',
        'Unknown':'0'
}

ids_ = {
        'srb':'1500535',
        'nimi':'1500506',
        'sahoo':'1500502',
        'vishi':'1500511',
        'shuchund':'15558',
        'unknown':'0'
}


class Doubly_map():
    def __init__(self,mapp):
        self.lmap = {}
        self.rmap = {}
        for key in mapp.keys():
            self.lmap[key] = mapp[key]
            self.rmap[mapp[key]] = key

doubly_map = Doubly_map(ids_)

def temp_id_gen(user_name):
    if(user_name in doubly_map.lmap):
        return int(doubly_map.lmap[user_name])
    else:
        return 0

def temp_name_gen(user_id):
    if(user_id in doubly_map.rmap):
        return doubly_map.rmap[user_id]
    else:
        return 'unknown'

