<h1 align="center"> Hangman ACF (Project3)</h1>

Hangman ACF or Animals, Countries and Foods, is a python terminal game. It will challenge your word knowledge in 3 different categories: Animals, Countries and Foods.
Then main menu allows for new game, print leaderboards and quit. For new game, you will input your Username and select one of the 3 categories. Then press enter when ready.
The game loop starts and you get points for correct guesses which get added to the final score once you find the word. The final score depends on ammount of guesses and word length.

![Responsive Mockup]()

## Index - Table of Contents
* [List of features](#features)
* [UX/UI](#ux-ui)
* [Design](#design)
* [Logic](#logic)
* [Testing](#testing)
* [Deployment](#deployment)
* [Citation of ALL sources](#citations)
* [Future features](#future-features)
* [Known Bugs](#know-bugs)

### FEATURES

- __Main-Menu:__ <br>


### UX-UI

### TESTING

__Validator__

[HTTP-Validator](https://validator.w3.org/nu/)
- Index.html <br>
![Index](documentation/images/passed.PNG)
- style.css <br>
![style](documentation/images/passed-css.PNG)
- script.js <br>
![script](documentation/images/jshint-result-assuming-ES6.PNG)
- JShint was tested under the assumption that ES6 is allowed.<br>

![Lighthouse Desktop](documentation/images/light-house-desktop.PNG)
- Lighthouse results on desktop devices <br>

![Lighthouse mobile](documentation/images/light-house-mobile.PNG)
- LightHouse on Mobile devices recieves a lower score on prefomance due to Main menu image only take up half the page.
- In future development, the difficulty selectors will be displayed below the Hero image for easier access and better visuals.


__Manual Testing__





__Bugs__
- During development that I dedicated extra time fixing:
- ReferenceError: Cannot access 'questionsMedium' before initialization 
- Fix = questionElement syntax error document.get was misspelt..

- Answer button background color cant be reset
- Fix = when calling element by Id, the value put was not registrating as string and the color i was trying to set did not exist (light-gray) when it should have been lightgray.

- Select answer gets called twice second time around
- Fix = moved out addlistEvent click reader outside of all functions and only changed innerHTML for each button.

- If you click multiple times on the buttons before the 1 second timeout timer shows the next question, both color of the button changes and score index gets affected.


__Browser Compatibility__

- Webpage is compatibal with Opera


### DEPLOYMENT

__The site was deployed to GitHub pages. The steps to deploy are as follows:__
- In the GitHub repository, navigate to the Settings tab and select the pages in the bottom left. 
- From the source section drop-down menu, select the Master Branch.
- Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
- Updates or changes to the master branch will take affect on the website

The live link can be found here - [Hangman ACF!](https://hangman-acf.herokuapp.com)


### CITATIONS

__Content__
- Content and layout was loosely based on 80s-Mixtape, Geo-master, the Love Maths Project and Web Dev Simplified Build a Quiz with Javascript.

__Code__
- Base template repository take from: [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) 


### FUTURE-FEATURES


### KNOWN-BUGS

