import ast
import csv
import errno
import os

from authorscanner import AuthorScanRepository
from shutil import copyfile


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

'''
def interpolateMissingComponent(graph_content, i, last_item, lookahead_item):
    if last_item is None:
        last_item = 0

    if lookahead_item is None:
        lookahead_item = 0

    graph_content[i] = (last_item + lookahead_item) / 2     # arithmetic mean


def assertInterpolationOnMissingComponents(graph_content):
    last_item = None

    ct_len = len(graph_content)
    for i in range(graph_content):
        item = graph_content[i]

        if item == 0.0:
            if i + 1 < ct_len:
                lookahead_item = graph_content[i + 1]
            else:
                lookahead_item = None

            interpolateMissingComponent(graph_content, i, last_item, lookahead_item)

        last_item = item
'''


class AuthorGraphResultPrinter:

    def writeCsvFile(self, file_path, column_names, graph_rows, dist=False):
        global scanner
        scanner = AuthorScanRepository.scanner

        if dist:
            folder_path = scanner.plot_path
        else:
            folder_path = scanner.csv_path

        file_name = folder_path + '/' + file_path[0:file_path.rfind('.')] + '.csv'

        setupDir(file_name)
        with open(file_name, 'w', encoding='UTF-32') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter='§', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

            csvwriter.writerow(column_names)
            for row in graph_rows:
                csvwriter.writerow(row)


    def readCsvFile(self, file_path):
        global scanner
        scanner = AuthorScanRepository.scanner

        file_name = scanner.csv_path + '/' + file_path[0:file_path.rfind('.')] + '.csv'

        graph_rows = []
        with open(file_name, 'r', encoding='UTF-32') as csvfile:
            csvreader = csv.reader(csvfile, delimiter='§', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

            for row in csvreader:
                row_elements = []

                for elem in row:
                    try:
                        row_elements.append(ast.literal_eval(elem))
                    except (ValueError, SyntaxError):
                        try:
                            elem = elem.translate(str.maketrans({"\"": r"\"",
                                                                 "\'": r"\'"}))

                            row_elements.append(ast.literal_eval('"' + elem + '"'))
                        except:
                            row_elements.append(None)

                graph_rows.append(row_elements)

        column_names = graph_rows[0]
        graph_rows = graph_rows[1:]

        return column_names, graph_rows


    def fetchGraphColumnNamesFromItem(self, graph_item, init_str):
        rows = []

        for k, v in graph_item.items():
            if type(v) is dict:
                rows.extend(self.fetchGraphColumnNamesFromItem(v, init_str + '_' + str(k)))
            else:
                rows.append(init_str + '_' + str(k))

        return rows


    def fetchGraphColumnValuesFromItem(self, graph_item):
        rows = []

        for k, v in graph_item.items():
            if type(v) is dict:
                rows.extend(self.fetchGraphColumnValuesFromItem(v))
            else:
                rows.append(v)

        return rows


    def fetchGraphColumnValues(self, dir_meta):
        if type(dir_meta) is dict:
            return self.fetchGraphColumnValuesFromItem(dir_meta)
        else:
            return [dir_meta]


    def loadGraphDatasetFormat(self, graph_column_names, graph_content):
        # add column labels to all nodes in a list of tuples "graph_content"
        graph_ds = []

        for graph_item in graph_content:
            graph_ds_item = {}
            graph_ds.append(graph_ds_item)

            for graph_node_idx in range(len(graph_item)):
                graph_node = graph_item[graph_node_idx]

                graph_ds_item[graph_column_names[graph_node_idx]] = graph_node

        return graph_ds


    def normalizeTupleGraphContents(self, graph_content):
        if type(graph_content[0]) is tuple:
            graph_ct = []

            for graph_it in graph_content:
                graph_tp = graph_it[1]
                graph_tp['name'] = graph_it[0]

                graph_ct.append(graph_tp)

            return graph_ct
        else:
            return graph_content


    def fetchCsvFilename(self, file_path, doc_index):
        if doc_index < 0:
            return file_path

        idx = file_path.rfind('.')
        path_st = file_path[0:idx]
        path_ext = file_path[idx:]

        file_path = path_st + '_jn' + str(doc_index) + path_ext
        return file_path


    def fetchGraphFilename(self, csv_file_path, doc_index=-1):
        global scanner
        scanner = AuthorScanRepository.scanner

        idx = csv_file_path.rfind('.')
        file_path = csv_file_path[0:idx]

        graph_filename = scanner.plot_path + '/' + file_path

        if type(doc_index) is str:
            graph_filename += '_' + doc_index
        elif doc_index >= 0:
            graph_filename += '_jn' + str(doc_index)

        return graph_filename + '.png'


    def writeGraphDataset(self, file_path, graph_content, doc_index = -1):
        if len(graph_content) > 0:
            graph_content = self.normalizeTupleGraphContents(graph_content)
            file_path = self.fetchCsvFilename(file_path, doc_index)

            column_names = []
            for name in self.fetchGraphColumnNamesFromItem(graph_content[0], ''):
                column_names.append(name[1:])

            rows = []
            for dir_meta in graph_content:
                rows.append(self.fetchGraphColumnValues(dir_meta))

            self.writeCsvFile(file_path, column_names, rows)


    def readGraphDataset(self, file_path, doc_index = -1):
        file_path = self.fetchCsvFilename(file_path, doc_index)

        column_names, graph_content = self.readCsvFile(file_path)
        return column_names, graph_content


    def replicateGraphDataset(self, file_path, column_names, rows, doc_index = -1):
        file_path = self.fetchCsvFilename(file_path, doc_index)
        self.writeCsvFile(file_path, column_names, rows, dist=True)


    '''
    def hasDictInterpolated(self):



    def interpolateMissingComponents(self, graph_content):
        ct_type = type(graph_content)

        if ct_type is list:
            if len(graph_content) > 0:
                ct_type_internal = type(graph_content[0])

                if ct_type_internal is int or ct_type_internal is float:
                    assertInterpolationOnMissingComponents(graph_content) # check interpolation

        if ct_type is dir:
            if len(graph_content) > 0:
                graph_content_vals = graph_content.values()
                ct_type_internal = type(graph_content_vals[0])

                graph_content_vals_copy = graph_content_vals.copy()
                if ct_type_internal is int or ct_type_internal is float:
                    assertInterpolationOnMissingComponents(graph_content_vals_copy) # check interpolation

                if




            for item in graph_content:
    '''

    def savePlot(self, sns_fig, plot_filepath):
        setupDir(plot_filepath)
        sns_fig.savefig(plot_filepath, dpi=1000, figsize=(6.40,7.00))


    def __init__(self):
        global grapher
        grapher = self


global grapher
grapher = None