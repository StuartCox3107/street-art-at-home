
<a name="top"></a>
<div align="center">
<img src="static/favicon/favicon.ico" width="120">
</div>

<div align="center">
<h1>street art @ home</h1>
</div>

---

<div align="center">
<img src="media/devicemockup.png" width="600">
</div>

## Links

### :dart: [Aim of the site](#aim)
### :woman: [User stories](#userstories)
### :compass: [Site plan](#plan) and [Features/Wireframes](#features)
### :art: [Theme & typography](#theme)
### :floppy_disk: [Database features & design](#database)
### :lock: [Features left to implement](#left)
### :bulb: [Technologies used](#tech)
### :goggles: [Testing](#testingsection)
- [Code testing](#code)
- [Manual testing](#manual)
- [User story testing](#usertesting)
- [Further testing](#further)
- [Screen-size testing](#screen)
### :computer: [Deployment](#deploy)
### :ant: [Issues & bugs](#issues)
### :clap: [Credits & acknowledgements](#credits)

---
<a name="aim"></a>

## :dart: Aim of the site

Street art @ home is designed for a fictional company, and designed to showcase and sell prints on canvas of photographs of graffiti and street-art for buyers to put on walls at home. The precise details of the artwork location and artist is indicative rather than 100% true.

## [Link to live site](https://street-art-at-home.herokuapp.com/) opens in same tab, click back if needed

### :arrow_up:[Top of page](#top)

<a name="userstories"></a>

## :woman: User Stories

| As a | I want to be able to | So that I can |
| --- | --- | --- |
| Shopper | View products | Choose ones to buy |
| Shopper | View individual products | View detail on individual products |
| Shopper | Check out interesting new street art | Have access to cutting edge |
| Shopper | View my shopping bag | Know what I am spending |
| |
| Site user | Know what the site is about at first glance | Check immediately whether this is the site for me |
| Site user | Easily register an account | Hold an account and view profile |
| Site user | Easily login or out | Access and use personal information |
| Site user | Have a personal profile | View order and payment history |
|    |
| Shopper | Search for a product by name or description | Find a specific product by city |
| Shopper | Easily see what I have searched for | Make a decision on whether this is a product I want | 
| Shopper | Select the quantity of items to buy | Add to my cart and buy |
| Shopper | View the items in my bag | See the items I have added and want to buy |
| Shopper | Adjust the quantity of items in my bag | Make changes to the quantity chosen |
| Shopper | Remove items from my shopping bag | Change to not buying an item if I change my mind |
| Shopper | Have the ability to order as a guest | Order even if not registered |
| Shopper | Easily enter payment information | Buy the items in my final choice |
| Shopper | View an order confirmation post checkout | So I am assured in knowing the items purchased are the ones I wanted |


### :arrow_up:[Top of page](#top)
---
## :compass: Site plan, features & wireframes

<a name="plan"></a>

### Site plan

Click [here](media/ms4siteplan.pdf) for the site plan, opens in same tab, click back if needed

<a name="features"></a>

## Features & Wireframes

### Landing page

[Desktop Wireframe](wireframes/homedesktop.png) <sub><sup> or </sup></sub> 
[Mobile Wireframe](wireframes/homemobile.png)

Designed to be simple, clean and give a main image with clear links to the possibility to be able to shop as well as a description of what the site is for. This, and all other pages will have a header with a logo and navbar links to the shop, a blog, a Cities area, the shopping basket and user account area. Also, on all views their will be a product search bar present.

The concept of the search bar is to drive users towards the commercial aspects of the site and will search product titles and description only (eg, not blog and cities entries). 

### All products

[Desktop Wireframe](wireframes/all_productsdesktop.png) <sub><sup> or </sup></sub> 
[Mobile Wireframe](wireframes/all_productsmobile.png)

A page showing every product that can be purchased (image, title, price), and a "back to top icon".

### One product

[Desktop Wireframe](wireframes/one_productdesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/one_productmobile.png)

A page showing an individual product, chosen from the all_products view with a description of all fields, the ability to plus or minus the quantity to order and buttons to give the user the ability to continue shopping or add the relevant number of items to the basket.

### Sign up

[Desktop Wireframe](wireframes/signupdesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/signupmobile.png)

A page giving the user the ability to be able to create an account using their personal detail with buttons to sign-in/submit or navigate to the login page if they realise that they do actually have an account already.

### Sign in

[Desktop Wireframe](wireframes/logindesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/loginmobile.png)

A simple page giving the user the ability to enter their username and password that they have to login to their account. Home and Sign-in (process) buttons to be present.

### Profile

[Desktop Wireframe](wireframes/myaccountdesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/myaccountmobile.png)

A simple page giving the user the ability to view their profile details and update if required.

### Basket

[Desktop Wireframe](wireframes/bagdesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/bagmobile.png)

A page showing an image of all items ordered as well as a breakdown of item price and total price. Buttons giving the ability to continue shopping or to go to the checkout app if the user has finished shopping.

### Checkout

[Desktop Wireframe](wireframes/checkoutdesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/checkoutmobile.png)

A page giving the user the ability to review and purchase all chosen items in the bag. A Keep Shopping and Checkout button present.

### Blog

[Desktop Wireframe](wireframes/blogdesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/blogmobile.png)

A simple page with images and detail of added blog items related to the subject areas and designed to showcase the cutting edge.

### Cities

[Desktop Wireframe](wireframes/citiesdesktop.png) <sub><sup> or </sup></sub>
[Mobile Wireframe](wireframes/citiesmobile.png)

A page giving an overview of our favourite cities in terms of street art.

### :arrow_up:[Top of page](#top)
---
<a name="theme"></a>

## :art: Theme & typography

Colours are designed to be largely soft and pastel like but with the option for the addition of a bold pink colour where needed, and a dark grey to give emphasis, the below colour palette was generated using [coolors](https://coolors.co/)

<div align="center">
<img src="media/projectcolours.png" width="500">
</div>

### :arrow_up:[Top of page](#top)

<a name="database"></a>

## :floppy_disk: Database features/design

Data is stored in three models;

**Products**

***Consisting of 6 subsets;***

- Sku- Numerical identifier,
- Name- Product name,
- City- City located in,
- Description- Overview of product,
- Price_l: Price in GBP,
- Image: Image of piece

**Blogentries**

Consisting of 6 subsets;

- Blogid- Numerical identifier,
- Blogposter- Name of poster,
- Blogdate- Date of blog posting,
- Blogtitle- Heading of blog,
- Blogtext- Main text of blog article,
- Blogimage- Article image

**Citiesentries**

Consisting of 4 subsets;

- Citiesid- Numerical identifier,
- Citiestitle- Title of entry (city),
- Citiestext- Main text of cities article,
- Image- Article image


### :arrow_up:[Top of page](#top)
---
<a name="left"></a>

## :lock: Features left to implement

- In the future I would like to add the option for users to be able to choose from various sized images or even custom ones. I would also add email functionality to both the user login process and order confirmation process.

### :arrow_up:[Top of page](#top)
---
<a name="tech"></a>

## :bulb: Technologies used

- HTML, CSS, Javascript & Python languages
- [Google fonts](https://fonts.google.com/) for Poppins font used through all pages, opens in same tab, press back to return, opens in same tab, press back to return
- [Font Meme](https://fontmeme.com/) for logo font, opens in same tab, press back to return
- [Gitpod](https://www.gitpod.io/) IDE used to code, opens in same tab, press back to return
- [GitHub](https://github.com/) To host the repositories for this project, opens in same tab, press back to return
- [Balsamiq](https://balsamiq.com/) used to design wireframes, opens in same tab, press back to return
- [Django](https://www.djangoproject.com/) used as the framework to create the app and the template language
- [Coolors](https://coolors.co/) used for colour palette, opens in same tab, press back to return
- [Bootstrap](https://getbootstrap.com/) front-end framework used, opens in same tab, press back to return
- [Hover.css](https://ianlunn.github.io/Hover/) used to add button hover effect , opens in same tab, press back to return
- [Tiny PNG](https://tinypng.com/) used to compress some images used, opens in same tab, press back to return
- [Heroku](https://dashboard.heroku.com/apps) used to deploy project, opens in same tab, press back to return
- [Flaticon.com](http://www.freepik.com) used for spray can favicon, opens in same tab, press back to return
- [Dreamtimes.com](https://www.dreamstime.com/) used for graffiti man image, opens in same tab, press back to return
- [Cursor.cc](https://www.cursor.cc/) used to generate graffiti spray can cursor, opens in same tab, press back to return
- [Stripe](https://stripe.com/gb) used to process credit card transactions, opens in same tab, press back to return
- [AWS](https://aws.amazon.com/) used to store static and media files
- [Fontawesome](https://fontawesome.com/) used for various icons across the site, opens in same tab, press back to return
- 


### :arrow_up:[Top of page](#top)
---
<a name="testingsection"></a>

## :goggles: Testing
<a name="code"></a>

### Code

- **HTML:** All tested with [W3S HTML Validation Service](https://validator.w3.org/), checked by rendering each page in the browser and right clicking and viewing ```Page source``` to ensure code being rendered excludes the templating language

- **CSS:** style.css tested with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator)

- **Javascript:** scripts.js tested with [JSLint](https://jslint.com/)

- **Python:** Code tested with pylint:


<a name="manual"></a>

### Manual Testing


<a name="usertesting"></a>

### User story testing

Tested against [User Stories](#userstories)

| As a | I want to be able to | Achieved |
| --- | --- | --- |
| Shopper | View products | :thumbsup: |
| Shopper | View individual products | :thumbsup: |
| Shopper | Check out interesting new street art | :thumbsup: |
| Shopper | View my shopping bag | :thumbsup: |
| |
| Site user | Know what the site is about at first glance | :thumbsup: |
| Site user | Easily register an account | :thumbsup: |
| Site user | Easily login or out | :thumbsup: |
| Site user | Have a personal profile | :thumbsup: |
|    |
| Shopper | Search for a product by name or description | :thumbsup: |
| Shopper | Easily see what I have searched for | :thumbsup: | 
| Shopper | Select the quantity of items to buy | :thumbsup: |
| Shopper | View the items in my bag | :thumbsup: |
| Shopper | Adjust the quantity of items in my bag | :thumbsup: |
| Shopper | Remove items from my shopping bag | :thumbsup: |
| Shopper | Have the ability to order as a guest | :thumbsup: |
| Shopper | Easily enter payment information | :thumbsup: |
| Shopper | View an order confirmation post checkout | :thumbsup: |


<a name="further"></a>

### Further testing


<a name="screen"></a>

### Screen size Testing



### :arrow_up:[Top of page](#top)
---
<a name="deploy"></a>

## :computer: Deployment

### To deploy to Heroku:

- Sign in to [Heroku dashboard](https://dashboard.heroku.com/apps)
- Create a new app by clicking `Create new app` in the `New` dropdown box
- Choose a relevant and unique app name
- Add Heroku Postgres as an add-on
- In the Config Vars add the relevant variables for:
    - SECRET_KEY
    - STRIPE_PUBLIC_KEY
    - STRIPE_WH_KEY
    - DATABASE_URL
    - USE_AWS (set to True)
    - DISABLE_COLLECT_STATIC, set to 1 (In this case as I uploaded static and media files manually)
- Freeze the requirements in the terminal by typing
'pip3 freeze > requirements.txt'
- Create a Procfile and save the below code into item<br>
`web: gunicorn street_art_at_home.wsgi:application`
- To set the database so it works with Postgres comment out the current database settings and add the below code to settings.py<br>
``` python
DATABASES = {
    'default': dj_database_url.parse(database_url_from_heroku_config_vars)
    }
```
- Run migrations
- Create a superuser by typing
`python3 manage.py createsuperuser`
- Revert back to the original setup in settings.py
- Add the below code in an if statement<br>
``` python
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
- Add the app name to ALLOWED_HOSTS in settings.py
- To make it easier, set Heroku to deploy automatically when code is pushed to GitHub

### Amazon Web Services

- Go to [AWS](https://aws.amazon.com/)
- Search for S3 and create a new bucket, give this bucket the same name as the Heroku app
- Unblock public access and finish creating the bucket
- In the permissions tab, edit cross origin resource sharing (CORS) and paste the below in<br>
``` python
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- Select `Policy Generator` to create a new security Policy
- Select S3 Bucket Policy as the type of policy and add a * to principle
- Set the Action to Get Object and paste in the ARN (Amazon Resource Name)
- Click `Add Statement`, then `Generate Policy`
- Copy the policy and paste it into the bucket policy editor
- Make sure a * is added to the end of the `Resource` value to allow access to all resources in the bucket
- In the ACL (Access Control List), set list object permissions for everyone
- Open IAM (Identity and Access Management) and create a group giving it a name
- Go the the `Policies` tab and choose `Create Policy`
- Select `Import Managed Policy` from the JSON tab, search for S3 and import `S3 Full Access Policy`
- Back on S3, copy the ARN and paste this twice in to the Resource item. The second arn line should have a /* on the end like the below
`"arn:aws:s3:::bucket/*"`
- Click `Review Policy`, name it and give it a decription before clicking `Create Policy`
- Search for the policy created and click `Attach Policy`
- Then create a user from the `User` tab by clicking `Add User`
- Give the user a name and allow the user programmatic access
- Add the user to the group, click `end` until done 
- Download the CSV file which will contain the access keys, be sure to save the file as it can only be downloaded once
- For Django to connect to S3, install boto3 and django-storages
- Also add 'storages' to the installed apps in settings.py
- Add the 2 AWS keys to the config vars in the Heroku config vars
- Add the below if statement to settings.py to check that USE_AWS is set to true<br>
``` python
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'street-art-at-home'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```


### :arrow_up:[Top of page](#top)
---
<a name="issues"></a>

## :ant: Issues & bugs

### Closed issues

- I had issues in terms of the automatic upload of static and media files to AWS. To deal with this I opted for a manual upload to populate. In future, I would attempt to make this an automatic process.


### Open issues

- Styling of the Django admin page. I have not been able to correct this and the Django admin page is very basic in looks. The functionality is 100% present however and I took the decision to leave as is.

### [:arrow_up:Top of page](#top)
---
<a name="credits"></a>

## :clap: Credits & acknowledgements

- Template for footer taken from [colorlib.com](https://codepen.io/hasib_technobari/pen/QmNxwy) and style customised for own site

- As always, the advice and support from my mentor Rohit 



### :arrow_up:[Top of page](#top)
---
