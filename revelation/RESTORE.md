# Restore Revelation on staging

The original staging backup contains the 22 chapter reading pages as serialized WordPress block content and their identifying metadata. The verified staging archive contains their revised content. Each archive includes a SHA-256 manifest.

1. Extract the selected archive and verify the manifest.
2. Confirm site 248834710 and each chapter page’s ID, URL and parent.
3. Back up the current chapters and reconcile later edits before restoring.
4. Obtain fresh content and block hashes and replace only the intended chapter block.
5. Read back the saved block and compare the rendered verse text, notes, and anchors.

The landing page and comparison pages are separate from the chapter reading blocks.
