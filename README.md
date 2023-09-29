<!-- Code for readme adapted from author's own project (Portfolio 2),
https://github.com/Boiann/budget-calculator -->

# CVEK ART GALLERY

Cvek Art Gallery is a Project 5 for Code Institute Full-stack development program: E-Commerce Applications. It is a B2C platform, gallery/store where the user can purchase painting/s, with added frame and discount options. Using mainly Django, a Python back-end development framework and Bootstrap, front-end (CSS) framework wired up to Stripe, this project was brought to life. Made with passion and meant to honor my father whose abilities, persistence and the thirst for learning keep inspiring. 

<!-- AmIResponsive img -->

Visit the live site [Here.](https://cvek-art-gallery-d4a224801c39.herokuapp.com/ "Link to Cvek Art Gallery")

---

## CONTENTS

* [Project Overview](#project-overview)
  * [Project Goals](#project-goals)

* [User Experience](#user-experience)
  * [User Expectations](#user-expectations)
  * [User Stories](#user-stories)

* [Business model](#business-model)
  * [Marketing](#marketing)

* [Design](#design)
  * [Color Scheme](#color-scheme)
  * [Imagery](#imagery)
  * [Structure](#structure)
  * [Database Design](#database-design)
  * [Wireframes](#wireframes)

* [Agile Project Management](#agile-project-management)

* [Features](#features)

* [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Programs Used](#programs-used)

* [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Code used and adapted](#code-used-and-adapted)
  * [Acknowledgments](#acknowledgments)

---

## **Project Overview**

Cvek Art Gallery was conceptualized a couple of months ago, even before Project 4 was. As the end Project and its requirements were known ahead of time, it was decided to honor Mr. Cvek's painting capabilities and their inherent beauty. It is a B2C (business-to-consumer) platform, gallery/store where the user can view all of the paintings currently for sale. As the paintings for sale are one of a kind, the quantity selector and model were replaced by an option to buy frame/s with the painting. 
Also, the discount on multiple purchases is a nice way of attracting new and keeping old customers. This project was realized using Django, Javascript, jQuery, Python, CSS3, Bootstap and HTML5, wired up to Stripe payment platform.

**Note for testing the checkout functionality:**

The site will not process an actual card payment and no charges will be collected through site and/or Stripe. Also, no orders will be fulfilled or delivered.
To keep your personal information secure, it is advised to use Stripe test Visa card:
* Card Number: 4242 4242 4242 4242
* MM/YY: Any future date in the format MM/YY
* CVC: Any 3 numbers
* ZIP: Any 5 numbers

* **HINT**: When Payment field is selected, just enter 424242... until the end!

### **Project Goals**

 * Develop CAG website using Django and Bootstrap frameworks, wire up to Stripe
 * Present the website in a clean and easy to understand manner
 * Keep good UX principles regarding layout/colors/interaction
 * Robust Python code without issues/bugs
 * Fully responsive, interactive and with feedbacks

[Back to top ⇧](#cvek-art-gallery)

---

## **User Experience**

### **User Expectations**

 - Able to quickly understand what the purpose of the site is
 - Intuitive navigation
 - Responsive across many devices and screen sizes
 - Able to find basic information
 - Find additional info if needed
 - Every interaction has feedback
 - User-friendly
 - See the exact cost of every item
 - Easy and secure checkout
 - Contacting the store through the website
 - See what discounts are applied

### **User Stories**

Many user stories were developed for the project using Agile development methodology, for the full list please see the [CAG Project.](https://github.com/users/Boiann/projects/12 "Link to Cvek Art Gallery Project") The following stories are selected from that project, and are the more important ones.

#### **First Time Visitor**
 * I can open the home page so that I can see what this website is about.
 * I can effectively explore this website so that I can access all the info I need.
 * I can see a list of paintings so that I can select one or more to purchase.
 * I can find out more about the artist so that I can find out more about him.
 * I can modify my shopping bag so that I can adjust my purchase.
 * I can see a notification upon successful modifying/removing so that I can know I'm doing things right.
 * I can connect with the store/business on Facebook so I can follow on any news/updates/special offers.

#### **Returning Customer**
 * I want to be able to register and log in/out without issues.
 * I want to get an email notification so that my registration is confirmed.
 * I can search or sort by category of paintings so that I can select one or more to purchase.
 * I can see if there is anything on special offer so that I can save some money.
 * I can remove paintings from my shopping bag so that I can adjust my purchase.
 * I can have personalized user profile so I can view my order history.
 * I can subscribe to the store newsletter so I can know about any news/updates/special offers.

#### **Website Admin/Owner**
* I can add/remove paintings from the store so I can remove sold out paintings and add new ones.
* I can modify paintings in the store so I can update them with the right details.
* I can see what the customer ordered, how much was paid, and was the discount applied.

[Back to top ⇧](#cvek-art-gallery)

---

## **Business Model**

This site follows a B2C (business-to-consumer) model, selling paintings with or without added extras (frames) directly to the customer. The customer can quickly make a purchase, there is no registration mandatory for checkout. There are multiple tiers of discounts available, for delivery, and for amount of paintings in the cart (buy 3, get €50 off, buy 6 get €100 off). The business is advertised on Facebook, where a real-life site can quickly gain traction and customer base. Primary target audience are customers looking for unique and homemade oil on canvas paintings. The site uses simple and intuitive design, good ux, sign-ups to the newsletter and contact through the site itself, potential deals and more to attract and expand its audience.

### **Marketing**

The site is connected to Facebook where business page was made. The [Facebook link](https://www.facebook.com/people/Cvek-Art-Gallery/61551953037626/) is not guaranteed to not be removed by the time this project is reviewed, and for that reason it is not included in the site footer FB link. FB page was captured in GIF format as proof:

<!-- FB GIF -->

The project also includes descriptive meta tags in base.html head, sitemap.xm and robots.txt to optimize SEO. Newsletter subscription is also supported via MailChimp.

[Back to top ⇧](#cvek-art-gallery)

---

## **Design**

### **Color Scheme**

The color scheme used in the project is not explicitly defined. Using Bootstrap CSS class selectors and templates taken from Boutique Ado project. If not for the background image, it would be dark/black text over white background. This is done on purpose to maintain site cleanliness. Color is added to confirm/cancel buttons in ux standard, red for cancel, green for confirm. Bootstrap toasts use color-coded messages too, blue for info, yellow for warning, red for danger and green for success.

### **Imagery**

All the images of paintings were taken in the home of Mr. Cvek with his blessing. He also approved their usage in this project. Only two images were produced explicitly for the purposes of the project, the logo and favicon. 

<!-- Logo img -->

The 'noimage' image, used for adding new painting to the store without actual painting image, was included even if it doesn't really make sense to submit a painting for sale without its image. It was kept in for testing purposes.

### **Structure**

  - CAG website is structured in a user-friendly and easy to navigate way.

  - *Home page:*

    - When the index first loads, the user is presented with page explaining the basic purpose of the site utilizing bootstrap carousel image change between three paintings. Each image has a 'shop now' button leading to all paintings for sale paginated page, and a short and strong message - 'Homemade oil paintings, self-taught artist, beautiful imagery.
    - The navigation bar presents the site name, logo, search field, account and basket icons, and selectors for all paintings, categories, subcategories, specials and about sections.
    - Right below the navbar there is an animated marquee banner that cycles special offers
    - The footer contains business email and physical address, popular categories, about and social media links, as well as newsletter subscription button that opens a subscription dedicated page
    - Using MVT-based framework (Model, View, Template) base template is created with head, navigation and footer being the same on all pages, adding specific page content to it.

  - *Navbar*
    
    - First navbar dropdown menu consists of sorting options for paintings, by year, price or category, and 'All Paintings' nav link
    - Second dropdown menu is for exploring Categories
    - Third dropdown is for Subcategories
    - Specials dropdown menu contains New Paintings, Deals, Clearance and 'All Specials' links
    - About dropdown leads to four separate pages; About the Artist, Contact Us, T&C's and Privacy
    - MY Account link and Font Awesome icon is for handling user's login, logout, registering, My Profile page, and admin's access and Paintings Management page 

  - *Footer:*
    - The footer contains business email and physical address, popular categories, about and social media links (opening in separate tabs)
    - At the top of the footer area there is a newsletter subscription button that opens a subscription dedicated page
    - Footer also contains copyright for both this project and paintings property rights.

  - *Registerig, logging in/out:*  
    - First time/unregistered user can successfully make a purchase without registering
    - First time user can register on the register page. The page contains redirect links to login if the user is mistakenly on register page, and link to login page if the user is registered already
    - Upon registering, the 'Register' link is replaced by 'Logout' link, allowing the user to sign out from the site.
    - If the registered user makes a purchase, the personal and delivery details as well as the past order and it's details are visible on 'My Profile' link in the My Account nav dropdown 
    - Logged in admin user will also have additional links in the navbar - 'Paintings management,' for adding paintings for sale and 'Admin Page' which opens admin site in a separate tab.
    - When logging in the user is brought to the index page.
    - When logging out, the user is asked 'Are you sure' before signing out.
    - When signed out, the user is brought to the index page.

  - *Paintings page (this includes all the categoties, subcategories and sorting options):*
    - The user is presented with a paginated view of paintings for sale.
    - Each painting card consists of image, price, category name and year it was made.
    - If the user clicks on a painting the detail of the painting is presented

  - *Painting-detail page:*
    - This page shows larger image of the Painting, as well as it's full name, size, price, year of production, add to cart button and frame option dropdown button
    - The customer can choose to add a standard (+€50) or Premium (+€100) frame, which affects the price at the checkout
    - If the painting is in 'clearance' subcategory, no frame options are available

  - *Cart page*
    - Consists of the list of paintings user has placed in the cart, current selected frame, with Subtotal calculations on the right depending on if the user wishes to add/remove/change the frame selected
    - There is an remove button so the user can remove paintings from the cart easily
    - If the user is under the free delivery threshold, the message is displayed below the grand total saying that the user can spend just (amount) to get free delivery 
    - Cart total is calculated excluding delivery
    - If user has three or more paintings in the cart, a message appears at the top of the page informing them of their €50 discount
    - If user has six or more paintings in the cart, a message appears at the top of the page informing them of their €100 discount

  - *Checkout page*
    - Checkout page consists of the painting image, title, frame selected and full total of the painting
    - The form for delivery details can be found on the left, after successful purchase the user is presented with checkout success page, holding all of the info from the purchase, painting/s, delivery and personal details, and the email confirmation sent message
    - Order is saved to 'My Profile' page if the user is registered with the site

  - *About pages*
    - About the Artist page is short info and a few images about the author of the paintings
    - Contact Us page contains a form for contacting the business, user is getting a feedback email upon successful form submission, and is redirected back to index page
    - T&C's page contains the site's Terms and conditions
    - Privacy page is where the user can find the site's privacy policy

  - *Error pages*
    - Two error pages are supported, 404 (page not found) and 500 (internal server error), both with buttons that guide the user back to the home page. 

### **Database Design**

Multiple apps and classes/models were created for the project, each one supporting the full site functionality.
 - Cart app - no classes and models, primarily focused on cart calculations

 - Checkout app - Order and OrderLineItem models

   - Order model:

|Name|Database Key|Field Type|Validation|
|---|---|---|---|
|order_number|order_number|CharField|max_length=32, null=False, editable=False|
|user_profile|user_profile|ForeignKey|'UserProfile', null=True, blank=True, on_delete=models.SET_NULL, related_name='orders'|
|full_name|full_name|CharField|max_length=50, null=False, blank=False|
|email|email|EmailField|max_length=254, null=False, blank=False|
|phone_number|phone_number|CharField|max_length=20, null=False, blank=False|
|country|country|CountryField|blank_label='Country *', null=False, blank=False|
|postcode|postcode|CharField|max_length=20, null=True, blank=True|
|town_or_city|town_or_city|CharField|max_length=40, null=False, blank=False|
|street_address1|street_address1|CharField|max_length=80, null=False, blank=False|
|street_address2|street_address2|CharField|max_length=80, null=True, blank=True|
|county|county|CharField|max_length=80, null=True, blank=True|
|date|date|DateTimeField|auto_now_add=True|
|delivery_cost|delivery_cost|DecimalField|max_digits=6, decimal_places=2, null=False, default=0|
|order_total|order_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0|
|grand_total|grand_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0|
|discount_applied|discount_applied|BooleanField|default=False|
|original_cart|original_cart|TextField|null=False, blank=False, default=''|
|stripe_pid|stripe_pid|CharField|max_length=254, null=False, blank=False, default=''|

   - OrderLineItem model

|Name|Database Key|Field Type|Validation|
|---|---|---|---|
|order|order|ForeignKey|'Order', null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'|
|painting|painting|ForeignKey|'Painting', null=False, blank=False, on_delete=models.CASCADE|
|frame|frame|CharField|max_length=20, null=True, blank=True|
|lineitem_total|lineitem_total|DecimalField|max_digits=6, decimal_places=2, null=False, blank=False, editable=False|

 - Cvek Art Gallery - main/root app
 - Home app - focused on the index page display and function
 - Paintings app - holding Category, SubCategory and Painting classes

   - Category model

| Name          | Database Key  | Field Type    | Validation     |
| ------------- | ------------- | ------------- | -------------- |
| name          | name          | CharField     | max_length=254 |
| friendly_name | friendly_name | CharField     | max_length=254, null=True, blank=True |

   - SubCategory model

| Name          | Database Key  | Field Type    | Validation     |
| ------------- | ------------- | ------------- | -------------- |
| category      | category      | ForeignKey    | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| name          | name          | CharField     | max_length=254 |
| friendly_name | friendly_name | CharField     | max_length=254, null=True, blank=True |

   - Painting model

| Name        | Database Key  | Field Type        | Validation                |
| ----------- | ------------- | ----------------- | ------------------------- |
| category    | category      | ForeignKey        | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| subcategory | subcategory   | ManyToManyField   | 'SubCategory', blank=True |
| sku         | sku           | CharField         | max_length=254, null=True, blank=True |
| name        | name          | CharField         | max_length=254            |
| description | description   | TextField         |                           |
| price       | price         | DecimalField      | max_digits=6, decimal_places=2 |
| year        | year          | DecimalField      | max_digits=4, decimal_places=0, null=True, blank=True |
| size        | size          | CharField         | max_length=254, null=True, blank=True |
| image       | image         | ImageField        | null=True, blank=True     |

 - Profiles app - where UserProfile model is defined

   - UserProfile model:

| Name                   | Database Key            | Field Type        | Validation                  |
| ---------------------- | ----------------------- | ----------------- | --------------------------- |
| user                   | user                    | OneToOneField     | 'User', on_delete=models.CASCADE |
| default_phone_number   | default_phone_number    | CharField         | max_length=20, null=True, blank=True |
| default_street_address1| default_street_address1 | CharField         | max_length=80, null=True, blank=True |
| default_street_address2| default_street_address2 | CharField         | max_length=80, null=True, blank=True |
| default_town_or_city   | default_town_or_city    | CharField         | max_length=40, null=True, blank=True |
| default_county         | default_county          | CharField         | max_length=80, null=True, blank=True |
| default_postcode       | default_postcode        | CharField         | max_length=20, null=True, blank=True |
| default_country        | default_country         | CountryField      | blank_label='Country', null=True, blank=True |

 - Support app - Contact class used for contacting the store

   - Contact model

| Name             | Database Key     | Field Type    | Validation                                 |
| ---------------- | ---------------- | ------------- | ------------------------------------------ |
| contact_reason   | contact_reason   | CharField     | max_length=24, choices=CONTACT_REASONS    |
| name             | name             | CharField     | max_length=100                             |
| email            | email            | EmailField    | max_length=100                             |
| phone            | phone            | CharField     | max_length=20, blank=True, null=True       |
| message          | message          | TextField     | max_length=1000                            |
| date_submitted   | date_submitted   | DateTimeField | auto_now_add=True                         |


### **Wireframes**

<!-- Description and images -->

[Back to top ⇧](#cvek-art-gallery)

---

## **Agile Project Management**

[Back to top ⇧](#cvek-art-gallery)

---

## **Features**

<!-- Features images/gifs -->

## **Future Implementations**

<!-- Description -->

[Back to top ⇧](#cvek-art-gallery)

---

## **Technologies Used**

### **Languages Used**

### **Programs Used**

[Back to top ⇧](#cvek-art-gallery)

---

## **Deployment**

[Back to top ⇧](#cvek-art-gallery)

---

## **Testing**

**Testing information can be found in a separate testing file [TESTING.md](/TESTING.md).**

[Back to top ⇧](#cvek-art-gallery)

---

## **Credits**

### **Code used and adapted**

### **Websites visited to gather knowledge**

###  **Acknowledgments**

[Back to top ⇧](#cvek-art-gallery)

***