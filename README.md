## Code with Document

This project illustrate how to utilize git's hook tricks to 
**enforce**: Update documents when we update our codes.

**doclist.json**:

This file contains a map from the source code to the documents.
Currently, we assume one source code file only relates to (at-most) one document file.
But one document file can be pointed by multiple source code files.

**Basic idea**:

The major code is located in **util/git-pre-commit.py**.

When we commit our modifications, the script will scan the staged files, check whether some code files have their related document files.
If yes, the script requires the document file is updated too.

The user can either: update both soruce-code-file and doc-file, or, explicitly ignore the checks.

### Notes

Some scripts of the demo are inherited from Gem5, an open-sourced cycle-level hardware simulator.

### License

The project follows Mulan License.

