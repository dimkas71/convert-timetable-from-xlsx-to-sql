Sub SaveCellsAsValues()
    Dim wsh As Worksheet
    For Each wsh In ThisWorkbook.Worksheets
        wsh.Cells.Copy
        wsh.Cells.PasteSpecial xlPasteValues
    Next
    Application.CutCopyMode = False
End Sub
