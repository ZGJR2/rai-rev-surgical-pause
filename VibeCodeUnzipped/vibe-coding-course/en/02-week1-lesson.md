# Week 1 — Full Lesson
## "Build Your First App in One Sitting" — A Patient-Education Quiz

*A complete, step-by-step lesson for total beginners. No coding. No patient data.*
*Companion to the Vibe Coding for Healthcare Professionals syllabus.*

---

> **A note on the screenshots:** The boxes labeled **[SCREEN]** below are *described mockups* of what you'll see — drawn in text so they stay accurate even as the tools update their visuals. Real apps change their buttons and colors often; the *labels and actions* described here are what to look for. When the wording differs slightly, match the closest button.

---

## Lesson at a Glance

- **Goal:** Build and publish a live "Diabetes Basics" patient-education quiz.
- **Time:** 60–90 minutes.
- **Tool:** Lovable (no installation, runs in your web browser).
- **Cost:** A free trial is enough to finish this lesson.
- **You'll leave with:** A real web link you can open on your phone and share.
- **Data safety:** Zero patient data. Everything here is public health-education content.

### What you need

- A laptop or desktop with a web browser (Chrome, Edge, or Safari).
- An email address.
- 90 quiet minutes.

---

## Part 0 — The Safety Check (2 minutes, every time)

Before *any* build, say this out loud:

> **"Does this tool touch real patient information? "**
> Our quiz uses **general public health facts** about diabetes. **No patient names, no records, no PHI.** ✅ Safe to build.

If the answer is ever "yes, it touches real patient data," you **stop** and talk to IT/compliance. For this lesson, we are firmly in the **green zone**.

---

## Part 1 — Create Your Account (5 minutes)

**Step 1.** Open your browser and go to **lovable.dev**.

**Step 2.** Click **Sign up** (top-right). Use your email, or "Continue with Google."

```
[SCREEN] — Lovable home page
+------------------------------------------------------+
|  Lovable                       [ Log in ] [ Sign up ]|
|                                                      |
|     Build something Lovable                          |
|     Describe your idea. Get a working app.           |
|                                                      |
|     [  Describe what you want to build...        ]   |
|     [                                  ( ↑ Send ) ]  |
+------------------------------------------------------+
```

**Step 3.** Confirm your email if asked. You'll land on a big text box that says something like *"Describe what you want to build."* That box is where the magic happens.

> 🧑‍🏫 **Teaching script:** "See that one text box? That is the entire 'programming language' we need today — plain English. We're going to type a description, and the AI builds the app. If you can write a patient-instruction sheet, you can do this."

---

## Part 2 — Plan Before You Build (10 minutes)

Good builds start with a clear request. We'll write our description in three simple parts.

**The 3-part recipe for any app prompt:**

1. **What it is** — one sentence.
2. **What's in it** — the pieces/content.
3. **How it looks & behaves** — style and buttons.

Here is our finished plan for the quiz. **Don't type it yet** — just read it:

> **What it is:** A simple patient-education quiz app called "Diabetes Basics."
>
> **What's in it:** A welcome screen with a "Start Quiz" button, then 5 multiple-choice questions (one at a time) about type 2 diabetes, each with 3 answer options. After each answer, show whether it was right and a one-sentence explanation. At the end, show the score out of 5 and a "Try Again" button.
>
> **How it looks & behaves:** Clean and friendly, large readable text, calm blue-and-white colors, big buttons suitable for older patients. Mobile-friendly.

> 🧑‍🏫 **Teaching script:** "Notice we never said *how* to build it — no code words. We described the *experience* a patient would have. That's the whole skill."

---

## Part 3 — Generate Version 1 (10 minutes)

**Step 4.** Click into the big text box. Copy the **prompt script** below and paste it in.

### ⌨️ Prompt Script #1 — The First Build

```
Build a simple patient-education quiz web app called "Diabetes Basics."

Content:
- A welcome screen with the title, one friendly sentence, and a big "Start Quiz" button.
- 5 multiple-choice questions about type 2 diabetes, shown one at a time.
- Each question has 3 answer options.
- After the user picks an answer, show if it was correct and a one-sentence explanation.
- A "Next" button moves to the next question.
- At the end, show the score out of 5 and a "Try Again" button that restarts the quiz.

Style:
- Clean, friendly, and calm. Blue and white colors.
- Large, easy-to-read text and big buttons, suitable for older adults.
- Works well on a phone screen.

Use accurate, general, public health-education facts about type 2 diabetes.
Do not include any real patient information.
```

**Step 5.** Press **Send** (the arrow / "Send" button). Now wait — the AI writes the app while you watch.

```
[SCREEN] — Building
+-------------------------+----------------------------+
|  Chat (your messages)   |   Live Preview             |
|                         |                            |
|  You: Build a simple... |   ⏳ Generating your app...|
|                         |   • creating welcome screen|
|  Lovable: Working on it |   • adding 5 questions     |
|  ✓ Created welcome      |   • styling buttons        |
|  ✓ Added questions      |                            |
|  ✓ Added scoring        |   [ preview appears here ] |
+-------------------------+----------------------------+
```

**Step 6.** In 1–3 minutes, a working app appears in the **Live Preview** on the right. Click **Start Quiz** and try it.

