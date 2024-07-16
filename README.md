<h1>aula1_Jornada Python</h1>

<h2>Description</h2>

This project is the first class of <i>Jornada Python</i> from <i>Hashtag Treinamentos</i> and consists in an automation process where the objective is to insert data from a ```.csv``` file in a web system, in an automated way with Python.
The logic behind the project was built with ```pyautogui``` library. With this module, an automation was done, first to login in the system and then, to input data on it. But how the algorithm open the ```.csv``` file? It's simple, with ```pandas``` library, all the data from the file was stored in a variable used in the algorithm. After that, one <i>for</i> loop scroll through the table and send data to variables, which store respective data and are inputted in the system with ```pyautogui``` commands. 
Finally, a loop <i>for</i> combined with a <i>if</i> statement is responsible for analyze if the content in obs column of our table is different from ```nan```. If different, the algorithm writes the content from obs column in the related field on the HTML page.

<h2>How to install and run the project</h2>

You need to clone the repository by doing the following command:
```git clone https://github.com/leoGeraldino/aula1_jornadaPython.git```

After this step, you need to configure a virtual environment, like this:
```python -m venv <virtual_environment_name>```

And activate it: 
```venv\Scripts\activate```

Finally, you need to instal the ```requirements.txt``` file, like this:
```pip install -r requirements.txt``` and so you can run the code.

<h2>How to use the project</h2>

This project was built just for didactic purposes, but you can modify it according to your needs. For example, you can do something like this to automate the creation of PowerPoint presentations for your job, or maybe automate data input in any web systems you want. 
Feel comfortable to use it as you need.

<h2>Credits</h2>

All the content in this project was a part of the event<i>Jornada Python</i> from <i><a target="_blank" href="https://www.youtube.com/@HashtagTreinamentos">Hashtag Treinamentos</a></i>. If you want to learn Python, in good content in brazilian portuguese, go ahead and see how amazing is Lira's didactic. 
