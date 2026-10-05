# Nikolas Morris: Personal Website + QR Code

Live site (once GitHub Pages is on): **https://niko2421.github.io/NikolasMorris-Website/**

```
index.html          The website (one page, built for phones first)
styles.css          Colors, fonts, layout. Change --accent at the top to rebrand.
contact.vcf         "Save Contact" card. One tap adds you to someone's phone.
resume.pdf          ← YOU ADD THIS (the "View Resume" button links here)
assets/             ← optional: headshot.jpg, preview.jpg
qr/qr-code.svg      QR for print (resume, business cards, posters)
qr/qr-code.png      QR, 1800px (LinkedIn, Canva, slides)
qr/qr-code-small.png QR, 450px (email signature)
qr/generate_qr.py   Re-creates the QR codes
```

---

## Step 1: Fill in your info

Open `index.html` and replace everything in `[SQUARE BRACKETS]`, such as `[MAJOR]`,
`[UNIVERSITY]`, `[YOUR-EMAIL]`, and `[YOUR-LINKEDIN]`. Delete any section you don't need.
Do the same in `contact.vcf`.

Tips for recruiters, who will spend about 30 seconds on your page:
- Keep "About" to 2–3 sentences, and end it with the role you want.
- Use bullets that show results ("grew club membership 35%"), not duties.
- Two or three strong projects beat six weak ones.

## Step 2: Add your resume and (optionally) a headshot

1. Export your resume as a PDF, name it **`resume.pdf`**, and put it in the top folder.
2. Optional: save a square photo as `assets/headshot.jpg`, then uncomment the
   `<img class="headshot">` line in `index.html`. It replaces the "NM" circle.

To upload on github.com, open the repo, click **Add file → Upload files**, then commit.

## Step 3: Turn on GitHub Pages (free hosting)

1. Make sure the site files are on the **`main`** branch. If they're on another branch,
   open a pull request and merge it.
2. On GitHub, go to **Settings → Pages**.
3. Under **Build and deployment**, set *Source* to **Deploy from a branch**,
   *Branch* to **`main`**, and *Folder* to **`/ (root)`**. Click **Save**.
4. Wait 1–2 minutes, then visit https://niko2421.github.io/NikolasMorris-Website/

Every time you commit a change to `main`, the site updates within a minute or two.

## Step 4: Test the QR code *before* you print anything

1. Open `qr/qr-code.png` on your laptop screen.
2. Point your phone camera at it (iPhone and Android cameras both read QR codes natively).
3. Confirm it opens your **live** site, and test it on a friend's phone too.

## Step 5: Use it

| Where | Which file | How big |
|---|---|---|
| Resume (top corner, next to contact info) | `qr-code.svg` | ~0.75–1 in (2–2.5 cm) |
| Business card | `qr-code.svg` | ≥ 0.8 in (2 cm) |
| Name badge / table sign at a career fair | `qr-code.svg` | 2–4 in |
| LinkedIn "Featured" section / banner | `qr-code.png` | as is |
| Phone lock screen (for "can I scan you?") | `qr-code.png` | as is |

Rules that keep it scannable:
- **Don't crop the white border.** The scanner needs it.
- Keep it **dark on a light background**. Don't invert it or put it on a photo.
- Put a short label under it, such as *"Scan for my portfolio"*.
- On a resume, **also write the URL in text.** Applicant tracking systems (ATS) and printed copies can't scan.

## Good to know

- **The QR code only stores the URL.** You can edit the website as much as you want
  and every printed QR code keeps working. It only breaks if the URL changes,
  for example if you rename the repo or switch to a custom domain.
- **Getting a custom domain later?** (Something like `nikolasmorris.com`, about $12/yr.)
  Do it *before* you print a lot of cards, then regenerate the QR:
  ```bash
  pip install segno
  python qr/generate_qr.py https://nikolasmorris.com
  ```
- **Privacy:** this site is public. Don't post your phone number, home address, or student ID.
  A school email plus LinkedIn is plenty.
