import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life!",
						"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

brothers = media.Movie("Brothers",
						"The consequences of brothers' actions threaten the foundation of the entire family",
						"http://lh3.ggpht.com/_rsdqufw36s8/TCDYRrDqePI/AAAAAAAAB0M/5NsnyZfPkQE/s350/Entre+hermanos+poster.JPG",
						"https://www.youtube.com/watch?v=9bWw1VP2iMY")

inception = media.Movie("Inception",
						"A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
						"http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
						"https://www.youtube.com/watch?v=E1iqGiX0lSg")

#print toy_story.storyline
#toy_story.show_trailer()
#print brothers.storyline
#brothers.show_trailer()


#movie_list = [toy_story, brothers, inception]
#fresh_tomatoes.open_movies_page(movie_list)

print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__