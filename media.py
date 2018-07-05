# The Movie class creates movie object's that contain
# movie's title, storyline, poster image and trailer.


class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        # string movie_title contains title of the movie
        self.title = movie_title

        # string movie_storyline contains storyline of the movie
        self.storyline = movie_storyline

        # string poster_image contains url link of the movie poster
        self.poster_image_url = poster_image

        # string trailer_youtube contains youtube url link of the movie trailer
        self.trailer_youtube_url = trailer_youtube
