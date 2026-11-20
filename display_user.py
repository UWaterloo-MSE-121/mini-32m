
MOVIE_ID = 0
TITLE = 1
GENRES = 2

class Movie:
    """"This class stores a movie's id, title, and genres."""
    def __init__(self, id, title, genres):
        

def get_movie_table(movie_tsv_filename):
    movie_table = dict()
    with open(movie_tsv_filename) as infile:
    header = infile.readline()
    for line in infile:
        fields = line.removesuffix("\n").split("\t")
        assert len(fields) == 3
        movie = Movie()
        movie.id = int(fields[0])
        movie.title = fields[1]
        movie.genres = fields[2]
        movie_table[movie.id] = movie
    return get_movie_table

def get_movie_title(desired_movie_id, movie_table):
    movie = movie_table[desired_movie_id]
    movie_title = movie.title
    return movie_title


def main():
    movie_ids, movie_titles, movie_genres = get_movie_table("movies.tsv")
    desired_user_id = 81287
    ratings_file = open("ratings.tsv")
    header = ratings_file.readline()
    for line in ratings_file:
        row = line.removesuffix("\n").split("\t")
        assert len(row) == 4
        user_id = int(row[0])
        movie_id = int(row[1])
        rating = float(row[2])
        if user_id == desired_user_id:
            movie_title = get_movie_title(movie_id, movie_table)
            assert movie_table
            print(f"user_id = {user_id}, movie_id = {movie_id}, title = {movie_title}, rating = {rating}")
    ratings_file.close()


if __name__ == "__main__":
    main()