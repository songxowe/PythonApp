import nester

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']

# 命名空间限定函数名
nester.print_lol(cast)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
nester.print_lol(movies, True, 0)
