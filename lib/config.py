class Config:
    def __init__(self, file = "", sheet = "", col_pn = 3, col_name = 2, col_position = 4, col_first_day = 6, row_from = 0, row_to = 0 ):
        self.file = file
        self.sheet = sheet
        self.col_pn = col_pn
        self.col_name = col_name
        self.col_position = col_position
        self.col_first_day = col_first_day
        self.row_from = row_from
        self.row_to = row_to

    def __repr__(self):
        return "Config(file={}, sheet={}, col_pn={}, col_name={}, col_first_day={}, row_from={}, row_to={} \
        )".format(self.file, self.sheet, self.col_pn, self.col_name, self.col_first_day, self.row_from, self.row_to)
