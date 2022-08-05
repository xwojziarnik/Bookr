🇬🇧

# Bookr

## Table of contents:

- [The aim of the project](#the-aim-of-the-project)
- [What is my motivation?](#what-is-my-motivation)
- [Features](#features)
- [Technologies & Documentation](#technologies--documentation)
- [Installation](#installation)
- [Run](#run)

## The aim of the project

This is going to be a repository with reviews of books. 

## What is my motivation?

I want to consolidate my Django skills while doing an app with a ["Web Development with Django: Learn to build modern web applications with a Python-based framework"](https://www.amazon.pl/Web-Development-Django-applications-Python-based/dp/1839212500/ref=asc_df_1839212500/?tag=plshogostdde-21&linkCode=df0&hvadid=504384189023&hvpos=&hvnetw=g&hvrand=5456534563855773767&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1011615&hvtargid=pla-1202063357020&psc=1) book.

## Features


- [x] Listing last reviews on main site,
- [x] Searching for books using title / contributor,
- [x] Login / logout,
- [x] Listing reviews if you're not logged in,
- [x] Adding / editing reviews if you are logged in & you have permissions,
- [x] Adding media (cover, sample) into books details,
- [x] Modified admin site,
- [ ] Containerize the app

## Technologies & Documentation

- [Python 3](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/4.0/)
- [Docker](https://www.docker.com/)
- [SQLite3](https://www.sqlite.org/docs.html)

## Installation

<details>
<summary>Python:</summary>

Visit https://www.python.org/downloads/ and type which installing package you prefer (by your operating system) and download the package.

After download, go through installation process.

After above, let's check if Python is installed on your computer. To do this, open your terminal or command prompt and type:

For MacOS/Linux:
```
python3 --version
```

For Windows:
```
python --version
```
</details>

<details>
<summary>Virtual environment:</summary>

[More info about venv](https://docs.python.org/3/library/venv.html)

Open terminal/command prompt and create directory where you will create a django project using commands below:

```
ls                                                   # to check content of your domain directory
mkdir <directory_name>                               # to create a separated directory for project
cd <directory_name>                                  # just to go into new directory
python3 -m venv <virtualenv_name>                    # to create virtualenv using MacOS terminal
python -m venv <virtualenv_name>                     # to create virtualenv on Windows
source <virtualenv_name>/bin/activate                # to activate virtualenv on MacOS
<virtualenv_name>\Scripts\activate                   # to activate virtualenv on Windows

(<virtualenv_name>) <username>@<actual_directory> %  # after above you should see the (<virtualenv_name>). This line appears on MacOS.
```
</details>

<details>
<summary> Django:</summary>

If you did above tutorials, now you should have schema of your files like:

```
Desktop/
    <directory_name>/
        <virtualenv_name>
```

Now we can install <framework name> framework. Simply type in your terminal/command prompt:

```
pip3 install django     # on MacOS
pip install django      # on Windows
```

</details>

<details>
<summary>All packages included in requirements.txt:</summary>

<details>
<summary>First option (preferred):</summary>

After clone this repo, type command:
```
pip3 install -r requirements.txt        # on MacOS
pip install -r requirements.txt         # on Windows
```

</details>

<details>
<summary>Second option:</summary>

Open file ```requirements.txt``` and type command with every package name:
```
pip3 install <package_name>     # on MacOS
pip install <package_name>      # on Windows
```

</details>

</details>

Perfect! Now, it's time to last episode.

##  Run

We've seen how to run venv. Keep that running!

<details>
<summary>Now we can simply clone this repo, and see if it's working on our machine (in case we did everything above count creating virtualenv):</summary>

```
git init                                                # to initialize repository
git clone <repo url>      # to clone this repository into your local machine

python3 manage.py runserver    # using MacOS
python3 manage.py runserver    # using Windows
```
</details>

And that's it! Great job!