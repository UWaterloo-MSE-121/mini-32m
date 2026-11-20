def main():
      movie_filename = "movies.tsv"
      ratings_filename = "ratings.tsv"
      min_ratings = 100
      min_average = 4.0

      titles = get_titles(movie_filename)
      sums, counts = get_sums_and_counts(ratings_filename)
      for movie_id in sums:
            if counts[movie_id]>=min_ratings:
                  average = sums[movie_id]/counts[movie_id]
                  if average >=min_average:
                        print(f"{average:.2f} {titles[movie_id]}")


      
def get_titles(movie_filename):
      titles = dict()
      with open(movie_filename) as infile:
            header = infile.readline()
            for line in infile:
                  fields = line.removesuffix("\n").split("\t")
                  movie_id = int(fields[0])
                  titles[movie_id] = fields[1]
      return titles

def get_sums_and_counts(ratings_filename):
      sums = dict()
      counts = dict()
      with open(ratings_filename) as infile:
            header = infile.readline()
            for line in infile:
                  fields = line.removesuffix("\n").split("\t")
                  movie_id = int(fields[1])
                  rating = float(fields[2])
                  if movie_id not in sums:
                        sums[movie_id] = 0.0
                        counts[movie_id] = 0
                  sums[movie_id] = sums[movie_id] + rating
                  counts[movie_id] = counts[movie_id] + 1
      return sums, counts


if __name__ == "__main__":
      main()