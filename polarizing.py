import math

def get_movie_name(movie_filename):
      movie = dict()
      with movie_filename as infile:
            header = infile.readline()
            for line in infile:
                  fields = line.removesuffix("\n").split("\t")
                  movie_id = int(fields[0])
                  movie_name = fields[1]
                  movie[movie_id] = movie_name
      return movie

def get_ratings(ratings_filename):
      ratings = dict()
      with ratings_filename as infile:
            header = infile.readline()
            for line in infile:
                  fields = line.removesuffix("\n").split("\t")
                  movie_id = int(fields[1])
                  rating = float(fields[2])
                  if movie_id not in ratings:
                        ratings[movie_id] = []
                  ratings[movie_id].append(rating)
      return ratings
def population_std_dev(values):
      total = 0.0
      for value in values:
            total = total + value
      average = total / len(values)
      sum_squares = 0.0
      for value in values:
            sum_squares = sum_squares + (value - average)**2
      return math.sqrt(sum_squares/len(values))

def main():
      movie_filename = "movies.tsv"
      ratings_filename = "ratings.tsv"
      min_ratings = 100

      titles = get_movie_name(movie_filename)
      ratings = get_ratings(ratings_filename)
      best_id = None
      best_spread = -1.0
      for movie_id in ratings:
            if len(ratings[movie_id]) >=min_ratings:
                  spread = population_std_dev(ratings[movie_id])
                  if spread > best_spread:
                        best_id = movie_id
                        best_spread = spread
      print(f"The most polarizing movie is {titles[best_id]} with a standard deviation of {best_spread}")


if __name__ == "__main__":
      main()
