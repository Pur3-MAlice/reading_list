 **Reading List**

## **Overview**
This program is a smart reading list that automatically updates a google spreadsheet with the user input from the app.

For this program I focused on function based programming.
  
[Click here to be taken to the final deployment of the project.]()

![Screenshot of the welcome screen](/documents/home_screen.jpg)

## **Table of Contents** 
* [**Reading List**](#reading-list)
  * [**Overview**](#overview)
  * [**Table of Contents**](#table-of-contents)
  * [**How to Use:**](#how-to-use)
* [**Planning Phase:**](#planning-phase)
  * [***User Stories:***](#user-stories)
  * [***Site Aims:***](#site-aims)
  * [***How Will This Be Achieved:***](#how-will-this-be-achieved)
  * [***Flow Chart:***](#flow-chart)
* [**Features**](#features)
  * [**Welcome Screen:**](#welcome-screen)
  * [**Future-Enhancements**](#future-enhancements)
* [**Data Model**](#data-model)
* [**Testing Phase**](#testing-phase)
* [**Libraries**](#libraries)
* [**Deployment**](#deployment)
* [**Credits**](#credits)

## **How to Use:**
* Once deploying the program. The user can enter 'X' letters do navigate through the terminal to different areas of the program. This is done to check their READ list, TBR list and also to add book inputs to both.
* The user can also stop the program entirely from the home page, which can either be naved back to or the user will automatically be dropped back to after inputs.
* Input book title and then author name when on the add pages for TBR and READ.

# **Planning Phase:**
## ***User Stories:***
As a user, I want to be able to:
* Add books, title and author, to either my To Be Read (TBR) list or my Read (READ) list easily.
* Have the date of book input automatically put into the sheet.
* Check both the TBR and READ lists. 
* Automatically update the lists so they can be checked correctly right away.
* Have dupelicate inputs highlighted in the app, and then also be able to choose wether or not they are still added to the list of choice.
* Leave the app/close off the app.

## ***Site Aims:***
The site aims to:
1. Create a simple to use interface.
1. Tell the user if they have made any errors whilst using the program and prompt them as such.
1. Automatically have book inputs given randomly assigned number letter 'unique number'.
  
## ***How Will This Be Achieved:***
To achieve the above, the site will:
1. validation
1. User the random int and random letter to creat uniwue code
1. use .upper and .lower to make sure any user prompts where error proof and either case could be used when entering letters for app navigation.
1. Using the break feature at the 'home page' to stop the program.


## ***Flow Chart:***
To understand the steps required in order to program the game, I created the below flowchart using [lucid charts](https://www.lucidchart.com/).  

![Logic Flowchart](/documents/reading_list_flowchart.jpg) 

# **Features**
 Home page
    ![Home Page](/documents/home_screen.jpg)

 Home page cancel
    ![Home Page Cancel](/documents/home_screen_cancel.jpg)

 About Page
    ![About Page](/documents/about.jpg)

 TBR and READ page (idenitcal) - check or add choice
    ![TBR list](/documents/tbr_list.jpg)

 Check list
    ![Check list](/documents/terminal_table.jpg)

 Book input
    ![Book input](/documents/add_book.jpg)

 Duplicate catch
    ![Dupe catch](/documents/dupecheck.jpg)
    ![Dupe catch, no](/documents/dupecheck_no.jpg)
    ![Dupe catch, yes](/documents/dupecheck_yes.jpg)
    
 Sheet update with the number gen
    ![Sheet Update](/documents/update_sheet.jpg)

## **Home page:**
From the Home page, the user has access to three things: -
* About Page / How to use
* Access Read List.
* Access TBR List.  
![Welcome screen screenshot]()

## **Future-Enhancements**
* To make this application better in the fututre these are the things I would include:
  1. The ability to remove books after checking the list of choice.
  1. The ability to add in mutliple books at once.
  1. The option to add in list of books from sources such a bestseller lists.
  1. Add due date for TBR entries to ensure there's a timeline for the user to read books. This could be used for students.

# **Data Model**

## **Logic Flow:**

### ***Setup Phase:***

# **Testing Phase**
Below is the tesing done for this page. It is in the format, action, expected outcome and then outcome. This was done after all inital fixes, but I will also indicate where I found errors that were later on fixed.

# **Libraries**
For this project to work, I required imported libraries: -
### ***os:***
  * Clear Screen. This was used to keep the terminal clean for a better user experince.
### ***rich:***
   * Rich is a Python library for rich text and beautiful formatting in the terminal. I used this primarily for printing tables for a better UX. This was used with console, table and box.
### ***datetime:***
   * datetime was used to get the exact date of the user input and append it to the google sheet.
### ***time:***
   * time was used for the screen delays. I input some screen delays so the user wasn't bombared with infomation and could easily digest when change in the terminal happened.
### ***datetime:***
   * datetime was used to get the exact date of the user input and append it to the google sheet.
### ***pyfiglet:***
   * pyfiglet was used for the homescreen ascii art.
### ***pandas:***
   * pandas was used to create dataframes that made working with the data of the spreadsheet easier and more managable.
### ***random: / string:***
   * used to create random number (1, 100) and random letter concat to give the book input a unique code.

# **Deployment**
## ***Final Deployment to Heroku:***  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. Log in to Heroku
1. Click the button labeled "New"
1. From the drop-down menu select "Create new app".
1. Enter a unique app name. I called this one reading-list-alice.
1. Once the web portal shows the green tick to confirm the name is original.
1. Select the relevant region, I chose Europe as I am in the UK.
1. Click on the "Create app" button.
1. From the project "Deploy" tab, nav to the settings tab and scroll to the "Config Vars" section. 
1. Click the button labelled "Reveal Config Vars" and enter port / 8000. Click the "add" button.
1. Scroll to the buildpacks section of the settings page and click the button labeled "add buildpack," select "Python," and click "Save Changes".
1. Repeat step 11 - add "node.js" instead of python. 
   * ***IMPORTANT*** The buildpacks must be in the correct order.
1. Scroll to the top of the settings page, and nav to the "Deploy" tab.
1. From the deploy tab select Github as the deployment method.
1. Confirm you want to connect to GitHub.
1. Search for the repo and click the connect button.
1. From the bottom of the deploy page select your preferred deployment type by follow one of the below steps:  
   * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github. Which is what I chose to test after deployment.
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.


# **Credits**
* The idea to decorate the board with numbers above and to the side came from [Knowledge Mavens youtube channel](https://youtu.be/alJH_c9t4zw)
* Clear console function copied from [delftstack.com](https://www.delftstack.com/howto/python/python-clear-console/)
* [lucid chart.com](https://www.lucidchart.com/) was used to create the flow chart
* [Code Institute](https://codeinstitute.net/) for providing the template. [template](https://github.com/Code-Institute-Org/python-essentials-template) 
* [ASCII_ART] Used the code from this webpage to create my interface banner.(https://www.devdungeon.com/content/create-ascii-art-text-banners-python)