''' Data is like trees in a forest, some times you need to just collect all the trees and then step back
    This application allows you to collect trees and then evaluate them later
'''

from flask.ext.script import Manager, Server
from ForestOfTrees import app

import json
from collections import defaultdict

manager = Manager(app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

tree = lambda: collections.defaultdict(tree)
root = tree()


def print_tree(root):
    print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))
    
Class Tree()

if __name__ == "__main__":
    manager.run()
    
'''
You can run this application with a test server, by issuing the following command at the system prompt:
python manage.py runserver
    
You can enter data in a shell mode by issuing the following command:
python manage.py shell
    
root['menu']['id'] = 'file'
root['menu']['value'] = 'File'
root['menu']['menuitems']['new']['value'] = 'New'
root['menu']['menuitems']['new']['onclick'] = 'new();'
root['menu']['menuitems']['open']['value'] = 'Open'
root['menu']['menuitems']['open']['onclick'] = 'open();'
root['menu']['menuitems']['close']['value'] = 'Close'
root['menu']['menuitems']['close']['onclick'] = 'close();'

'''