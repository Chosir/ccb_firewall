# coding=utf-8

import xlrd
import xlsxwriter

def main():
    src_workbook = xlrd.open_workbook('ccb.xlsx')
    src_sheets_len = len(src_workbook.sheets())
    dst_workbook = xlsxwriter.Workbook('demo.xlsx')
    wb_format = dst_workbook.add_format()
    wb_format.set_text_wrap()
    dst_worksheet = dst_workbook.add_worksheet()
    hearder = (u'源区域', u'源IP', u'目的区域', u'目的IP', u'访问控制点1', u'访问控制点2', u'访问控制点3')
    dst_worksheet.write_row('A1', hearder)

    x = 2
    for i in range(1, src_sheets_len):
        cur_sheet = src_workbook.sheet_by_index(i)
        for j in range(1, cur_sheet.nrows):
            row = 'A' + str(x)
            if '-' in cur_sheet.row_values(j)[1] or '-' in cur_sheet.row_values(j)[3]:
                dst_worksheet.write_row(row, format_trans(cur_sheet.row_values(j)), wb_format)
            else:
                dst_worksheet.write_row(row, cur_sheet.row_values(j), wb_format)
            x += 1

    dst_workbook.close()


def format_trans(line):
    dst_lines = []
    dst_line = ''
    for k in range(len(line)):
        if k == 1 and '-' in line[1]:
            cell = line[1]
            cell_line = cell.split('\n')
            for i in range(len(cell_line)):
                if '-' in cell_line[i]:
                    atom = cell_line[i].split('.')
                    ip1 = atom[0]
                    ip2 = atom[1]
                    ip3 = atom[2]
                    ip4 = atom[3]
                    x = 0
                    for j in range(len(atom)):
                        if '-' in atom[j]:
                            floor = int(atom[j].split('-')[0])
                            top = int(atom[j].split('-')[1])
                            break
                        else:
                            x += 1
                    if x == 0:
                        for m in range(floor, top+1):
                            dst_line += "%s.%s.%s.%s\n" % (str(m), ip2, ip3, ip4)
                    if x == 1:
                        for m in range(floor, top+1):
                            dst_line += "%s.%s.%s.%s\n" % (ip1, str(m), ip3, ip4)
                    if x == 2:
                        for m in range(floor, top+1):
                            dst_line += "%s.%s.%s.%s\n" % (ip1, ip2, str(m), ip4)
                    if x == 3:
                        for m in range(floor, top+1):
                            dst_line += "%s.%s.%s.%s\n" % (ip1, ip2, ip3, str(m))
                else:
                    dst_line += "%s\n" % (cell_line[i].strip())
            dst_lines.append(dst_line)
            dst_line = ''
        elif k == 3 and '-' in line[3]:
            cell = line[3]
            cell_line = cell.split('\n')
            for i in range(len(cell_line)):
                if '-' in cell_line[i]:
                    atom = cell_line[i].split('.')
                    ip1 = atom[0]
                    ip2 = atom[1]
                    ip3 = atom[2]
                    ip4 = atom[3]
                    x = 0
                    for j in range(len(atom)):
                        if '-' in atom[j]:
                            floor = int(atom[j].split('-')[0])
                            top = int(atom[j].split('-')[1])
                            break
                        else:
                            x += 1
                    if x == 0:
                        for m in range(floor, top + 1):
                            dst_line += "%s.%s.%s.%s\n" % (str(m), ip2, ip3, ip4)
                    if x == 1:
                        for m in range(floor, top + 1):
                            dst_line += "%s.%s.%s.%s\n" % (ip1, str(m), ip3, ip4)
                    if x == 2:
                        for m in range(floor, top + 1):
                            dst_line += "%s.%s.%s.%s\n" % (ip1, ip2, str(m), ip4)
                    if x == 3:
                        for m in range(floor, top + 1):
                            dst_line += "%s.%s.%s.%s\n" % (ip1, ip2, ip3, str(m))
                else:
                    dst_line += "%s\n" % (cell_line[i].strip())
            dst_lines.append(dst_line)
        else:
            dst_lines.append(line[k])
    return dst_lines

if __name__ == '__main__':
    main()