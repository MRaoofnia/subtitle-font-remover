from sys import argv

def help():
    print("""
    Use FontRemover source_filename [destination_filename] to remove fonts from one file.
    Use FontRemover -a source_path [destination_path, name_postfix] to remove font from all files in path.
    Use FontRemover -h to see this manual.""")


def remove(source:str, dest:str):
    with open(source) as sourceFile:
        with open(dest,'w') as destFile:
            isFontFlag = False
            for line in sourceFile.readlines():
                if line.startswith("[Font"):
                    isFontFlag = True
                elif line.startswith("[Event"):
                    isFontFlag = False
                if not isFontFlag:
                    destFile.write(line)

if __name__=="__main__":
        if len(argv) < 2:
            print("No arguments provided.")
            help()
        elif argv[1] == "-h":
            help
        elif argv[1] == "-a":
            print("Work in progress...")
            help()
        else:
            sourceFile = argv[1]
            destFile = ""
            if len(argv) == 2:
                destFile = sourceFile.replace(".ass","") + "_NO_FONT.ass"
            else:
                destFile = argv[2]
            remove(sourceFile,destFile)
            print("Done ;)")


#with open()