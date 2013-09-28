climson
==========

climson is a tool for easy and simplify to implement applications that is using multi-command CLI.

climsonize your application
-----------

Let me show you climson with an example. 

There are **Only 4 steps to implementation.**

#. Create handler-class extends *climson.BaseCommand*.
#. Specify *name(required)* as sub-command name and *description* into class field.
#. Implement *do_command(self, **kwargs)* method. If command executes with somw options, method takes it as **kwargs.
#. Make client instance & register command classes.

Create *handler-class* for each sub commands ::

    # file: my_command.py

    from climson import climsonClient
    from climson import climson
    from climson.climson import make_option

    class Hello(climson.BaseCommand):
    
        # command name (required)
        name = 'hello'

        # sub command description
        description = 'Say hello!'

        def do_command(self):
            print 'Hello!'

If you want to use some options, specify it to field *options* like this.

It means same as *argparse.add_argument()*, and it's 2 ways to reference opt's values in do_command(), **kwargs with do_command method or self.optargs.

::

    options = climson.BaseCommand.options + (
        make_option('-n', '--name', help='Your name', required=True, dest='name'),
        make_option('-a', '--age', help='Your age', required=False, type=int, dest='age'),  
    )

::

    class Goodbye(climson.BaseCommand):

        name = 'goodbye'

        description = 'Say goodbye!'

        options = climson.BaseCommand.options + (
            make_option('-n', '--name', help='Your name', required=True, dest='name'),
            make_option('-a', '--age', help='Your age', required=False, type=int, dest='age'),  
        )

        #
        # commandline-option's name/value as **kwargs
        #
        def do_command(self, message=None, age=0):
            print 'Goodbye, {}(age:{}) in kwargs'.format(message, age)

            # Or can reference original args object with self.optargs
            print 'Goodbye, {}(age:{}) in optargs'.format(self.optargs.message, self.optargs.are)

        #
        # Do Custom validate if you need.
        #
        def validate(self, message=None, age=0):
            if age < 0:
                raise ValidateError('Specify age!')
            return True

.. note::
    If you want to validate option values, override method *validate(self, **kwargs)*. It returns bool as check result or raise climson.climson.ValidateError when validate failed.



Register commands and kick it.

*climson.climsonClient.__init__* arguments link to *argparse.ArgumentParser()*'s it.

::

    if __name__ == '__main__':
        from climson import climsonClient
        message_client = climsonClient(description='Show some messages!', prog='Myprog')
        message_client.add(Hello)
        message_client.add(GoodBye)
        message_client.execute()

So you can execute application with command.

::

    $ python my_command.py --help
    $ python my_command.py hello --help
    $ python my_command.py hello
    $ python my_command.py goodbye --name Michel --age 20


Commandfy decorator
-----------
commandfy-decorator to simplify further these implementation of climsonize.
You can execute commands only prepare method of each commands.

::

    from climson import commandfy
    from climson import commandfy_client

    @commandfy(description='Say hello!')
    def hello():
        print 'Hello!'

    @commandfy(description='Say goodbye!')
    def goodbye(name=None, age=0):
        print 'Goodbye, {}(age:{})'.format(message, age)

    if __name__ == '__main__':
        commandfy_client.execute()

.. note::
    * If you want to validate options, you have to implement that yourself.
    * Can not specify commandline opt type, short name, actions etc..
    * But commandfy is so simple!

Installation 
-----------

climson is hosted on two different platforms, PyPI_ and GitHub_.

#. **Install from PyPI**

    Install climson from PyPI_ for a stable version ::

        $ sudo pip install climson

#. **Get Clime from GitHub**

    If you want to follow the latest version of climson, use ::

        $ git clone git://github.com/takumakanari/climson.git
    
    to clone a repository, or download manually from GitHub_.


.. _GitHub:
    http://github.com/takumakanari/climson

.. _PyPI:
    http://pypi.python.org/pypi/climson

