# Catch the vision - 10th session: Git & GitHub Fundamentals for Software Engineers


## Managing Merge Conflicts
Welcome to the Catch the Vision Workshop's Python Calculator repository! This workshop is designed to help participants learn Git through practical exercises focused on building a simple command-line calculator collaboratively.

In this exercise, we will be managing merge conflicts.
### What is a Merge Conflict?

Firstly, let's define what we mean by a merge conflict. A merge conflict occurs when Git is unable to automatically resolve differences in code between two commits. When all the changes in the code occur on different lines or in different files, Git will successfully merge commits without your help. But if there are conflicting changes on the same lines, a "conflict" occurs because Git doesn’t know which code to keep and which to discard.

### Causes of Merge Conflicts

Merge conflicts typically occur when:

1. Several people have changed the same lines of the same file.
2. One person decided to delete a file while another person decided to modify it.
3. There are changes in the local branch which have not been committed yet, and those changes overlap with another branch's committed changes.

### How to Resolve Merge Conflicts

Resolving merge conflicts involves three steps:

1. **Identifying the conflict**: Git will mark the area in your code where conflict has arisen. It does so by enclosing the conflicting changes between `<<<<<<< HEAD` and `=======`, and ends with `>>>>>>> branch-name`.

2. **Reviewing the conflict**: Analyze the code and determine which parts you want to keep and which parts to discard. This step requires communication between the developers involved in the conflict.

3. **Resolving the conflict**: Once the desired changes are chosen, manually edit the code to resolve the conflict, remove the conflict markers, and save the file.

After resolving the conflict, commit the resolved file to finalize the merge.

### Exercise: Managing Merge Conflicts

Now, let's put this into practice.