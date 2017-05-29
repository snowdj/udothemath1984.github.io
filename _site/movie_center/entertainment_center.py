import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life!",
						"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

brothers = media.Movie("Brothers",
						"The consequences of brothers' actions threaten the foundation of the entire family.",
						"http://lh3.ggpht.com/_rsdqufw36s8/TCDYRrDqePI/AAAAAAAAB0M/5NsnyZfPkQE/s350/Entre+hermanos+poster.JPG",
						"https://www.youtube.com/watch?v=9bWw1VP2iMY")

inception = media.Movie("Inception",
						"A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
						"http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
						"https://www.youtube.com/watch?v=E1iqGiX0lSg")

life_of_pi = media.Movie("Life Of Pi",
						"'Life Of Pi' tells the story of a young man's incredible survival at sea against impossible odds.",
						"http://www.impawards.com/2012/posters/life_of_pi.jpg",
						"https://www.youtube.com/watch?v=j9Hjrs6WQ8M")

up = media.Movie("Up",
						"'a comedy adventure in which 78-year-old Carl Fredricksen fulfills his dream of a great adventure when he ties thousands of balloons to his house and flies away to the wilds of South America, only to discover that he has brought with him his biggest nightmare, a 9-year-old Wilderness Explorer stowaway.",
						"https://vignette3.wikia.nocookie.net/disney/images/a/a6/Up_Poster_Run.jpg/revision/latest?cb=20160202180816",
						"https://www.youtube.com/watch?v=ORFWdXl_zJ4")

the_departed = media.Movie("The Departed",
						"An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
						"https://fanart.tv/fanart/movies/1422/movieposter/the-departed-52f9631087322.jpg",
						"https://www.youtube.com/watch?v=auYbpnEwBBg")



#print toy_story.storyline
#toy_story.show_trailer()
#print brothers.storyline
#brothers.show_trailer()


movie_list = [toy_story, brothers, inception, life_of_pi, up, the_departed]
fresh_tomatoes.open_movies_page(movie_list)

print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)