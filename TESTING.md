<!-- Code for readme adapted from author's own project (Portfolio 1),
https://github.com/Boiann/boudoir-studio -->

# **CVEK ART GALLERY - Testing** 

[Main README.md file](/README.md)

Visit the live site - [Cvek Art Gallery](https://cvek-art-gallery-d4a224801c39.herokuapp.com/ "Link to Cvek Art Gallery")

View GitHub [Repository](https://github.com/Boiann/cvek-art-gallery)

---
## **Contents**
* [Automated Testing](#automated-testing)
  * [W3C HTML Validator](#w3c-html-validator)
  * [W3C CSS Validator](#w3c-css-validator)
  * [JSHINT Javascript Validator](#jshint-javascript-validator)
  * [CI Python Linter](#ci-python-linter)
  * [Lighthouse](#lighthouse)

* [Accessibility](#accessibility) 
  * [WAVE WebAim](#wave-webaim) 

* [Manual Testing](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
    * [Features](#features)
    * [Responsiveness](#responsiveness)

* [Bugs](#bugs)
  * [Known Bugs](#known-bugs)
  * [Solved Bugs](#solved-bugs)

* [Browser Compatibility](#browser-compatibility)      

---

## Automated Testing

### **W3C HTML Validator**

The [HTML W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) was used to validate the HTML code used, showing no errors.

<details>
<summary>HTML Validation:</summary>

 - Index
 <br>

![Index](readme_assets/images/tests/html/html-index.png)

 - Paintings
 <br>

![Paintings](readme_assets/images/tests/html/html-paintings.png)

 - Painting detail
 <br>

![Painting detail](readme_assets/images/tests/html/html-painting-detail.png)

 - Cart
 <br>

![Cart](readme_assets/images/tests/html/html-cart.png)

 - Checkout
 <br>

![Checkout](readme_assets/images/tests/html/html-checkout.png)

 - Checkout success
 <br>

![Checkout success](readme_assets/images/tests/html/html-checkout-success.png)

  - Newsletter
 <br>

![Newsletter](readme_assets/images/tests/html/html-newsletter.png)

  - About the Artist
 <br>

![About the Artist](readme_assets/images/tests/html/html-about.png)

  - Contact Us
 <br>

![Contact Us](readme_assets/images/tests/html/html-contact.png)

  - T&C's
 <br>

![T&C's](readme_assets/images/tests/html/html-t&c.png)

 - Privacy
 <br>

![Privacy](readme_assets/images/tests/html/html-privacy.png)

 - Log in
 <br>

![Log in](readme_assets/images/tests/html/html-login.png)

 - Log out
 <br>

![Log out](readme_assets/images/tests/html/html-logout.png)

 - Register
 <br>

![Register](readme_assets/images/tests/html/html-register.png)

 - My Account
 <br>

![My Account](readme_assets/images/tests/html/html-profile.png)

 - Add Painting
 <br>

![Add Painting](readme_assets/images/tests/html/html-add-painting.png)

</details>

---

### **W3C CSS Validator**

The [CSS Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) was used to validate the CSS code used, showing no errors.

<details>
<summary>CSS Validation:</summary>

![CSS Validator](readme_assets/images/tests/rest/css.png)

</details>

---

### **JSHINT Javascript Validator**

The [JsHint](https://jshint.com/) was used to validate the Javascript code used, showing no errors.

<details>
<summary>Javascript Validation:</summary>

![Javascript Validator](readme_assets/gifs/general/js-validation.gif)

</details>

---

### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code used, showing no errors.

---

#### Cart App

<details>
<summary>Cart App Validation:</summary>

 - contexts.py
 <br>

![contexts](readme_assets/images/tests/python/cart/contexts.png)

 - urls.py
 <br>

![urls](readme_assets/images/tests/python/cart/urls.png)

 - views.py
 <br>

![views](readme_assets/images/tests/python/cart/views.png)

</details>

---

#### Checkout App

<details>
<summary>Checkout App Validation:</summary>

 - admin.py
 <br>

![admin](readme_assets/images/tests/python/checkout/admin.png)

 - forms.py
 <br>

![forms](readme_assets/images/tests/python/checkout/forms.png)

 - models.py
 <br>

![models](readme_assets/images/tests/python/checkout/models.png)

 - signals.py
 <br>

![signals](readme_assets/images/tests/python/checkout/signals.png)

 - urls.py
 <br>

![urls](readme_assets/images/tests/python/checkout/urls.png)

 - views.py
 <br>

![views](readme_assets/images/tests/python/checkout/views.png)

 - webhook_handler.py
 <br>

![webhook_handler](readme_assets/images/tests/python/checkout/wh-handler.png)

 - webhooks.py
 <br>

![webhooks](readme_assets/images/tests/python/checkout/webhooks.png)

</details>

---

#### Root App - cvek_art_gallery

<details>
<summary>Root App Validation:</summary>

 - urls.py
 <br>

![urls](readme_assets/images/tests/python/root/urls.png)

 - views.py
 <br>

![views](readme_assets/images/tests/python/root/views.png)

</details>

---

#### Home App

<details>
<summary>Home App Validation:</summary>

 - urls.py
 <br>

![urls](readme_assets/images/tests/python/home/urls.png)

 - views.py
 <br>

![views](readme_assets/images/tests/python/home/views.png)

</details>

---

#### Paintings App

<details>
<summary>Paintings App Validation:</summary>

 - admin.py
 <br>

![admin](readme_assets/images/tests/python/paintings/admin.png)

 - forms.py
 <br>

![forms](readme_assets/images/tests/python/paintings/forms.png)

 - models.py
 <br>

![models](readme_assets/images/tests/python/paintings/models.png)

 - urls.py
 <br>

![urls](readme_assets/images/tests/python/paintings/urls.png)

 - views.py
 <br>

![views](readme_assets/images/tests/python/paintings/views.png)

 - widgets.py
 <br>

![widgets](readme_assets/images/tests/python/paintings/widgets.png)

</details>

---

#### Profiles App

<details>
<summary>Profiles App Validation:</summary>

 - forms.py
 <br>

![forms](readme_assets/images/tests/python/profiles/forms.png)

 - models.py
 <br>

![models](readme_assets/images/tests/python/profiles/models.png)

 - urls.py
 <br>

![urls](readme_assets/images/tests/python/profiles/urls.png)

 - views.py
 <br>

![views](readme_assets/images/tests/python/profiles/views.png)

</details>

---

#### Support App

<details>
<summary>Support App Validation:</summary>

 - forms.py
 <br>

![forms](readme_assets/images/tests/python/support/forms.png)

 - models.py
 <br>

![models](readme_assets/images/tests/python/support/models.png)

 - urls.py
 <br>

![urls](readme_assets/images/tests/python/support/urls.png)

 - views.py
 <br>

![views](readme_assets/images/tests/python/support/views.png)

</details>

---

### **Lighthouse**

[LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) was used for testing performance.

#### Desktop:

<details>
<summary>Desktop Lighthouse Validation:</summary>

 - Index
 <br>

![Index](readme_assets/images/tests/lighthouse/desktop/index.png)

 - Paintings
 <br>

![Paintings](readme_assets/images/tests/lighthouse/desktop/paintings.png)

 - Painting detail
 <br>

![Painting detail](readme_assets/images/tests/lighthouse/desktop/painting-detail.png)

 - Cart
 <br>

![Cart](readme_assets/images/tests/lighthouse/desktop/cart.png)

 - Checkout
 <br>

![Checkout](readme_assets/images/tests/lighthouse/desktop/checkout.png)

 - Checkout success
 <br>

![Checkout success](readme_assets/images/tests/lighthouse/desktop/checkout-success.png)

  - Newsletter
 <br>

![Newsletter](readme_assets/images/tests/lighthouse/desktop/newsletter.png)

  - About the Artist
 <br>

![About the Artist](readme_assets/images/tests/lighthouse/desktop/about.png)

  - Contact Us
 <br>

![Contact Us](readme_assets/images/tests/lighthouse/desktop/contact.png)

  - T&C's
 <br>

![T&C's](readme_assets/images/tests/lighthouse/desktop/t&c.png)

 - Privacy
 <br>

![Privacy](readme_assets/images/tests/lighthouse/desktop/privacy.png)

 - Log in
 <br>

![Log in](readme_assets/images/tests/lighthouse/desktop/login.png)

 - Log out
 <br>

![Log out](readme_assets/images/tests/lighthouse/desktop/logout.png)

 - Register
 <br>

![Register](readme_assets/images/tests/lighthouse/desktop/register.png)

 - My Account
 <br>

![My Account](readme_assets/images/tests/lighthouse/desktop/my-account.png)

 - Add Painting
 <br>

![Add Painting](readme_assets/images/tests/lighthouse/desktop/add-painting.png)

 - Edit Painting
 <br>

![Edit Painting](readme_assets/images/tests/lighthouse/desktop/edit-painting.png)

</details>

---

#### Mobile:

<details>
<summary>Mobile Lighthouse Validation:</summary>

 - Index
 <br>

![Index](readme_assets/images/tests/lighthouse/mobile/index.png)

 - Paintings
 <br>

![Paintings](readme_assets/images/tests/lighthouse/mobile/paintings.png)

 - Painting detail
 <br>

![Painting detail](readme_assets/images/tests/lighthouse/mobile/painting-detail.png)

 - Cart
 <br>

![Cart](readme_assets/images/tests/lighthouse/mobile/cart.png)

 - Checkout
 <br>

![Checkout](readme_assets/images/tests/lighthouse/mobile/checkout.png)

 - Checkout success
 <br>

![Checkout success](readme_assets/images/tests/lighthouse/mobile/checkout-success.png)

  - Newsletter
 <br>

![Newsletter](readme_assets/images/tests/lighthouse/mobile/newsletter.png)

  - About the Artist
 <br>

![About the Artist](readme_assets/images/tests/lighthouse/mobile/about.png)

  - Contact Us
 <br>

![Contact Us](readme_assets/images/tests/lighthouse/mobile/contact.png)

  - T&C's
 <br>

![T&C's](readme_assets/images/tests/lighthouse/mobile/t&c.png)

 - Privacy
 <br>

![Privacy](readme_assets/images/tests/lighthouse/mobile/privacy.png)

 - Log in
 <br>

![Log in](readme_assets/images/tests/lighthouse/mobile/login.png)

 - Log out
 <br>

![Log out](readme_assets/images/tests/lighthouse/mobile/logout.png)

 - Register
 <br>

![Register](readme_assets/images/tests/lighthouse/mobile/register.png)

 - My Account
 <br>

![My Account](readme_assets/images/tests/lighthouse/mobile/my-account.png)

 - Add Painting
 <br>

![Add Painting](readme_assets/images/tests/lighthouse/mobile/add-painting.png)

 - Edit Painting
 <br>

![Edit Painting](readme_assets/images/tests/lighthouse/mobile/edit-painting.png)

</details>

---

[Back to top ⇧](#cvek-art-gallery---testing)

---

## **Accessibility**

### **WAVE WebAim**

[W.A.V.E.](https://wave.webaim.org/) was used to test for accessibility, showing no errors. Unfortunately cart, checkout and pages requiring login could not be tested on WebAim.

<details>
<summary>WAVE WebAim Validation:</summary>

 - Index
 <br>

![Index](readme_assets/images/tests/wave/index.png)

 - Paintings
 <br>

![Paintings](readme_assets/images/tests/wave/paintings.png)

 - Painting detail
 <br>

![Painting detail](readme_assets/images/tests/wave/painting-detail.png)

  - About the Artist
 <br>

![About the Artist](readme_assets/images/tests/wave/about.png)

  - Contact Us
 <br>

![Contact](readme_assets/images/tests/wave/contact.png)

  - T&C's
 <br>

![T&C's](readme_assets/images/tests/wave/t&c.png)

 - Privacy
 <br>

![Privacy](readme_assets/images/tests/wave/privacy.png)

 - Log in
 <br>

![Log in](readme_assets/images/tests/wave/login.png)

 - Register
 <br>

![Register](readme_assets/images/tests/wave/register.png)

</details>

---

[Back to top ⇧](#cvek-art-gallery---testing)

---

## **Manual Testing**

### **Testing User Stories**

#### **First Time Visitor**

| User Story | Pass/Fail |
|------------|----------|
| I can open the home page so that I can see what this website is about. | PASS |
| I can effectively explore this website so that I can access all the info I need. | PASS |
| I can see a list of paintings so that I can select one or more to purchase. | PASS |
| I can find out more about the artist so that I can find out more about him. | PASS |
| I can modify my shopping bag so that I can adjust my purchase. | PASS |
| I can see a notification upon successful modifying/removing so that I can know I'm doing things right. | PASS |
| I can connect with the store/business on Facebook so I can follow on any news/updates/special offers. | PASS |

#### **Returning Customer**

| User Story | Pass/Fail |
|------------|----------|
| I want to be able to register and log in/out without issues. | PASS |
| I want to get an email notification so that my registration is confirmed. | PASS |
| I can search or sort by category of paintings so that I can select one or more to purchase. | PASS |
| I can see if there is anything on special offer so that I can save some money. | PASS |
| I can remove paintings from my shopping bag so that I can adjust my purchase. | PASS |
| I can have personalized user profile so I can view my order history. | PASS |
| I can subscribe to the store newsletter so I can know about any news/updates/special offers. | PASS |

#### **Website Admin/Owner**

| User Story | Pass/Fail |
|------------|----------|
| I can add/remove paintings from the store so I can remove sold out paintings and add new ones. | PASS |
| I can modify paintings in the store so I can update them with the right details. | PASS |
| I can see what the customer ordered, how much was paid, and was the discount applied. | PASS |

[Back to top ⇧](#cvek-art-gallery---testing)

### **Full Testing**

#### **Features**

### **Index**

<details>
<summary>Index page image carousel and shop now button opening paintings for sale, animated marquee, logo and title return to index working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Index page dropdown menus opening respective pages/selections working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Search funtion returning relevant paintings, returning category/subcategory, nothing found result working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Subscription button opening subscription page working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Footer nav links opening new page working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Footer social media links open in a new tab working</summary>

<!-- GIF --> 
</details>

### **Account**

<details>
<summary>My Account dropdown links, register and log in pages with reverse links working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Register page email required warning, password not matching warning, user already registered warning working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Register page check email and validation working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Successful sign-in success toast message, 3 sec delay before disappearing working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Logging out 'are you sure' check and success toast message working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Password reset functionality, email check working</summary>

<!-- GIF --> 
</details>

<details>
<summary>My Account page for details after user is logged in working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin links in 'My Account' working</summary>

<!-- GIF --> 
</details>

### **Paintings**

<details>
<summary>All Paintings dropdown returns selected sorting working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Paintings paginated view, sorting options and smooth return to top button working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Paintings having in a category can have subcategory and return in the selected category working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Painting detail view, info and frame selector working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Painting in 'Clearance' subcat has no frames available, 20% discount working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin painting detail view, edit and delete buttons visible, warning modals working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin 'Product Management' link and adding new painting, no image working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin 'Product Management' link and adding new painting, with image working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin edit painting page modal and success message/s working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin delete painting page modal and success message working</summary>

<!-- GIF --> 
</details>

### **Cart**

<details>
<summary>Add to cart success message and basket total updating, mini-view of cart with delivery warning and cart info working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Add to cart success message and mini-view of cart with frame info and over 3 paintings in the cart message working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Add to cart button with different frame selected updates the basket total working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Cart page with paintings info, grand total calculation with delivery working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Cart page with paintings info, grand total calculation with 3 paintings discount working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Cart page with paintings info, grand total calculation with 6 paintings discount working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Cart page with paintings info, update/change frame option, delete painting from cart working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Cart page with paintings info, 'clearance' painting info and no frames options working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Keep shopping button lists all paintings working</summary>

<!-- GIF --> 
</details>

### **Checkout**

<details>
<summary>Checkout page and order summary with relevant info about paintings to be purchased, discount visible working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Adjust cart button returns to current cart working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Order form not working without inputs working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Successful purchase of unregistered user, email check working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Successful purchase of registered user, email check working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Successful purchase of registered user, order and details saved to 'My Profile' page working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Successful purchase positive results from Stripe webhooks working</summary>

<!-- GIF --> 
</details>

### **Other**

<details>
<summary>Newsletter link opening subscribe page, thank you msg, already subscribed msg working</summary>

<!-- GIF --> 
</details>

<details>
<summary>About the Artist page working</summary>

<!-- GIF --> 
</details>

<details>
<summary>T&C's page working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Privacy page working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Contact us page, form inputs required, success redirect to index and email check working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Error 400 page working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Error 500 page working</summary>

<!-- GIF --> 
</details>

### **Admin page**

<details>
<summary>Admin can view details of orders working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin can edit/delete details of orders and users working</summary>

<!-- GIF --> 
</details>

<details>
<summary>Admin can create new painting for sale on admin page working</summary>

<!-- GIF --> 
</details>

[Back to top ⇧](#cvek-art-gallery---testing)

#### **Responsiveness**

Responsiveness for the website was thoroughly tested for devices up to 320px wide using [Chrome Del Tools](https://developer.chrome.com/docs/devtools/).

<details>
<summary>Responsiveness test</summary>

![Responsiveness test](readme_assets/gifs/general/responsive-test.gif)
</details>


[Back to top ⇧](#cvek-art-gallery---testing)

---

## **Bugs**

### **Known Bugs**

* No known bugs present in the project (disclaimer; that doesn't mean there are none) at the time of writing this readme/testing.

### **Solved Bugs**

There were many 'small' bugs that had to be dealt with during the development of the project. Most of them were squashed by doing a quick [Google](https://google.com/ "Google home page") search and using [Stack Overflow](https://stackoverflow.com/ "Stack Overflow home page") to find relevant solutions.

Two of the biggest bugs were with Stripe webhooks and in later development, connection to AWS. The webhook bug is documented through GitHub Issues, the AWS one was not unfortunately, mainly because it caused quite a bit of panic being so close to submission date.

- Image format not recognized - [BUG NO. 1](https://github.com/Boiann/cvek-art-gallery/issues/83).

- Implementing Subcategories into the project proved to be bit more difficult than it seemed but it worked out in the end. The remaining issue that was subsequently removed from the project was to get the current subcategory selected display as a nav-link below the navbar. The same implementation worked for categories, but for subcategories it displayed either all of the subcategories, or none at all. A lot of effort was put into this trying to solve it but due to the project deadline it was decided to leave it out, along with current category nav link as not to present links for categories but not for subcategories.

- First major bug was encountered while implementing Stripe and its webhooks. It took multiple days and tries for this to be solved, and it took away time from further development. The code was updated and reworked multiple times because there was lack of attention to details and testing scope on the developer's part. That bug lead directly to other one with the database. After overloading the code with `print()` statements, it was fixed. More about this bug in [BUG NO. 2](https://github.com/Boiann/cvek-art-gallery/issues/93).

- Forcing sku as unique identifier instead of painting_id was a mistake in retrospect, this caused additional time spent when reworking the code to use painting_id. This change necessity became apparent when trying to implement adding new paintings as admin. When using SKU-s, when SKU field was left empty when submitting new painting, nothing worked because SKU was missing and not automatically generated, and painting_id is.

- Search functionality was not working as it should, returning nothing if searched term was category/subcategory, which was solved and fixed quickly.

- Connecting the deployed Heroku site with AWS was, in short, a nightmare causing actual physical consequences. Brought on by, again, lack of attention to details. This caused so much upset that it was not documented, and by the time it was fixed it was decided it will be talked about in this section. This was stemming from the fact that a similar issue actually happened, and it was not considered to be possible again. And the fact that mentor and tutors were unable to help with the issue.
  - AWS bucket creation and wiring-up steps were followed diligently, but media files were not showing up no matter what.
  - A lot of trial and unfortunate errors were made trying to fix this, reflected in the number of commits submitted on this issue (form 'AWS Deployment' to 'Fix favicon img path, delete previous loadstatic files')
  - After seeking help with the images not loading, it was realized what the mistake was, not using template tags for logo. The paintings images not showing up was still an issue
  - Looking up on Slack, Stack-Overflow, Google, asking the mentor and tutors did not help
  - It was assumed the issue was in `DISABLE_COLLECTSTATIC` config var in Heroku, and that it somehow didn't connect/wire up with AWS
  - Slack community members suggested that `DISABLE_COLLECTSTATIC` should actually NOT be removed for the first time deployment connected with AWS, this was later looked into and the issue is actually having the debug mode set to true, and that was creating issues for some people
  - Trying to run collectstatic and 'fixing' static settings in settings.py only made things worse, lack of experience made it worse still
  - Finally, the mistake was caught - because of multiple projects in GitPod workspace each project had it's own `DATABSE_URL`, renamed to `DATABSE_URL_CAG` for this project. This was an issue before with Stripe, because `STRIPE_WH_SECRET` set to general user scope (Boiann/*) was returning webhooks from both Boutique Ado + CAG. This was caught early, fixed quickly, and promise was made to oneself - 'Don't do this again'. But it did happen again, because database Heroku Config var was using `DATABSE_URL`. Changing that config var to `DATABSE_URL_CAG` solved issues with media files.

 - Sitemap bug - when sitemap was created for the first time, it was over 2500 lines long. At first, this was thought to be an issue with missing robots.txt file. After that was added, the sitemap still returned very large. Other projects were tested to see their sitemap scope, all returned ok. After Google, Slack and Stack Overflow check, tutoring was contacted, yielding no clear instruction/advice. Upon closer examination, it was noticed that add/edit/delete painting links were crawled, which only a superuser can do. The issue was that the html presented no edit/delete buttons for regular user (superuser check) but the buttons were still present in the hidden modal. Adding superuser check within the modal itself solved this issue and returned sitemap of normal size. 

[Back to top ⇧](#cvek-art-gallery---testing)

---

## **Browser compatibility**

The website was tested on the following browsers with no issues found: Google Chrome, Mozilla Firefox, Microsoft Edge and Opera Browser.

 - Browser Compatibility image:
 <br>

 ![Browser Compatibility](readme_assets/images/general/browser-compatibility.png)

---

[Back to top ⇧](#cvek-art-gallery---testing)