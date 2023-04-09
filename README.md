<h1>backend app #smartphone_proj</h1>


<h2>Service part</h2>

admin/

<h2>Api for phones</h2>


api/phones/func/?search={name} - accepts GET. get - searches by the name field, gives an approximate list of records

api/phones/func/?search={name}&corpus={corpus} - accepts GET. get - searches by the field name and corpus, gives an approximate list of records (you can combine the request)

api/phones/func/?brand={brand}&corpus={corpus}&yadra={yadra}&front_kamera={front_kamera}&giga_vstoeno={giga_vstoeno}&giga_operate={giga_operate}&accumulator={accumulator} - accepts GET. get - searches the corpus, Brand, Yadra, Front kamera, Giga vstoeno, Giga operate, Accumulator fields and gives an approximate list of records, NOTE the request must be clearly written

api/phones/func/?brand={brand,brand,brand...} - accepts GET. get - searches for the brand field, but also takes all brands, displays a list of records that are included in the brand list

api/phones/func/{id}/ accepts GET,PUT,DELETE. get - getting one record put - changing data except slug, delete - deleting one record

api/phone/{slug}/ accepts GET. get - displays a record by slug but also displays a series of records similar in brand field and similar records from airpods


<h2>Api for airpods</h2>


api/phone/{slug}/ accepts GET. get - displays a record by slug but also displays a series of records similar in brand field and similar records from airpods

api/airpods/func/ accepts GET, POST. get - get a list of all phones and etc... post - create a new post

api/airpods/func/{id}/ accepts GET,PUT,DELETE. get - getting one record put - changing data except slug, delete - deleting one record


<h2>Api for accounts</h2>


api/accounts/user/ accepts GET. get - checks if the user has a token

api/accounts/login/ accepts POST. post - requires a username, password field, after which you can get a token

api/accounts/logout/ accepts POST. post - requires a token after which the token is deleted from the user

api/accounts/logoutALL/ accepts POST. post - requires a token after which ALL tokens are deleted from the user

api/accounts/create/ - accepts POST. POST require fields username, email during filling, an account is created without confirmation initially and the user will receive a link to confirm the account (where a password is also generated) and he will go to {redirect url} after which the user needs to authorize his created account use api/accounts/login/

reset/ - accepts POST. POST require fields new_password,check_password,your_email, Google mail will receive a confirmation message to change the password and user will go to {redirect url} after which the user needs to authorize his created account use api/accounts/login/

<h2>Api for comments</h2>


api/comments/createPho/ - accepts POST. post - takes phone_id, rate, comment fields

api/comments/operatePho/{id}/ - accepts GET,PUT,DELETE. get - Lists the entries associated with the phone_id. put - requires authentication and that the user be the owner of this comment, requires the comments field, rate after which the comment will change, delete - the same as put but without input fields

api/comments/createAir/ - accepts POST. post - takes the airpod_id, rate, comment fields

api/comments/operateAir/{id}/ - accepts GET,PUT,DELETE. get - Lists the entries associated with the airpod_id. put - requires authentication and that the user be the owner of this comment, requires the comments field, rate after which the comment will change, delete - the same as put but without input fields


<h2>Api for basket of goods + payment</h2>


api/comments/add_product/ - accepts POST. post - takes the fields group_product(1-phones,2-headphones), product_id also requires a user token/session, and there is an optional count field, if it is not specified count=1, after which the product will be added to the customer's cart with additional fields. Note: it will be impossible to make a request again, the slug field cannot be repeated.

api/comments/operate_product/{id}/ - accepts GET, DELETE, PUT. get - takes the user's id and compares it with the user's token, after which a list of goods taken by the user is displayed, delete - takes the object id and the user's token, then deletes this record, put - takes the object's id and the user's token, requires the count field, after which the product will be changed.

api/comments/get_traffic/ - accepts PATCH. patch - takes the user's token, after which it displays a list of products that went through a successful transaction

create-checkout-session/<id>/ - accepts POST. post - takes the user id (works for all users) and generates a unique session (link) that redirects the user to the stripe site where the payment takes place, after the user has entered his data (test: 4242 4242 4242 4242.11 / 23.123 ) a payment operation occurs during which all goods are paid for and redirects the user {redirect_url} and in case of cancellation of the purchase {redirect_url} , after the payment is processed, the user receives an email message

