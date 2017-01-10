# This file defines command line commands for manage.py
#
# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

from flaskuserapp import manager, create_users


@manager.command
def init_db():
    """ Initialize the database."""
    create_users()
