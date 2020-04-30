# Swapi_favorites
Vist site at: https://djangoswapi.herokuapp.com/

This project is a site users can visit to see the top favorites of Films, Characters, Starships, etc from the Star Wars Films.

The user can search and browse through all of this information and allows the user to click on related items to see their
information. Users can favorite things they are looking at on the site, it will to our database to display on the Home Page.

The information for the movies is collected from the SWAPI API at https://swapi.co/ we cache the data for a short period of
time for easy of use by the user. Their database currently holds information on episodes 1 through 7.

# Learning Highlights from this Project
This project allowed me to dip into many of the different aspects of django and compare to experience and knowledge of other
frameworks. I was already familiar with Python and this project allowed me to use it in a web framework.

- Understanding of Django's MTV pattern compared to the MVC pattern.
- Use of Class based Views.
- Practice in using 3rd party API calls.
- Use of caching.
- Creating tests for each aspect of the MTV.
- Understanding of how Django interacts with it's database through the Model.
- Usage of Session data.
- Template use with CSS/JS Framework.(Materialize)

# Bug List
-(Resolved) SWAPI had a domain name change. Broke ability to search for any items in DB.
- SWAPI domain change has made some favoriting not work in all catagories. ex/ Favoriting Humans works, but not Droids.

