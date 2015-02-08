from calibre.gui2.actions import InterfaceAction

AscendingOrder = 0

class SortBySeriesPlugin(InterfaceAction):
    name='Sort By Series'
    action_spec = ('Sort By Series Plugin',None,'Run Sort By Series Plugin','Ctrl+Shift+s')
    
    def genesis(self):
        print 'called genesis in SortBySeriesPlugin'
        self.qaction.triggered.connect(self.sort)

    def sort(self):
        model = self.gui.library_view.model()
        idx = model.column_map.index("series")
        self.gui.library_view.sortByColumn(idx,AscendingOrder)

