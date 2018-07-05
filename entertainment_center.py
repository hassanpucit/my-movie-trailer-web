import media
import movies_store

gladiator = media.Movie("Gladiator",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipe"
                        "dia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=AxQajgTyLcM")

lord_of_the_ring = media.Movie("Lord of the Ring",
                               "A story of HungerGame.",
                               "https://upload.wikimedia.org/wikipe"
                               "dia/en/a/ad/Lord_of_the_Ri"
                               "ngs_-_The_Two_Towers.jpg",
                               "https://www.youtube.com/watch?v=cvCktPUwkW0")

dark_knight = media.Movie("Dark Knight",
                          "Going back in time to meet authors",
                          "https://upload.wikimedia.org/wikipe"
                          "dia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=kmJLuwP3MbY")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/To"
                        "y_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marien on an alian planet.",
                     "http://upload.wikimedia.org/wikipe"
                     "dia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

ratatouille = media.Movie("Ratatouille",
                          "A story of rat in a chef",
                          "http://upload.wikimedia.org/wikipe"
                          "dia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

school_of_rock = media.Movie("School of Rock",
                             "A story of a boy and his toys that come to life",
                             "http://upload.wikimedia.org/wikipe"
                             "dia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

hunger_games = media.Movie("Hunger Game",
                           "A story of Hunger Game.",
                           "https://upload.wikimedia.org/wikipe"
                           "dia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

training_day = media.Movie("Training Day",
                           "Going back in time to meet authors",
                           "https://upload.wikimedia.org/wikipe"
                           "dia/en/b/b3/Training_Day_Poster.jpg",
                           "https://www.youtube.com/watch?v=DXPJqRtkDP0")

movies = [dark_knight, lord_of_the_ring, gladiator, toy_story,
          school_of_rock, ratatouille, avatar, hunger_games, training_day]
movies_store.open_movies_page(movies)
