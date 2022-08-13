
""""
Like the previous question, suppose we have a list of clicks and corresponding urls as follows:

url_counts = ["50,google.com",
     "60,yahoo.com",
     "10,yahoo.com",
     "1,wikipedia.org",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "2,wikipedia.org",
     "1,stackoverflow.com",
     "1,google.com"]

This time, we want to write a function that takes in this input as a parameter and returns a data structure containing the total number of clicks that were recorded on each url.

Note: Use of functions like "split", "index", "indexOf" are now permitted if desired.

Sample output:

url_clicks(counts) =>
google.com           51
yahoo.com:           370
wikipedia.org        3
sports.yahoo.com     40
stackoverflow.com    1

Complexity variables:
n: the number of strings in the list
(The length of the input string has a constant upper limit.)

"""

url_counts = [
    "50,google.com",
    "60,yahoo.com",
    "10,yahoo.com",
    "1,wikipedia.org",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "2,wikipedia.org",
    "1,stackoverflow.com",
    "1,google.com"
]

urls = {}


def url_clicks(url_counts):

    for url in url_counts:
        count,  url1 = url.split(",")
        try:
            urls[url1] += int(count)
        except KeyError:
            urls[url1] = int(count)


def main():
    url_counts = ["50,google.com",
                  "60,yahoo.com",
                  "10,yahoo.com",
                  "1,wikipedia.org",
                  "40,sports.yahoo.com",
                  "300,yahoo.com",
                  "2,wikipedia.org",
                  "1,stackoverflow.com",
                  "1,google.com"]

    url_clicks(url_counts)

    for url in urls:
        print(url, urls[url])


if __name__ == "__main__":
    main()
