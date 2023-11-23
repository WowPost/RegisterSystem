![home](https://github.com/WowPost/RegisterSystem/assets/150549548/7081736b-0c61-438b-824d-dd59ff765cb0)
![users](https://github.com/WowPost/RegisterSystem/assets/150549548/dd989a64-423d-4d03-a8a9-808098aa856c)

# Register System

This is a simple Django project to get started in Django studies. It's a simple form to input and display user data.

## Getting Started

This project is aimed at Debian based distros but other Unix based distros, Windows and Mac users should be able to follow, with some command changes 
specific to each OS. You can also grab a copy of a Debian based distro and start running it on a Virtual Machine. Setting up a VM is not on the scope of this tutorial.

### Prerequisites

You need to Git, Python version 3.11, Django and pipenv package installed. It is a simple straight forward process:

```
Open your terminal and check if python is installed: python --version
If the command above does not display your python version, do: sudo apt install python3.11
For git, the process is similar, but do instead: git --version
If not installed, do: sudo apt install git
Then run: pip install pipenv --> to create a virtual environment at your desired location. To run it, do: pipenv install
To activate the virtual environment, do: pipenv activate
With your activated environment, install Django: pip install Django. 
```

### Installing

After everything is set up:

Getting the repository:

```
git clone https://github.com/WowPost/RegisterSystem.git
```

Then:

```
Move to WowPost/RegisterSystem and run the pip install pipenv here.
Move to WowPost/RegisterSystem/RegisterSystem where manage.py file is located. This is the root directory of the project.
Here, run: pip install -r requirements.txt
```

Finally:

```
To set the configurations: python manage.py makemigrations
To apply the saved configurations: python manage.py migrate
```
Your project should display the images above.

### J

