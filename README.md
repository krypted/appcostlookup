# appcostlookup
Basic lookup of app metadata in iTunes App Store


# Requirements
1. Ofcourse, you need to have Python installed. And specifically python3.
2. 2 packages are required: BeautifulSoup, Requests.
3. To install those packages with the command `pip install beautifulsoup4` and `pip install requests`


# How it works?
appcostlookup will read all of the app atom_ids from a csv file and create a new column with the cost of the app.
1. Create a file called `input.csv` with the atom_id of apps as the first column. 
2. Run the script with the input.csv in the same working directory (or provide a URI in the script or as part of a microservice) .
3. After looking up costs, it will export the dataset into a new column in the same CSV.


# To-do
1. Perform a uniq operation to deduplicate lookups
2. Move script to a lambda
