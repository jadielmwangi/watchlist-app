class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=4b5875e5fc8e9e3c5c43dc4be409b591 '

    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

class Config:
    '''
    General configuration parent class
    '''
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=4b5875e5fc8e9e3c5c43dc4be409b591'