> 🧑‍🏫 **Teaching script:** "Congratulations — you just built software. Don't worry if it's not perfect. First versions never are. Our real job starts now: testing and refining."

---

## Part 4 — Test Like a Skeptic (10 minutes)

Your job is to *try to break it.* Click everything. Use this checklist:

**✅ Week 1 Test Checklist**

- [ ] Does **Start Quiz** open the first question?
- [ ] Are all **5 questions** there?
- [ ] Does each question have **3 options**?
- [ ] When I pick an answer, does it tell me **right or wrong**?
- [ ] Is there a **one-sentence explanation** after each answer?
- [ ] Does **Next** move forward every time?
- [ ] At the end, is there a **score out of 5**?
- [ ] Does **Try Again** restart from the beginning?
- [ ] On a **narrow window** (drag it skinny like a phone), does text still fit?

Write down anything that's wrong or ugly. Each item becomes a refinement in Part 5.

> 🧑‍🏫 **Teaching script:** "Testers aren't pessimists — they're the patient's advocate. If a confused click can happen, a real patient will find it. Note it; we'll fix it."

---

## Part 5 — Refine in Small Steps (15 minutes)

Now we improve the app **one change at a time**, typing each request into the same chat box. After each one, the preview updates — re-test before the next change.

### ⌨️ Prompt Scripts — Common First Refinements

Use only the ones you actually need:

**Make text bigger / friendlier:**
```
Make all the text larger and add more space between the buttons,
so it's comfortable for older adults to read and tap.
```

**Add a progress indicator:**
```
At the top of each question, show "Question 2 of 5" so users know how far along they are.
```

**Improve the ending:**
```
On the final score screen, add an encouraging message:
if the score is 4 or 5, say "Great job!"; if it's 3 or lower,
say "Good start — review and try again." Keep the "Try Again" button.
```

**Fix a specific bug (example):**
```
When I click "Next" on question 3, nothing happens.
Please make the "Next" button move to the following question every time.
```

> 🧑‍🏫 **Teaching script — the #1 habit:** "One change, then test. If you ask for five things at once and something breaks, you won't know which one caused it. Slow is smooth, and smooth is fast."

> 💡 **Golden rule of bug reports:** Describe **what happened**, not how to fix it. "When I click Save, nothing happens" gives the AI everything it needs. You don't have to know the solution.

---

## Part 6 — Publish It (10 minutes)

**Step 7.** Find the **Publish** (or **Deploy**) button — usually top-right.

```
[SCREEN] — Top bar
+------------------------------------------------------+
|  Diabetes Basics            [ Share ]  [ Publish ▸ ] |
+------------------------------------------------------+
```

**Step 8.** Click **Publish**. After a few seconds you'll get a **live link** like `diabetes-basics.lovable.app`.

**Step 9.** Open that link on your **phone**. It's a real, live app on the internet now.

**Step 10.** Send the link to one trusted colleague and ask: *"Would this help a newly diagnosed patient? What's confusing?"*

> 🧑‍🏫 **Teaching script:** "That link works on any phone, anywhere — you didn't install a thing. This is the moment most people realize they can actually do this."

---

## Part 7 — Wrap-Up & Homework (5 minutes)

**You did it.** You planned, built, tested, refined, and published a real app — with zero code and zero patient data.

### 📋 Homework for next session

1. **Re-test** your published quiz on a phone and fix **one** thing you don't like (one small prompt).
2. **Write a plan** (the 3-part recipe) for a tool *you* want — a checklist, a calculator, a flashcard set. Don't build it yet; just write the description.
3. **Start your Prompt Library:** open a notes file and paste in any prompt that worked well today.

### ✅ Self-check: did you meet the goals?

- [ ] I created an account and found the "describe your app" box.
- [ ] I wrote a clear 3-part plan.
- [ ] I generated a working first version.
- [ ] I tested it against the checklist.
- [ ] I made at least one refinement, one change at a time.
- [ ] I published it and opened the live link on my phone.
- [ ] I confirmed: **no real patient data** anywhere. ✅

---

## Quick Troubleshooting

| Problem | What to do |
|---|---|
| The app didn't generate / errored | Click Send again, or paste: *"That didn't work. Please try building the quiz again."* |
| A button does nothing | Tell the AI exactly: *"When I click X, nothing happens. Please make X do Y."* |
| It looks cramped on a phone | Paste: *"Make it mobile-friendly with larger text and spacing."* |
| It changed something I liked | Paste: *"Undo the last change and go back to how it was before."* |
| I'm out of free credits | You can stop here — your published link still works. Upgrading is optional. |

---

## Instructor Notes (for whoever is teaching this)

- **Group size:** Works 1-on-1 or up to ~12 with one helper roaming.
- **Pre-class setup:** Ask learners to create the account *before* class to save 5 minutes.
- **The one rule to over-emphasize:** the data-safety check in Part 0. Repeat it at the start and end.
- **Common stumble:** learners try to fix things themselves instead of *describing the problem*. Coach them back to "describe what happened."
- **If someone finishes early:** have them add a 6th question, or restyle with the prompt *"Give it a warmer, more reassuring look."*
- **Time-saver:** keep Prompt Script #1 on a handout or shared doc so nobody has to retype it.

---

*This lesson is educational and uses only public health-education content. It is not legal or compliance advice. Never enter real patient information into AI tools, and follow your organization's policies.*
