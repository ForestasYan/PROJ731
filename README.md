# PROJ731
This project is a introduction to programming sockets and map-reduce in python.

To launch this programm, you'll have to launch "serveur1.py" in one terminal and then "client.py" in an other.
Client will send the name of multiple .txt files to the server that will open them, and create a thread and a python dictionnary for every text.
Every thread will count the amount of words of their text, put it in their dictonnary.
Then a reduce function will combine the dictionnaries and the programm will create a file that shows the total amount of times every word was used in all the texts.
