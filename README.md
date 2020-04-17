Sean's Fitness Centre
Getting Started
Install flask. It'll act as the server for the project.

pip3 install Flask
To start working on the project you need to:

Open terminal ( cmd + space and type terminal)
Type cd sean_fitness
Type code .
In VSCode to start server:
i) Select Terminal from top menu panel
ii) Select new Terminal
iii) type “python3 main.py” in the vscode terminal
Go to to http://0.0.0.0:5000/, you should see the website running.

File Structure
main.py: entry point for the program. This creates the server and is the entry point for the program.

/templates: folder containing HTML files. Think of an HTML file as a page on the website.

/templates/index.html: home page of the project

static: all things that don't change dynamically, like Images and css styles.

src: this is where we will keep all the logic. The meat and potatoes.

Project timeline
 Phase 1: Write the calorie counter algo
 Phase 2: Learn HTML/CSS and create a frontend website collects the input params from the user (gender, execursion level, etc...)
 Phase 3: Connect the HTML/CSS to the calorie counter algo
 Phase 4: Return the results of the calorie counter algo to the client. (We'll talk about this more later).