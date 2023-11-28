# Homework 4: Weather API

This is the starter code for the 4th homework assignment for WEB 1.1. Follow the instructions here: https://make-school-courses.github.io/WEB-1.1-Web-Architecture/#/Assignments/03-APIs

##Part 1: Current Weather Data
- [x] Open up the app.py file in your starter code. Complete the TODOs in the results() route to retrieve the user's choices, construct the API query parameters, check the results of the API call, and pass the resulting data to the client.

Then, open the results.html file and complete the TODOs to show the resulting data.

It may be helpful to read over the API documentation for the current weather endpoint.

Also, you may want to review the requests Quick Start Guide if you're having trouble understanding how the API call is being made or how the data is being passed.

Part 2: Comparing Two Cities
Take a look at the comparison_results.html file. You will need to complete the TODOs to compare two cities.

The comparison_results route gives a bit less guidance on how to proceed, but by now, you should have a good understanding on how to make these API calls! See if you can use the hints to make your code more elegant and efficient.

Stretch Challenges
Complete one or more of the following stretch challenges and demonstrate a higher-level understanding of the topic(s) in order to earn "stretch" points.

These are all just ideas - feel free to riff off of these to create your own stretch challenges!

Show an Icon
The API data returned from OpenWeatherMaps includes an "icon" field that we can use to show an image of the current weather conditions (e.g. sunny, cloudy, rainy, etc). See here for a list of weather conditions and their corresponding icons.

Modify the results.html and/or comparison_results.html pages to show an icon image for that day's weather conditions.

Error Handling
Currently, the app doesn't have any error handling, so if the user enters a city that doesn't exist or a date outside of the allowed range, they are shown a generic error message. Modify the routes to show a 404 page if the user enters invalid data.

Style Level Up
The styling in the results.html and comparison_results.html files is kind of plain - the weather conditions are just shown in bullet points. See if you can add to the styles in static/style.css to improve on it!

