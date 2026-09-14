# Repo Publishing

For tenants whose target is a repository path.

## Path

The tenant profile owns the convention, including whether an issue key belongs in the filename. Read it there and build the path from it.

Do not invent a directory. If the convention names a directory that does not exist, say so and ask whether to create it, rather than writing to the nearest one that does.

## Before writing

Show the resolved path, whether it exists, and what changes if it does.

For an existing file, show the change at section level. For a new file, show the title and the section list.

## Writing

- Write the file at the resolved path.
- Preserve the file's existing frontmatter, and update only the fields that changed.
- Do not reformat sections you did not change. A publish that reflows the whole document makes the change unreviewable.
- Do not delete a section because it is empty. Empty and present is a known gap; absent is an invisible one.

## Verdict and override

The review verdict goes in the document's Overview table, in the Review verdict field.

If the gate was overridden, the override block goes above everything else in the file, before the first heading.

## Version control

Do not commit, branch, push or open a pull request unless the user asked for that specifically. Writing the file was the instruction.

If the working tree has uncommitted changes to the same file, say so before writing rather than overwriting them.

## Conflicts

If the file changed since the version you were working from, stop, show the difference, and ask. Do not merge silently.

## After

Report the path and whether the file was created or updated. Offer the commit as a next step if that fits how the user works, in one line, and do not take it.
