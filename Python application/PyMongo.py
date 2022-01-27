import pymongo
import pandas as pd
from datetime import datetime

##### Connect to MongoClient #####
client = pymongo.MongoClient('mongodb://localhost:27017')

##### Get Mongo Database #####
database = client.Books
collection = database.BookDetail


##### Simple Search (Assign to SEARCH button) #####
# Example: {"title": "java programming"} will display title with either "java" or "programming" #
def simple_search(text):
    # define variable
    if "()" not in text:
        if "(" or ")" in text:
            new_text = ""
            for i in range(len(text)):
                if text[i] == "(" or text[i] == ")":
                    continue
                else:
                    new_text += text[i]
            search_title = new_text
        else:
            search_title = text
    else:
        search_title = text

    
    # terminate if user didn't key in anything
    if not search_title:
        print("Please insert value!")
        return

    search_title_split = search_title.split()
    df2 = pd.DataFrame(columns=["_id", "title"])

    # do an inner join first
    for each_title in search_title_split:
        books = collection.find({
                "title": { "$regex": each_title, '$options' : 'i' }
            },
            {
                "_id": 1, "title": 1,
            })
        df3 = pd.DataFrame(books)
        if df3.empty:
            continue
        elif df2.empty:
            df2 = df3
        else:
            df2 = pd.merge(df2, df3, on=["_id", "title"])

    # then do an outer join

    for each_title in search_title_split:
        books = collection.find({
                "title": { "$regex": each_title, '$options' : 'i' }
            },
            {
                "_id": 1, "title": 1
            })
        df3 = pd.DataFrame(books)
        if df3.empty:
            continue
        else:
            df2 = pd.merge(df2, df3, on=["_id", "title"], how='outer')

    return df2.values.tolist()

##### Advance Search (Assign to SEARCH button) #####
# categories: authors, categories, isbn, year ##
# Step 1 = store what user searched in dictionary #
# def create_search_dictionary():
#     # define variable
#     search_title = "Portlets and Apache Portals"
#     search_author = "stefan"
#     search_category = ""
#     search_isbn = ""
#     search_year = ""
#
#     search_dictionary = {}
#     #title
#     if search_title:
#         search_dictionary["title"] = search_title.split()
#
#     #authors
#     if search_author:
#         search_dictionary["authors"] = search_author.split()
#
#     #categories
#     if search_category:
#         search_dictionary["categories"] = search_category.split()
#
#     #isbn
#     if search_isbn:
#         search_dictionary["isbn"] = search_isbn
#
#     #year
#     if search_year:
#         search_dictionary["year"] = search_year
#
#     return search_dictionary


# Step 2: Advance search algorithm ##
# Note: each word in title, authors and categories will be stored in a list after Step 1 #
# Example: {"title": ["java", "programming"], "authors": ["king"]} will display title with either "java" or #
# "programming" by author "king" #
def advance_search(dictionary):
    # create dictionary based on what user searches
    search_dictionary = dictionary

    # terminate if user didn't key in anything
    if not search_dictionary:
        print("Please insert value!")
        return

    df = pd.DataFrame(columns=["_id", "title"])

    # for every filter that the user searches
    for category, search_text in search_dictionary.items():
        df2 = pd.DataFrame(columns=["_id", "title"])

        # if user searches year of publication
        if category=="year":
            search_text = int(search_text)
            books = collection.find({
                "publishedDate": {"$gte": datetime(search_text,1,1) , "$lt": datetime(search_text + 1, 1,1)}
                },
                {
                   "_id": 1, "title": 1
                })
            df2 = pd.DataFrame(books)

        # if user searches isbn
        elif category=="isbn":
            books = collection.find({
                "isbn": { "$regex": search_text, '$options' : 'i' }
                },
                {
                    "_id": 1, "title": 1
                })
            df2 = pd.DataFrame(books)
                
        # if user searches authors or categories
        else:
            # do an inner join first
            for each_search_text in search_text:
                books = collection.find({
                        category: { "$regex": each_search_text, '$options' : 'i' }
                    },
                    {
                        "_id": 1, "title": 1
                    })
                df3 = pd.DataFrame(books)
                
                if df3.empty:
                    continue
                elif df2.empty:
                    df2 = df3
                else:
                    df2 = pd.merge(df2, df3, on=["_id", "title",])

            # then do an outer join       
            for each_search_text in search_text:
                books = collection.find({
                        category: { "$regex": each_search_text, '$options' : 'i' }
                    },
                    {
                        "_id": 1, "title": 1,
                    })
                df3 = pd.DataFrame(books)
                
                if df3.empty:
                    continue
                else:
                    df2 = pd.merge(df2, df3, on=["_id", "title"], how='outer')

        if df2.empty:
            continue
        elif df.empty:
            df = df2
        else:
            df = pd.merge(df, df2, on=["_id", "title"])

    return df.values.tolist()




