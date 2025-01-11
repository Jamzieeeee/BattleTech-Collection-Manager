# BattleTech Collection Manager

![BattleTech Collection Manager](documentation/images/responsive.png)

Portfolio 4 project as part of the Diploma in Full Stack Software Development by Code Institute.

---

BattleTech Collection Manager (BTCM) is a website that lets users manage their collection of miniatures for the BattleTech boardgame.

It is a fullstack web application that allows users to browse the current catalogue of available miniatures, and create an account in order to manage their own collection. User with the appropriate permissions can add new items to the catalogue when they are released.

Link to live site: [https://battletech-collection-manager-b607f0b95fe2.herokuapp.com](https://battletech-collection-manager-b607f0b95fe2.herokuapp.com)



___

## Site Objectives

Design and create a web application to demonstrate an increasing understanding of the libraries and frameworks available to developers.

My three main objectives were:

- ### Create a readable, clean and responsive front end

  I wanted to make the site easily accessible and intuitively navigated for the users. Django and Bootstrap were used to create and style the front end.

- ### Make use of available backend functionality

  The use of the backend framework allows users to create a profile, add, edit, and delete miniatures from their collection.

- ### Store data on an external cloud database

  I used NeonDB to store the PostgreSQL database for this project.

___

# User Experience/UX

## Target Audience

- Players of the BattleTech boardgame that are interested in keeping a record of their miniatures collection.

## User Stories

### New Visitor Goals

- To understand what the site and content is about.
- How to navigate the site.
- Create an account and engage with the site and start a collection.

### Existing Visitor Goals

- Log in and out of their account.
- View their collection and make updates to it.
- As a Catalogue Manager: keep the Catalogue up to date with new product releases.

# Design

## Wireframes

![iPhone Catalogue](documentation/images/iPhone%20SE%20-%201.png)
![iPad Catalogue](documentation/images/iPad%20Pro%2011_%20-%201.png)
![Desktop Catalogue](documentation/images/Desktop%20-%201.png)

# Data model
### Catalogue
- Base ID: CharField(6)
    - Represents the ID moulded on the base of the miniature
    - Is not unique (There are different miniatures with the same Base ID)
    - Is validated against a pattern which matches all known Base ID formats
- Name: CharField(255)
    - Name of the miniature
- Notes: TextField(can be Null/Blank)
    - Extra information 
- Image: ImageField(can be Null/Blank)
    - An image of the miniature
    - Is required to be less than 500KB

### Collection
- Owner: User
    - From django.contrib.auth.models
- Mini: Catalogue
    - References the Catalogue model
    - It is possible for users to own multiple copies of the same miniature
- Notes: TextField(can be Null/Blank)
    - Extra information

### Authentication/Authorisation 
- Uses django.contrib.auth.models User and Group
    - Users with permission to modify the Catalogue are in the 'Catalogue Managers' group, and must be added via the django admin page by a SuperUser.


# Features

## Existing Features

Homepage with explaination of site with links
![Homepage not logged in](documentation/images/homepage-not-logged-in.png)

The user can log in and register an account
![Login](documentation/images/login.png)

Miniatures Catalogue with the ability to add to collection
As a Catalogue Manager: add, edit, or delete entries from the catalogue
![Catalogue logged in](documentation/images/catalogue-logged-in.png)

View collection with the ability to edit or delete items from it
![Update collection](documentation/images/update-collection.png)

Detailed view of item in catalogue or collection
![Catalogue detail](documentation/images/catalogue-detail.png)
![Collection detail](documentation/images/collection-detail.png)



## Future Features

- Allow the user to add images of items to their collection
- Allow the user to search the catalogue/their collection for a specific miniature by name or base ID
- Allow the user to define a paint scheme (including notes on which paints were used etc...) and apply it to an item in their collection

# Technologies Used

Here are the technologies used to build this project:

- [Gitpod](https://gitpod.io/) To build and create this project
- [Github](https://github.com) To host and store the data for the site.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- [NeonDB](https://www.neon.tech/) Used to store PostgreSQL database.
- [Heroku](https://id.heroku.com/) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [CrispyForms](https://django-crispy-forms.readthedocs.io/)
- [Crispy-Boostrap](https://pypi.org/project/crispy-bootstrap5/)
- [Whitenoise](https://whitenoise.readthedocs.io/)
- [Pillow](https://pypi.org/project/pillow/)

# Agile

This project was designed using Agile methodology, utilising the Project Board and Issues sections in GitHub

- [Project Board](https://github.com/users/Jamzieeeee/projects/3/views/1)

# Testing 

## Manual Testing

### As User
| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Can create an account | Created successfully | Pass |
| Can log in | Logged in successfully | Pass |
| Can log out | Logged out successfully, but logging in again straight from the logout page takes you back to the logout page | Fail(1) |
| See different homepage when logged in | Page loaded correctly | Pass |
| Can view catalogue | Page loaded correctly | Pass |
| Can add item to collection | Item added successfully | Pass |
| Can view collection | Page loaded correctly | Pass |
| Can edit item in collection | Item edited successfully | Pass |
| Can delete item in collection | Item deleted successfully | Pass |
| Cannot access catalogue management | Access denied | Pass |

(1) The next url passed to the login page needs not to be set when on the logout page

### As Catalogue Manager
| TEST | OUTCOME | PASS/FAIL |
|:---:|:---:|:---:|
| Can view catalogue management controls | Create, edit, and delete visible | Pass |
| Can add item to catalogue | Item added successfully | Pass |
| Can edit item in catalogue | Item edited successfully | Pass |
| Can delete item in catalogue | Item deleted successfully | Pass |

## Validator Testing 

### Lighthouse
Testing the full Catalogue page which contains all current 253 known BattleTech miniatures.

![Lighthouse results](documentation/images/lighthouse.png)

### HTML/CSS
Testing the homepage and a Collection detail page with an image.
![w3 results](documentation/images/w3-homepage.png)

### Python
Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

A number of errors and whitespace issues were found and rectified. The linter does not seem to handle escape characters in regular expression correctly (models.py, line: 11)

Python Files Tested:

- models
- forms
- views
- urls

## Unfixed Bugs

- The Catalogue is sorted by Base ID as a string, because the values are somewhat inconsistent and not all of them are numbers. It would be good to use a better sorting function.

# Deployment

## Github Deployment

The website was stored using GitHub for storage of data and version control. To do this I did the following;

After each addition, change or removal of code, in the terminal within your IDE (I used codeanywhere for this project) type:

- git add .
- git commit -m "meaningful commit message"
- git push

The files are now available to view within your github repository.

## Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page

## Clone

To create a clone you do the following;

1. Click on the code tab, left of the Gitpod tab
2. To the right of the repository name, click the clipboard icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repository name
6. Clone has been created

## Repository deployment via Heroku

- On the [Heroku Dashboard](https://dashboard.heroku.com) page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. Then click 'Create app'
- In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. The credentials for this app were:

1. Postgres Database URL
2. Port (8000)

- Below this click Add buildpack and choose python and nodejs in that order.

## Deployment of the app

- Click on the Deploy tab and select Github-Connect to Github.
- Enter the repository name and click Search.
- Choose the repository that holds the correct files and click Connect.
- A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub.
- Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button which should appear below the build information window, alternatively, there is another button located in the top right of the page.

## Initial Catalogue data load

- Run `python3 manage.py loaddata CurrentMechList.json` to load the current BattleTech catalogue into the database

# Credits 

## Content 
The initial project structure was based on Code Institute's 'I Think Therefore I Blog' project. 

I created models to represent the Catalogue and Collection, and then added custom views and forms to manage them.

I referred to code examples from the following sites to build the project:
- [Bootstrap docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
    - For bootstrap styling
- [GeeksforGeeks](https://geeksforgeeks.org)
    - For django views and bootstrap styling
- [Django docs](https://docs.djangoproject.com)
    - For code examples and reference
- [W3Schools](https://w3schools.com)
    - For code examples and reference
- [Abidibo's blog](https://www.abidibo.net/blog/2014/05/22/check-if-user-belongs-group-django-templates/)
    - For the django template filter to check whether a user is in a group

- Initial Catalogue data from [Sarna BattleTech Wiki](https://sarna.net)

The Readme layout was based indirectly (via [Mark Daniel](https://github.com/markdaniel1982/MD82-P4/blob/main/README.md)) on the example by [Kera Cudmore - Readme Examples](https://github.com/kera-cudmore/readme-examples/blob/main/README.md?plain=1) and [Sdalsosa - Readme](https://github.com/Sdalsosa/ComposerHub/blob/main/README.md)

The wireframe mockups were created using [Figma](https://www.figma.com/)


## Media

- Favicon is taken from [https://www.talesfromtheperiphery.org.uk/](https://www.talesfromtheperiphery.org.uk/) with permission

- Miniature images from [Sarna BattleTech Wiki](https://sarna.net)

## Acknowledgments and Thanks

Jubril Akolade my Code Institute mentor

Kieron Pierson and Jeantelle van Niekerk from the Student Care team

Mike Whitaker (my father)