
def main():
      movies_filename = "movies.tsv"
      genre_counts = count_genres(movies_filename)
      for genre in genre_counts:
           print(genre, genre_counts[genre])

def count_genres(movies_filename):
     genre_counts = dict()
     with open(movies_filename) as infile:
          header = infile.readline()
          for line in infile:
               fields = line.removesuffix("\n").split("\t")
               genres = fields[2].split("|")
               for genre in genres:
                    if genre not in genre_counts:
                         genre_counts[genre] = 0
                    genre_counts[genre] = genre_counts[genre]+1
     return genre_counts                 



if __name__ == "__main__":
    main()