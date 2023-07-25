# Catch the vision - 10th session: Git & GitHub Fundamentals for Software Engineers :computer: :octocat:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

## Managing Merge Conflicts :construction_worker: :collision:
Welcome to the Catch the Vision Workshop's Python Calculator repository! :wave: This workshop is designed to help participants learn Git through practical exercises focused on building a simple command-line calculator collaboratively. :people_holding_hands:

In this exercise, we will be managing merge conflicts. :monocle_face:

### What is a Merge Conflict? :grey_question:

Firstly, let's define what we mean by a merge conflict. :thinking: A merge conflict occurs when Git is unable to automatically resolve differences in code between two commits. When all the changes in the code occur on different lines or in different files, Git will successfully merge commits without your help. But if there are conflicting changes on the same lines, a "conflict" occurs because Git doesn’t know which code to keep and which to discard.

### Causes of Merge Conflicts :detective:

Merge conflicts typically occur when:

1. Several people have changed the same lines of the same file. :writing_hand:
2. One person decided to delete a file while another person decided to modify it. :file_folder: :x:
3. There are changes in the local branch which have not been committed yet, and those changes overlap with another branch's committed changes. :busts_in_silhouette:

### How to Resolve Merge Conflicts :hammer_and_wrench:

Resolving merge conflicts involves three steps:

1. **Identifying the conflict**: Git will mark the area in your code where conflict has arisen. It does so by enclosing the conflicting changes between `<<<<<<< HEAD` and `=======`, and ends with `>>>>>>> branch-name`.

2. **Reviewing the conflict**: Analyze the code and determine which parts you want to keep and which parts to discard. This step requires communication between the developers involved in the conflict. :speech_balloon:

3. **Resolving the conflict**: Once the desired changes are chosen, manually edit the code to resolve the conflict, remove the conflict markers, and save the file. :memo:

After resolving the conflict, commit the resolved file to finalize the merge. :white_check_mark:

### Exercise: Managing Merge Conflicts :muscle:

Now, let's put this into practice. :rocket: