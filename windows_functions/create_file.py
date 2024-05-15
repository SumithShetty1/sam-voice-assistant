import os
from sam_functions.speak import speak


# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Define file types mapping
file_types = {
    ".txt": "Text",
    ".doc": "Document",
    ".xls": "Excel",
    ".ppt": "PowerPoint",
    ".py": "Python",
    ".html": "HTML",
    ".css": "CSS",
    ".js": "JavaScript",
    ".c": "C",
    ".cpp": "C++",
    ".cs": "C#",
    ".java": 'Java',
    ".php": "PHP"
}


# Function to create different types of files
def create_file(query):
    try:
        # Extract the file type from the query
        file_type = None
        if "text file" in query:
            file_type = ".txt"
        elif "document file" in query:
            file_type = ".doc"
        elif "excel file" in query:
            file_type = ".xls"
        elif "powerpoint file" in query:
            file_type = ".ppt"
        elif "python file" in query:
            file_type = ".py"
        elif "html file" in query:
            file_type = ".html"
        elif "css file" in query:
            file_type = ".css"
        elif "javascript file" in query:
            file_type = ".js"
        elif "c file" in query:
            file_type = ".c"
        elif "c++ file" in query:
            file_type = ".cpp"
        elif "c# file" in query:
            file_type = ".cs"
        elif "java file" in query:
            file_type = ".java"
        elif "php file" in query:
            file_type = ".php"

        file_name = "file"

        if file_type:
            file_name = file_types[file_type].lower()

        if "name it as" in query or "save it as" in query:
            name_query = query.split("name it as ")[1] if "name it as" in query else query.split("save it as ")[1]
            file_name = name_query.split()[0]

        if file_type:
            base_directory = os.path.join(os.path.expanduser("~"), "Documents", "Sam Virtual Assistant", "Documents"
                                          , file_types[file_type])
            create_directory(base_directory)
            file_path = os.path.join(base_directory, file_name + file_type)

            # Check if the file already exists
            count = 1
            while os.path.exists(file_path):
                file_path = os.path.join(base_directory, f"{file_name} ({count}){file_type}")
                count += 1

            # Create an empty file
            with open(file_path, "w") as f:
                pass

            updated_file_name = f"{file_name} ({count - 1}){file_type}" if count > 1 else f"{file_name}{file_type}"

            speak(f"{updated_file_name} has been created, boss.")

        else:
            speak("Sorry, I couldn't determine the file type from the query, boss.")
    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to create the file, boss.")
