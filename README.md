# Let Law Students Become Law Students First

A one-page campaign site for the Bar Association of the District of Columbia (BADC) resolution before the ABA House of Delegates on accelerated law-firm recruiting. It hosts the on-site pamphlet and a full-resource page (resolution text, report, coalition, and citations).

## Live URL

Once published (see below), the site will be at:

    https://codesisyphus.github.io/law-student-hiring-resolution/

The QR code printed on the pamphlet points to this exact address. **Keep the repository name `law-student-hiring-resolution`** or the QR code will not resolve. If you must rename it, regenerate the QR (see "Changing the URL" below).

## Files

- `index.html`: concise, persuasive landing page (what the QR code opens).
- `resolution.html`: full resolution text, report, coalition list, and sources.
- `assets/Pamphlet_ABA_Resolution.pdf`: the printable one-page pamphlet.
- `.nojekyll`: tells GitHub Pages to serve the files as-is.

## Publish on GitHub Pages

1. Create a new **public** repository named `law-student-hiring-resolution` under the `CodeSisyphus` account. Do not add a README, .gitignore, or license when creating it (this folder already has them).
2. Open a terminal (or Claude Code) in this folder and run:

       git init
       git add -A
       git commit -m "Add BADC / ABA resolution campaign site"
       git branch -M main
       git remote add origin https://github.com/CodeSisyphus/law-student-hiring-resolution.git
       git push -u origin main

3. On GitHub, go to **Settings -> Pages**. Under "Build and deployment," set **Source** to **Deploy from a branch**, choose branch **main** and folder **/ (root)**, and click **Save**.
4. Wait one to two minutes, then open `https://codesisyphus.github.io/law-student-hiring-resolution/`.

## Update the content

Edit the HTML files, then:

    git add -A
    git commit -m "Update content"
    git push

Pages redeploys automatically within a minute or two.

## Changing the URL

If you publish under a different repo name or a custom domain, regenerate the pamphlet QR code so it points to the new address, then reprint the pamphlet.
