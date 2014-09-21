# -*- coding:utf-8 -*-
#  Copyright (c) 2010-2011 openpyxl
#  Copyright (c) 2012 @yamada_program 
#
#  http://yamada-program.blogspot.jp/2012/10/python-openpyxl.html

import openpyxl
 
def write_worksheet_sheetviews(doc, worksheet):
    from openpyxl.writer.worksheet import start_tag, end_tag, tag
    from openpyxl.cell import coordinate_from_string
    from openpyxl.worksheet import column_index_from_string
     
    viewattrs = {'workbookViewId': '0'}
    #その他ビューパラメータを取得
    sheetview = worksheet.sheet_view
    if sheetview:
        if hasattr(sheetview, 'zoomScale'):
            viewattrs['zoomScale'] = sheetview.zoomScale
        if hasattr(sheetview, 'zoomScaleNormal'):
            viewattrs['zoomScaleNormal'] = sheetview.zoomScaleNormal
     
    start_tag(doc, 'sheetViews')
    start_tag(doc, 'sheetView', viewattrs)
    selectionAttrs = {}
    topLeftCell = worksheet.freeze_panes
    if topLeftCell:
        colName, row = coordinate_from_string(topLeftCell)
        column = column_index_from_string(colName)
        pane = 'topRight'
        paneAttrs = {}
        if column > 1:
            paneAttrs['xSplit'] = str(column - 1)
        if row > 1:
            paneAttrs['ySplit'] = str(row - 1)
            pane = 'bottomLeft'
            if column > 1:
                pane = 'bottomRight'
        paneAttrs.update(dict(topLeftCell=topLeftCell,
                              activePane=pane,
                              state='frozen'))
        tag(doc, 'pane', paneAttrs)
        selectionAttrs['pane'] = pane
        if row > 1 and column > 1:
            tag(doc, 'selection', {'pane': 'topRight'})
            tag(doc, 'selection', {'pane': 'bottomLeft'})
 
    selectionAttrs.update({'activeCell': worksheet.active_cell,
                           'sqref': worksheet.selected_cell})
 
    tag(doc, 'selection', selectionAttrs)
    end_tag(doc, 'sheetView')
    end_tag(doc, 'sheetViews')
 
 
# 既定のwriterメソッドを置き換え
openpyxl.writer.worksheet.write_worksheet_sheetviews = write_worksheet_sheetviews
