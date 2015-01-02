class level(object):
    """Level data type 
       """
    __slots__ = ['height', 'tileheight', 'tilesets', 'tilewidth', 'width', 'data']    

    def __init__(self, json_data):
        self.height = json_data['height']
        self.tileheight = json_data['tileheight']
        self.tilesets = json_data['tilesets']
        self.tilewidth = json_data['tilewidth']
        self.width = json_data['width']
        self.data = json_data['layers'][0]['data']
