import pandas as pd
import os
from multiprocessing import pool

# Supported languages/extensions:
# .html
# .css
# .js
# .c
# .cpp
# .c
# .md
LANGUAGES = {"Hypertext Markup Language": [".html"],
             "Cascading Style Sheets": [".css", ".scss"],
             "JavaScript": [".js"],
             "TypeScript": [".ts", ".tsx"],
             "C": [".c", ".h"],
             "C++": [".cpp", ".cc"],
             "C#": [".cs"],
             "Java": [".java"],
             "Python": [".py"],
             "Dart": [".dart"],
             "Rust": [".rs"],
             "Kotlin": [".kt"],
             "Shell Scripts": [".sh"],
             "Go": [".go"],
             "JSON": [".json"],
             "YAML": [".yaml", ".yml"],
             "Markdown": [".md"]
             }

# print(LANGUAGES.items())
def get_all_extensions():
    li = []
    for key, value in LANGUAGES.items():
        li += value
    return li

ALL_SUPPORTED_FILE_EXTENSIONS = get_all_extensions()
print(ALL_SUPPORTED_FILE_EXTENSIONS)


WORKING_DIR = r"C:\Users\vincent\Documents\TEMP\finalproj_resources"
CLEAN_REPO_DIR = os.path.join(WORKING_DIR, "CLEANREPOS")
DATA_DIR = os.path.join(WORKING_DIR, "data")


# FEATURE SELECTION, SELECTING SPECIFIC SUPPORTED FILES
def featurize_data(directory):
    i = 0
    all_files = pd.DataFrame()

    for filename in os.listdir(directory):
        # if i == 1000: break
        # Get file extension
        ext = os.path.splitext(filename)[1]
        if ext.lower() in ALL_SUPPORTED_FILE_EXTENSIONS:
            language = None
            for key, value in LANGUAGES.items():
                if ext.lower() in value:
                    language = key
                    break
            path = os.path.join(directory, filename)
            content = None
            try:
                with open(path, 'r', encoding="UTF-8") as f:
                    content = f.read()
            except:
                continue

            entry = pd.DataFrame({"Language": [language], "Path": [path], "Content": [content]})
            all_files = pd.concat([all_files, entry])

        print(i)
        i += 1

    return all_files

data = featurize_data(DATA_DIR)
data.to_csv("datawithcontent.csv", index=False)