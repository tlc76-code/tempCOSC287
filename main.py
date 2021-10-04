import requests


def main():
    #############################
    # Examples using APIs
    #
    # Version 1
    #############################

    # Define variables
    data = []

    # Setup parameters for API query
    base_url = "https://api.usa.gov/crime/fbi/sapi/api/hatecrimebybias/states/"
    query_params = {"api_key": "plZ6fEz4jjaRFeNR2BZPmhd6Vw9SGImEs0YGZ4hI",
                    "stateAbbr": "MO",
                    "bias": "anti_atheism",
                    "variable": "OFFENSE"}

    #Example stolen from the internet (doesn't fucking work) https://nicktallant.com/DataCensus/PolicyArea/Crime/
    #base = 'https://api.usa.gov/crime/fbi/sapi/'
    #query = 'api/summarized/agencies/WY0200100/homicide?api_key='
    #key = 'plZ6fEz4jjaRFeNR2BZPmhd6Vw9SGImEs0YGZ4hI'

    # Query FBI database for hate crime data
    response = requests.get(base_url, query_params)
    print(response.url)

    print(response.text)



    # Pull out the json text
    json_txt = response.json()
    #print(json_txt)
    # Select columns of interest from json text [NOTE json libary does this in a nice way]
    for record in json_txt:
        # Use .get() because some results don't have data for all attributes

        data.append(record)

    # Print header and data

    print(data)


if __name__ == "__main__":
    main()
