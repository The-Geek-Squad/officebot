OFFICE BOT
==========

Description
-----------
Get your favorite Character from the Office to post to Slack

Required Dependencies
---------------------
* MySQL
* MySQL Python Connector
* Slack Client

Installation
------------
.. code-block:: bash

    git clone https://github.com/The-Geek-Squad/officebot.git
    cd officebot
    pip install mysql-connector-python
    pip install slackclient

Rename settings.py.example to settings.py and your slack bot api key and database information

.. code-block:: bash

    mv settings.py.example settings.py

Run the Database setup tool

.. code-block:: bash

    python src/setDatabase.py

Currently no quotes are provided so you have to fill the quotes table in the database manually

.. code-block:: sql

    USE officebot;
    INSERT INTO quotes (quote) VALUE ("Example");

Then Fire up officebot

.. code-block:: bash

    python src/main.py

Usage
-----

To Get a quote:

.. code-block:: bash

    @<officebot-name> quote

To Get the bot to say That's What She Said

.. code-block:: bash

    @<officebot-name> twsh

To Say Hello

.. code-block:: bash

    @<officebot-name> hi