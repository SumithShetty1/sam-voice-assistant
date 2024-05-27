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
def create_file(query, intent_data):
    try:
        # Detect the entity in the query
        detected_entity = next((entity for entity in intent_data.get('entities', []) if entity in query.lower()), None)

        # Extract the file type from the query
        file_type = None
        if detected_entity == "text":
            file_type = ".txt"
        elif detected_entity == "document":
            file_type = ".doc"
        elif detected_entity == "excel":
            file_type = ".xls"
        elif detected_entity == "powerpoint":
            file_type = ".ppt"
        elif detected_entity == "python":
            file_type = ".py"
        elif detected_entity == "html":
            file_type = ".html"
        elif detected_entity == "css":
            file_type = ".css"
        elif detected_entity == "javascript":
            file_type = ".js"
        elif detected_entity == "c":
            file_type = ".c"
        elif detected_entity == "c++":
            file_type = ".cpp"
        elif detected_entity == "c#":
            file_type = ".cs"
        elif detected_entity == "java":
            file_type = ".java"
        elif detected_entity == "php":
            file_type = ".php"

        file_name = "file"

        if file_type:
            file_name = file_types[file_type].lower()

        # Loop through each preposition pattern
        for prep in intent_data['text']:
            if prep in query:
                # Extract file name from the query based on the preposition
                name_query = query.split(prep)[1].strip()
                file_name = name_query.split()[0]
                break

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

            speak(f"{updated_file_name} has been created sir.")

        else:
            speak("Sorry, I couldn't determine the file type from the query sir.")
    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to create the file sir.")
