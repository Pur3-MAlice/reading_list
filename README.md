**Reading List**

## **Overview**
This program is a smart reading list that automatically updates a google spreadsheet with the user input from the app.
  
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
* Have duplicate inputs highlighted in the app, and then also be able to choose whether or not they are still added to the list of choice.
* Leave the app/close off the app.

## ***Site Aims:***
The site aims to:
1. Create a simple to use interface.
1. Tell the user if they have made any errors whilst using the program and prompt them as such.
1. Automatically have book inputs given randomly assigned number letter 'unique number'.
  
## ***How Will This Be Achieved:***
To achieve the above, the site will:
1. User validation via error messages.
1. User the random int and random letter to create unique code.
1. use .upper and .lower to make sure any user prompts where error proof and either case could be used when entering letters for app navigation.
1. Using the break feature at the 'home page' to stop the program.


## ***Flow Chart:***
To understand the steps required in order to program the game, I created the below flowchart using [lucid charts](https://www.lucidchart.com/).  

![Logic Flowchart](/documents/reading_list_flowchart.jpg) 

# **Features**
## **Home page:**
From the Home page, the user has access to three things: -
* About Page / How to use.
* Access Read List.
* Access TBR List.  
* Cancel the program.

![Home Page](/documents/home_screen.jpg)
![Home Page Cancel](/documents/home_screen_cancel.jpg)

## **About page:**
The About page: -
* Tells the user what the app is for and how to use. Also gives the user a brief intro on how to nav the app.

![About Page](/documents/about.jpg)

## **TBR and READ list page:**
The TBR and READ list page: -
* TBR and READ page (identical) - check the list, add an input, go home.
* Base for letting user edit and adapt their sheet.

![TBR List](/documents/tbr_list.jpg)

## **Check list page:**
 Check list
 * The check list page lets the user see in the terminal all the data on that particular list (TBR/READ)
 * It uses the Rich add on for python to make it look nicer.

  ![Check list](/documents/terminal_table.jpg)

## **Book input page:**
 Book input
 * Lets the user input the title and author of the book they are adding to their list.
 * Automatically makes the inputs Title Case with .title().

  ![Book input](/documents/add_book.jpg)

## **Duplicate catch page:**
Duplicate catch
* Lets the user know if they already have that title on their list, but the user may want to add it again or the title may be used by another author so the user is given the choice to add it or not.
* Catch dupe, then don't add the entry, but also add the entry.

  ![Dupe catch](/documents/dupecheck.jpg)

  ![Dupe catch, no](/documents/dupecheck_no.jpg)

  ![Dupe catch, yes](/documents/dupecheck_yes.jpg)

## **Sheet update:**
 Sheet update with the number gen
 * This is the image of the updated sheet with the addition of the unique number gen which is a feature to help disseminate each input.
 * The unique number is composed of (1, 100) and (A-Z/a-z). EX. 85D or 32f or 54P
 
  ![Sheet Update](/documents/update_sheet.jpg)

## **Delete row based on title:**
 Delete row
 * The user can choose to delete a row on their TBR list by entering the title of the page
 * This checks for the title being on the list and for user entry.

  ![Delete Row](/documents/delete_row.jpg)  

## **Future-Enhancements**
* To make this application better in the future these are the things I would include:
  1. The ability to remove books after checking the list of choice.
  1. The ability to add in multiple books at once.
  1. The option to add in list of books from sources such a bestseller lists.
  1. Add due date for TBR entries to ensure there's a timeline for the user to read books. This could be used for students.
  1. Be able to delete rows based on Unique ID or author not just title.
  1. Be able to delete multiple rows
  1. Be able to move rows from one sheet to the other.

# **Data Model**
## **Logic Flow:**
The home function is called at the end of the run.py file, just after the banner call. The welcome screen is now loaded and has ascii art and the user selection home page. The user can read the about, the delete from TBR, go to their TBR, or go to their READ list. They also have the option to cancel the program and leave. Entering the appropriate letter will take them to that area. Spaces and letters not shown to guide the user throw user errors.

Once the user enters "X" to go to the list, the set user's list is passed to each function moving forward to ensure that the correct sheet is being edited by the user. As part of the error handling for the input, the user cannot enter any other letters or numbers without being passed an error message.

This app works with Google Sheets API and works to add and remove rows from the users TBR and READ lists, which are part of the Google worksheet.

# **Libraries**
For this project to work, I required imported libraries: -
### ***os:***
  * Clear Screen. This was used to keep the terminal clean for a better user experience, without a long terminal the user can focus on what needs to be interacted with at that moment.
### ***rich:***
   * Rich is a Python library for rich text and beautiful formatting in the terminal. I used this primarily for printing tables for a better UX. This was used with console, table and box.
### ***datetime:***
   * Datetime was used to get the exact date of the user input and append it to the google sheet.
### ***time:***
   * Time was used for the screen delays. I input some screen delays so the user wasn't bombarded with information and could easily digest when change in the terminal happened.
### ***pyfiglet:***
   * Pyfiglet was used for the home screen ascii art.
### ***pandas:***
   * Pandas was used to create data frames that made working with the data of the spreadsheet easier and more manageable.
### ***random: / string:***
   * Random used to create random number (1, 100) and random letter concat to give the book input a unique code.

## **During Development Testing**
### ***Manual Testing:***
During the development process, I was manually testing in the following ways:-
* Manually testing each user input for errors via the console in gitpod. Also later tested in Heroku.
    * Detailed below is the method in which I tested the app to make sure that it did what was intended. This test was focused on any unexpected outcomes. I have taken screen shots of the excel file used to do my manual testing. Please see the below:
    ![Home Page Test](/documents/home_test.jpg)
    ![About Page Test](/documents/about_page_test.jpg)
    ![Add Page READ Test](/documents/add_page_read_test.jpg)
    ![Add Page TBR Test](/documents/add_page_tbr_test.jpg)
    ![READ choose Test](/documents/read_choose_page_test.jpg)
    ![TBR Choose Test](/documents/tbr_choose_page_test.jpg)  
    ![Title input Test](/documents/title_input_test.jpg)           
        
* Asked a Data Scientist friend to review the app by following the above procedure often throughout the development of the game. They did not offer any help on the coding nor did they provide feedback other than "XXX" is doesn't work as expected. They did however make a good soundboard for me to talk at while talking through difficult code issues.

### ***Bugs and Fixes:***
Below is a list of bugs I found during the development process. A lot of the bugs and fixes where minor enough that they were caught and easily amended by just seeing the redlines in gitpod. But here are a few that stumped me enough to write them down.
1. **Intended Outcome** - Be able to go through the programs easily without too much looping.
    * ***Issue Found:*** 
        * Unable to get out of program. And looping occurred without breaks.
    * ***Solution Used:*** 
        * Added one break option at the home page. User chosen "X". Also removed unnecessary.
1. **Intended Outcome** - Only be able to add title and authors if there is a user input.
    * ***Issue Found:*** 
        * Could add book input without and characters.
    * ***Solution Used:*** 
        * Use enforced min input for title and author - min string.
1. **Intended Outcome** - Don't check for entries of error book inputs, such as having no actual input
    * ***Issue Found:*** 
        * The app was checking for dupes despite their being no title.
    * ***Solution Used:*** 
        * Added in a while True loop
1. **Intended Outcome** - The add dupe Y/N function to only accept Y and N. Other inputs throw error.
    * ***Issue Found:*** 
        * Any other input other than Y/N broke the code and sent the user back to the start
    * ***Solution Used:*** 
        * Added in a while True loop and an else title_prompt = "".     

## **Post Development Testing**
### **Validators**
#### ***PEP8*** - [PEP8](https://pep8ci.herokuapp.com/)
* ***Issue Found:***
    * Trailing whitespace on line 61
* ***Solution Used:***
    * Removed trailing whitespace on line 61

# **Deployment**
## ***Final Deployment to Heroku:***  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. Log in to Heroku
1. Click the button labelled "New”.
1. From the drop-down menu select "Create new app".
1. Enter a unique app name. I called this one reading-list-alice.
1. Once the web portal shows the green tick to confirm the name is original.
1. Select the relevant region, I chose Europe as I am in the UK.
1. Click on the "Create app" button.
1. From the project "Deploy" tab, nav to the settings tab and scroll to the "Config Vars" section. 
1. Click the button labelled "Reveal Config Vars" and enter port / 8000. Click the "add" button.
1. Scroll to the buildpacks section of the settings page and click the button labelled "add build pack," select "Python," and click "Save Changes".
1. Repeat step 11 - add "node.js" instead of python. 
   * ***IMPORTANT*** The buildpacks must be in the correct order.
1. Scroll to the top of the settings page, and nav to the "Deploy" tab.
1. From the deploy tab select Github as the deployment method.
1. Confirm you want to connect to GitHub.
1. Search for the repo and click the connect button.
1. From the bottom of the deploy page select your preferred deployment type by follow one of the below steps:  
   * Clicking “Enable Automatic Deploys" for automatic deployment when you push updates to Github. Which is what I chose to test after deployment.
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.

### **References**
* Whilst I did try to deviate as much as possible, this project was influenced by the code project love sandwiches which I built before starting this project.
* I did rely on Stack Overflow, W3schools, openpyxl and MDN web docs for general references and problem solving throughout the project.
# **Credits**
* The idea to decorate the board with numbers above and to the side came from [Knowledge Mavens youtube channel](https://youtu.be/alJH_c9t4zw)
* Clear console function copied from [delftstack.com](https://www.delftstack.com/howto/python/python-clear-console/)
* [lucid chart.com](https://www.lucidchart.com/) was used to create the flow chart
* [Code Institute](https://codeinstitute.net/) for providing the template. [template](https://github.com/Code-Institute-Org/python-essentials-template) 
* [ASCII_ART] Used the code from this webpage to create my interface banner.(https://www.devdungeon.com/content/create-ascii-art-text-banners-python)
