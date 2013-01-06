Installation
------------

You may list ``Products.PFGSelectionStringField`` to ``buildout.cfg`` or ``setup.py`` in your own package.

zc.buildout and the plone.recipe.zope2instance
==============================================

Use zc.buildout and the plone.recipe.zope2instance
recipe by adding ``Products.PFGSelectionStringField`` to the list of egg::

    [buildout]
    ...
    eggs =
        ...
        Products.PFGSelectionStringField


Dependency to your own package
==============================

You may also list to install_requires to ``setup.py`` within your package.
