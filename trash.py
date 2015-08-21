#!/usr/bin/env python
import sys
import shutil
import os
 
def moveToTrash(trash_dir):
    file_name = sys.argv[1]
    if os.path.isfile(file_name):
        shutil.move(file_name, trash_dir)
        print "%s moved to Trash folder." % (file_name)
    else:
        print "%s not found." % (file_name)

def listTrashContents(trash_dir):
    print "\n".join(os.listdir(trash_dir))

if __name__ == "__main__":
    # The first argument of sys.argv is always the filename,
    # meaning that the length of system arguments will be
    # more than one, when command-line arguments exist.
    if len(sys.argv) > 1:
        trash_dir = os.environ['HOME'] + "/.Trash"
        if sys.argv[1] == "--list":
            listTrashContents(trash_dir)
        else:
            moveToTrash(trash_dir)
    else:
        command_tokens = sys.argv[0].split("/")
        command = command_tokens[len(command_tokens) - 1]
        print "Usage: %s [options] [filename]" % command
        print "Options:"
        print "  --list        Lists Trash contents"
        print "Examples:"
        print "  %s myFile" % command
        print "  %s --list" % command
        sys.exit(1)