##### Extract title, isbn #####
# Input = df of bookIDs and other information #
# Output = Combined df with title and isbn #
def extract_title_isbn(df):
    id_list = df["_id"].tolist()
    books = collection.find({
            "_id": { "$in": id_list }
        },
        {
            "_id": 1, "title": 1, "isbn": 1
        })

    df2 = pd.DataFrame(books)
    return pd.merge(df, df2, on="_id")


##### Extract title, isbn, authors #####
# Input = df of bookIDs and other information #
# Output = Combined df with title, isbn and authors #
def extract_title_isbn_authors(bookids):
    id_list = df["_id"].tolist()
    books = collection.find({
            "_id": { "$in": id_list }
        },
        {
            "_id": 1, "title": 1, "isbn": 1, "authors": 1
        })

    df2 = pd.DataFrame(books)
    return pd.merge(df, df2, on="_id")


##### Extract authors only #####
# Input = list of bookIDs and other information #
# Output = Combined list with authors #
def extract_authors(bookids):
    df = pd.DataFrame(bookids,columns=["_id"])
    id_list = bookids
    books = collection.find({
            "_id": { "$in": id_list }
        },
        {
            "_id": 1, "authors": 1
        })

    df2 = pd.DataFrame(books)
    return pd.merge(df, df2, on="_id").values.tolist()

##### Extract isbn only #####
# Input = list of bookIDs and other information #
# Output = Combined list with isbn #
def extract_isbn(bookids):
    df = pd.DataFrame(bookids,columns=["_id"])
    id_list = bookids
    books = collection.find({
            "_id": { "$in": id_list }
        },
        {
            "_id": 1, "isbn": 1
        })

    df2 = pd.DataFrame(books)
    return pd.merge(df, df2, on="_id").values.tolist()

##### Extract isbn only #####
# Input = list of bookIDs and other information #
# Output = Combined list with thumbnailUrl #
def extract_thumbnailUrl(bookids):
    df = pd.DataFrame(bookids,columns=["_id"])
    id_list = bookids
    books = collection.find({
            "_id": { "$in": id_list }
        },
        {
            "_id": 1, "thumbnailUrl": 1
        })

    df2 = pd.DataFrame(books)
    return pd.merge(df, df2, on="_id").values.tolist()

##### Extract all #####
# Input = list of bookIDs and other information #
# Output = Combined list with title, isbn , thumbnailUrl, shortDescription, longDescription, status, authors and categories #
def extract_details(bookids):
    df = pd.DataFrame(bookids,columns=["_id"])
    id_list = bookids
    books = collection.find({
            "_id": { "$in": id_list }
        },
        {
            "_id": 1, "title": 1, "isbn": 1, "thumbnailUrl": 1, "shortDescription": 1, "longDescription": 1, "status": 1,
            "authors": 1, "categories": 1
        })

    df2 = pd.DataFrame(books)
    pd.set_option('display.max_columns', None)
    return pd.merge(df, df2, on="_id").to_dict()


