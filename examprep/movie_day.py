# Input
movie_time = int(input())
scenes_count = int(input())
scene_duration = int(input())

# Logics
preparation = movie_time * 0.15
all_scenes_time = scenes_count * scene_duration
all_time = preparation + all_scenes_time

# Print output
if movie_time >= all_time:
    print(f'You managed to finish the movie on time! You have {round(movie_time - all_time)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(all_time - movie_time)} minutes.')
