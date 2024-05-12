from take_query import take_query


# Main function to initiate the assistant
if __name__ == '__main__':
    try:
        take_query()
    except Exception as e:
        print(e)
        print("Exiting")
