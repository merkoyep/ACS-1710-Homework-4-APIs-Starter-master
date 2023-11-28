# Homework 4: Weather API

This is the starter code for the 4th homework assignment for WEB 1.1. Follow the instructions here: https://make-school-courses.github.io/WEB-1.1-Web-Architecture/#/Assignments/03-APIs

## Part 1: Current Weather Data
- [x] Open up the app.py file in your starter code. Complete the TODOs in the results() route to retrieve the user's choices, construct the API query parameters, check the results of the API call, and pass the resulting data to the client.

- [x] Then, open the results.html file and complete the TODOs to show the resulting data.


## Part 2: Comparing Two Cities
- [x] Take a look at the comparison_results.html file. You will need to complete the TODOs to compare two cities.

- [x] The comparison_results route gives a bit less guidance on how to proceed, but by now, you should have a good understanding on how to make these API calls! See if you can use the hints to make your code more elegant and efficient.

## Stretch Challenges

Show an Icon
- [x] The API data returned from OpenWeatherMaps includes an "icon" field that we can use to show an image of the current weather conditions (e.g. sunny, cloudy, rainy, etc). See here for a list of weather conditions and their corresponding icons.

- [x] Modify the results.html and/or comparison_results.html pages to show an icon image for that day's weather conditions.

Error Handling
- [] Currently, the app doesn't have any error handling, so if the user enters a city that doesn't exist or a date outside of the allowed range, they are shown a generic error message. Modify the routes to show a 404 page if the user enters invalid data.

Style Level Up
- [x] The styling in the results.html and comparison_results.html files is kind of plain - the weather conditions are just shown in bullet points. See if you can add to the styles in static/style.css to improve on it!

