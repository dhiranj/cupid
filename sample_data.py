from models import Song, User

def get_sample_songs():
    return [
        Song(name="Song1", genre="Pop", tempo="Medium", singer="Singer1", popularity_score=85.5, release_year=2020),
        Song(name="Song2", genre="Rock", tempo="Fast", singer="Singer2", popularity_score=90.0, release_year=2019),
        Song(name="Song3", genre="Jazz", tempo="Slow", singer="Singer3", popularity_score=75.0, release_year=2018),
        Song(name="Song4", genre="Classical", tempo="Slow", singer="Singer4", popularity_score=80.0, release_year=2017),
        Song(name="Song5", genre="Pop", tempo="Medium", singer="Singer5", popularity_score=95.0, release_year=2021),
        Song(name="Song6", genre="Pop", tempo="Medium", singer="Singer6", popularity_score=70.0, release_year=2020),
        Song(name="Song7", genre="Rock", tempo="Fast", singer="Singer7", popularity_score=80.0, release_year=2019),
        Song(name="Song8", genre="Jazz", tempo="Slow", singer="Singer8", popularity_score=78.0, release_year=2018),
        Song(name="Song9", genre="Classical", tempo="Slow", singer="Singer9", popularity_score=82.0, release_year=2017),
        Song(name="Song10", genre="Pop", tempo="Medium", singer="Singer10", popularity_score=94.0, release_year=2021),
        Song(name="Song11", genre="Rock", tempo="Fast", singer="Singer10", popularity_score=85.0, release_year=2016),
        Song(name="Song12", genre="Jazz", tempo="Slow", singer="Singer8", popularity_score=77.0, release_year=2015),
        Song(name="Song13", genre="Classical", tempo="Slow", singer="Singer9", popularity_score=79.0, release_year=2014),
        Song(name="Song14", genre="Pop", tempo="Medium", singer="Singer14", popularity_score=92.0, release_year=2013),
        Song(name="Song15", genre="Rock", tempo="Fast", singer="Singer15", popularity_score=87.0, release_year=2012),
        Song(name="Song16", genre="Jazz", tempo="Slow", singer="Singer2", popularity_score=76.0, release_year=2010),
        Song(name="Song17", genre="Classical", tempo="Slow", singer="Singer17", popularity_score=81.0, release_year=2010),
        Song(name="Song18", genre="Pop", tempo="Medium", singer="Singer3", popularity_score=92.0, release_year=2009),
        Song(name="Song19", genre="Rock", tempo="Fast", singer="Singer5", popularity_score=86.0, release_year=2009),
        Song(name="Song20", genre="Jazz", tempo="Slow", singer="Singer20", popularity_score=78.0, release_year=2017),
    ]
 

def get_sample_users():
    return [
        User(name="User1", playlist=["Song1", "Song2"], friends=[]),
        User(name="User2", playlist=["Song3", "Song4"], friends=[]),
        User(name="User3", playlist=["Song1", "Song5"], friends=[]),
        User(name="User4", playlist=["Song6", "Song7"], friends=[]),
        User(name="User5", playlist=["Song8", "Song9"], friends=[]),
        User(name="User6", playlist=["Song10", "Song11"], friends=[]),
        User(name="User7", playlist=["Song12", "Song13"], friends=[]),
        User(name="User8", playlist=["Song14", "Song15"], friends=[]),
        User(name="User9", playlist=["Song16", "Song17"], friends=[]),
        User(name="User10", playlist=["Song18", "Song19"], friends=[]),
        User(name="User11", playlist=["Song20", "Song1"], friends=[]),
        User(name="User12", playlist=["Song2", "Song3"], friends=[]),
        User(name="User13", playlist=["Song4", "Song5"], friends=[]),
        User(name="User14", playlist=["Song6", "Song7"], friends=[]),
        User(name="User15", playlist=["Song8", "Song9"], friends=[]),
        User(name="User16", playlist=["Song10", "Song11"], friends=[]),
        User(name="User17", playlist=["Song12", "Song13"], friends=[]),
        User(name="User18", playlist=["Song14", "Song15"], friends=[]),
        User(name="User19", playlist=["Song16", "Song17"], friends=[]),
        User(name="User20", playlist=["Song18", "Song19"], friends=[]),
    ]

def make_sample_friends():
    return [
        {"user1": ["user2", "user3", "user4"]},
        {"user2": ["user1", "user5", "user6"]},
        {"user3": ["user1", "user7", "user8"]},
        {"user4": ["user1", "user9", "user10"]},
        {"user5": ["user2", "user11", "user12"]},
        {"user6": ["user2", "user13", "user14"]},
        {"user7": ["user3", "user15", "user16"]},
        {"user8": ["user3", "user17", "user18"]},
        {"user9": ["user4", "user19", "user20"]},
        {"user10": ["user4", "user1", "user2"]},
        {"user11": ["user5", "user3", "user4"]},
        {"user12": ["user5", "user6", "user7"]},
        {"user13": ["user6", "user8", "user9"]},
        {"user14": ["user6", "user10", "user11"]},
        {"user15": ["user7", "user12", "user13"]},
        {"user16": ["user7", "user14", "user15"]},
        {"user17": ["user8", "user16", "user20"]},
        {"user18": ["user8", "user10", "user19"]},
        {"user19": ["user9", "user20", "user1"]},
        {"user20": ["user9", "user2", "user3"]},
    ]