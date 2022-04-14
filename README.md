
# Six Nations Rugby Quiz

For my **Portfolio 3 Project** on the **Code Institute's Diploma in Software Development (E-commerce Applications)** course I have created a command line Six Nations Rugby Quiz game.  Just like the tournament itself there are six sections for each of the countries.  The user will be asked 5 random questions in each section relating to a particular country.  The user can select whichever country their want to start with and work their way through each country, when their score will be totalled and they will find out if they made the leaderboard or not!   

Link to the deployed app is [here](https://sixnationsrugbyquiz.herokuapp.com/). 

Link to the repository is [here](https://github.com/rockymiss/sixnationsrugbyquiz). 



![alt text](https://res.cloudinary.com/rockymiss/image/upload/v1649890785/rugby/mockup_kgpgxf.png)

-----

## Who is this game for and what does it do?
This game is for anyone who likes Rugby, particularly the Six Nations Tournament.  
 
-----

## User Experience


### From a User's Perspective
As a user it is important: 

1. That it is easy to follow the game. 
2. To understand the rules of the game. 
3. To understand how to start the game. 
4. To choose a game they want to play.
5. To quit the game if they want to. 
6. To answer questions and receive a result. 
7. To view their scores. 
8. To view the leaderboard.  


### Users Fulfilment

1.  The game is laid out clearly so the user knows immediately what to do.  A welcome message is provided prompting the user for their name. 
2.  Rules are available for the user to view. 
3.  Clear instructions are given on how to start the game.
4.  Clear instructions are given on how to select the country they want to play. 
5.  The user is given opportunities to quit the game throughout. 
6.  The user is asked multiple choice questions which they can answer by typing in a letter and are given a result as to whether they answered correctly or incorrectly. 
7.  After each section ends the user is shown how they scored in that round. 
8.  At the end of the game and if they quit the user is given the option to view the leaderboard. 


-----
## UX 

While I did want to give the game a bit of design it was designed minimally as the instructions were to produce a command line interface application.  Minimal styles were achieved by adding a background image, adding a mock screen and color to the 'Let's Play' button. 

![alt text](https://res.cloudinary.com/rockymiss/image/upload/v1649938195/rugby/wireframe_hs0tpn.png)



<p align="center"><img src="rugbyquizflow.png"></p>


### Python Logic

I created a flow chart using drawio.  The chart gave me an idea of the flow of the game and how the game would progress, paying particular attention to user input and validation.  While some changes have been made to the quiz since drafting this flow chart it was extrememly beneficial in how the quiz was put together.  

<p align="center"><img src="rugbyquizflow.png"></p>



### Scope  

#### Existing Features

- Startup Display
  - The first display the user will see is the startup screen showing the logo done with ASCII art with the words "Rugby Quiz".  
  - A welcome message tells the user a small bit about the game.
  - The user is prompted to enter in their name. 
  - The user will then be asked to read the rules of play the game. 

- Rules
  - If the user selects to view the rules the rules are shown setting out the game.  The user will be told that there are six sections, one for each country that take part in the Six Nations Rugby Championship.  Users are told the questions are multiple choice and can be answered by typing in a, b, c.    The user will then be asked to play or quit. 

- Choices Menu
  - If the user chooses to play a list of choices will show for each country.  The user can select one of the six countries by typing in "eng" for England, "ire" for Ireland, "sc" for Scotland, "wal" for Wales, "fr" for France and "sc" for Scotland.  The user can select whichever country they wish to start on. 

- Quiz Questions
  - Once the user makes a choice of which country they will be asked 5 questions in relation to that country.  The questions are displayed with the available answers underneath.  The user is prompted to pick and answer by typing a, b, or c.  
    - Correct Answer 
      - If the user answers correctly it will be displayed in green. 
    - Incorrect Answer
      - If the user answers incorrectly it will be displayed in red. 

- Section Results
  - Once all questions have been answered in the Quiz Questions section a results page will open up telling the user how many points they scored in that section.  The user can then decided to continue playing or to quit the game. 

- Remaining Choices 
  - If the user decides to continue playing after Section results then they will be given a list of remaining countries to choose from.  Once they choose another country they will be re-directed by to the Quiz Questions, then Section results and back to remaining Choices until all games have been completed.  

- No Choices Left
  - Once all games have been completed the user will be directed to the a screen telling them that they have no choices left to play.  The user is asked if they want to see the leaderboard or to quit the game.   

- Leaderboard
  - If the user chooses to view the leaderboard a banner with the word "Leaders" will appear and a table beneath it showing the top three highest scores.  Users names are displayed along with scores for each country. 

- 







### Structure Plane


### Skeleton 




### Surface  

##### Colors 





 
##### Typography




-----
## Future Implementation 



-----
## Technologies Used 


- HTML5 to provide content and structure to the website.
- CSS3 provides styles for the website. 
- Python
-  
- [Cloudinary.com](https://www.cloudinary.com/) to store images for the website.
-
- 
- Gitpod to create and edit the website. 
- GibHub for hosting files and deployment of the website.
- Google Chrome DevTools for debug and testing site.
- GitBash to push changes to the GitHub repository.



</details>

-----
## Resources 

- Code Institute course materials, tutor and mentor support.
- Code Institute Slack Community.
- Love Sandwiches walk-through on Code Insitute.
- [W3schools](https://www.w3schools.com/) 
- [Brock Byrd](https://brockbyrdd.medium.com/creating-a-multiple-choice-quiz-in-python-terminal-1c46123b86d5) for quiz class layout etc. 
   

### Images





-----
## Testing


### Local Testing


### User Testing

The website was sent to a group of approximately 15 people of all different ages.  My children 6 and 8 also tested the game and could manage functionality well and really enjoyed it.  Other users found the game easy to work through but found it hard to win in under 8 flips.  I didn't change the flip lives because of this as all users kept going back to the game to try to win!  Some in competition with others.  I liked this as they kept coming back to it.  Devices used to test were as follows: 


### Browser Testing

The Website has been tested on Google Chrome, Microsoft Edge, Safari and Opera.   On all browsers testing was as expected.  Functionality and responsiveness are good. 


### Validators 

The website was tested using Jigsaw W3C validation. 




### Responsiveness 

To check responsiveness I used Google Chrome Dev Tools.  Desktop, Mobile and tablet sizes were tested.  The website responded well.   
<br>

###  Result: Chrome Lighthouse 




</details>
<br>


### Color Contrast Testing 

I used [a11y](https://https://color.a11y.com/) to test the color contrast on the website which produced no issues. 
<details open>
<summary>Color Contrast </summary> 
<p align="center"><img src=""></p>

</details>
<br>

### Accessibility 


<details open>
<summary>accessibilty</summary> 
<p align="center"><img src=""></p>

</details>
<br>


### Issues/Bugs Fixed 



<details open>
<summary>Issue images</summary>
<p align="center"><img src=""></p>
</details>
<br>



<details open>
<summary>Safari/Iphone Error</summary>
<p align="center"></p>
</details>
<br>


### Issues Unresolved




-----
## Version Control


### Git and GitHub 

Local repository and IDE used: GitPod
Remote repository used: GitHub

Steps followed: 
- I created a new public repository on GitHub using the Code Institute template.
- I then created a workspace and started coding on GitPod. 
- All relevant files were created. 
- As I worked I previewed changes using python??.
- To save my work safely I continued to use the terminal consistently by using: 
    - **git add .** to add work to git
    - **git commit -m""** to commit the work 
    - **git push** to update work to GitHub 


### Deployment 


  #### Deployment: 
        
    

<details open>
<summary>Deployment Preview Image</summary>
<br>
<p align="center"><img src=""></p>

</details>
    

  #### Fork: 
        
    A copy can be made of a repository by forking the repository.  The copy can then be viewed and changed without affecting the original repository. 
    
      - From your list of repositories select the repository you want to fork.
      - On the top of the page to the right had side you will see a fork image.  Click on the button to create a copy. 

      
  <details open>
<summary>Fork Preview Image</summary>
<br>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1642789173/kitchen-nippers/fork-preview_xraeo2.png"></p>

</details>


  #### Clone: 
        
    Cloning this project from GitHub can be done by following these steps: 
    
      - From your list of repositories select the repository you want to deploy.
      - Click on the code tabe. 
      - Click on the clipboard icon to copy the URL.  
      - Open Git Bash in your IDE. 
      - Change the current working directory to the location you want to place the clone. 
      - Type git clone and paste the copied URL.  
      - Press enter for the clone to be created. .

  <details open>
<summary>Clone Preview Image</summary>
<br>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1642790166/kitchen-nippers/clone-preview_kkvsfx.png"></p>

</details>
<br>


-----
## Acknowledegments/Conclusion


Rachel Rock April 2022
