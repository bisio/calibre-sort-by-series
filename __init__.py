from calibre.customize import InterfaceActionBase

class SortBySeriesBase(InterfaceActionBase):

    name = 'Sort By Series'
    author = 'Andrea Bisognin'
    supported_platforms = ['windows', 'osx', 'linux']
    version             = (1, 0, 3)
    

    actual_plugin = 'calibre_plugins.sort_by_series.ui:SortBySeriesPlugin'
    print actual_plugin

    def is_customizable(self):
        return False

    

