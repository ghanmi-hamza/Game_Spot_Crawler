A crawler which extract data from a Gamespot user Profile:
data extracted:

*profile description:
{user_name,
 user_role,
 forum_posts,
 nb_followers,
nb_followings
 other_info
}
*posts:
{date
contenu
user_comments}
*comments:
{all user comments}

PS:to run this script go inside Crawler folder and then run this command : python __main__.py --url="A" --n=B 
where:
	A=url of the user
	B=number of forums pages to scrape


a folder "data" will be created and inside it you will find multiple folder named X(the name of the user) and inside each one you will
find images and json file contains data about the user X