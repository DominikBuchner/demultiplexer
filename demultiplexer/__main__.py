import datetime, pkg_resources, os
import PySimpleGUI as sg
from demultiplexer import file_pairs
from demultiplexer import save_primerset
from demultiplexer.scheme_generator import scheme_layout
from demultiplexer.scheme_generator import save_scheme
from demultiplexer import demultiplexing
from pathlib import Path


## define pathes to the primersets and taggings templates
primersets_path = Path(pkg_resources.resource_filename(__name__, 'data/primersets/'))
tagging_templates_path = Path(pkg_resources.resource_filename(__name__, 'data/tagging_templates/'))

def main():
    ## defines the layout of demultiplexer
    main_layout = [
                  [sg.Frame(layout = [
                  [sg.Text('Select all files to demultiplex:')],
                  [sg.InputText(size = (20, 1), key = '_FILES_'), sg.FilesBrowse(), sg.Button('Load files')]],
                  title = 'Input files')],
                  [sg.Frame(layout = [
                  [sg.Text('Create primer set:')],
                  [sg.Text('Number of primers per direction:'), sg.Spin([i for i in range(1, 21)], size = (3, 1), key = '_NUM_PRIMERS'), sg.Button('Create primer set')],
                  [sg.Text('Select existing primerset:')],
                  [sg.InputText(size = (41, 1), key = '_PRIMERSET_'), sg.FileBrowse(initial_folder = primersets_path, file_types = (("Text Files", "*.txt"),))]],
                  title = 'Primer information')],
                  [sg.Frame(layout = [
                  [sg.Text('Create a new tagging scheme:')],
                  [sg.Text('Number of primer combinations used:'), sg.Spin([i for i in range(1, 21)], size = (3, 1), key = '_USED_COMBS_'), sg.Button('Create tagging scheme')],
                  [sg.Text('Select existing tagging scheme:')],
                  [sg.InputText(size = (41, 1), key = '_TAGGING_SCHEME_'), sg.FileBrowse(initial_folder = tagging_templates_path, file_types = (("Worksheets", "*.xlsx"),))],
                  [sg.Button('Modify selected scheme')]],
                  title = 'Tagging information')],
                  [sg.Frame(layout = [
                  [sg.Text('Select an output folder:')],
                  [sg.InputText(size = (41, 1), key = '_OUTPUT_PATH_'), sg.FolderBrowse()],
                  [sg.Checkbox('Remove tags from sequence', key = '_TAG_REMOVAL_'), sg.Button('Start demultiplexing', button_color = ('white', 'red'), size = (20, 2))]],
                  title = 'Output information')],
                  [sg.Frame(layout = [
                  [sg.Multiline(size = (57, 10), key = '_OUTSTREAM_', autoscroll = True)]],
                  title = 'Output')],
                  ]

    ## creates the window element
    window = sg.Window('Demultiplexer', main_layout)
    primer_window_active = False
    scheme_gen_active = False

    ### main loop
    while True:
        event, values = window.read(timeout = 100)

        ## code to close the program
        if event == None or event == 'Exit':
            break

        ## code to check the selected files
        if event == 'Load files':
            if not values['_FILES_']:
                window['_OUTSTREAM_'].print('{}: Please select files first.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
            else:
                files = values['_FILES_'].split(';')
                pairs = [i for i in file_pairs.main(files) if len(i) == 2]
                window['_OUTSTREAM_'].print('{}: {} files were loaded.'.format(datetime.datetime.now().strftime("%H:%M:%S"), len(files)))
                window['_OUTSTREAM_'].print('{}: {} valid file pairs were found.'.format(datetime.datetime.now().strftime("%H:%M:%S"), len(pairs)))

        ## opens the primerset generator, second part will prevent to windows open at the same time
        if event == 'Create primer set' and not primer_window_active:
            ## activate the primer generator window
            primer_window_active = True

            ## define the primer generator layout
            fwd_col = [[sg.Input(size = (15, 1)), sg.Input(size = (10, 1))] for i in range(int(values['_NUM_PRIMERS']))]
            rev_col = [[sg.Input(size = (15, 1)), sg.Input(size = (10, 1))] for i in range(int(values['_NUM_PRIMERS']))]

            ## no better way to adjust the padding around the headers
            ## layout definition for the primerset generator
            primerset_layout = [[sg.Text('Name of primerset:'), sg.Input(size = (20, 1), key = '_PRIMERSETNAME_')],
                               [sg.Frame(layout = [
                               [sg.Text(' Name'), sg.Text('                 Sequence')],
                               [sg.Column(fwd_col)]],
                               title = 'Forward primers'),
                               sg.Frame(layout = [
                               [sg.Text(' Name'), sg.Text('                 Sequence')],
                               [sg.Column(rev_col)]],
                               title = 'Reverse primers')],
                               [sg.Button('Close'), sg.Button('Save')]
                               ]

            primer_window = sg.Window('Primer generator', primerset_layout)

        ## read the window only if active, handle all input to primer generator window
        if primer_window_active:
            primer_ev, primer_vals = primer_window.read(timeout = 100)

            if primer_ev == None or primer_ev == 'Close':
                primer_window_active = False
                primer_window.close()

            ## save the primerset in the modules data path
            if primer_ev == 'Save':
                ## code to save the primerset, only works if a name is in the primersets name Input Box
                if primer_vals['_PRIMERSETNAME_'] != '':
                    save_primerset.save_primerset(primer_vals, primersets_path, window['_OUTSTREAM_'])
                else:
                    window['_OUTSTREAM_'].print('{}: Please choose a valid name for your primerset.'.format(datetime.datetime.now().strftime("%H:%M:%S")))


        ## opens the tagging scheme generator
        ## all tagging scheme generator code can be found here
        if event == 'Create tagging scheme' and values['_PRIMERSET_'] != '' and 'pairs' in locals():
            ## activate the scheme generator window
            scheme_gen_active = True

            ## generate the layout at runtime
            scheme_gen_layout = scheme_layout(values['_USED_COMBS_'], values['_PRIMERSET_'])

            scheme_gen_window = sg.Window('Tagging scheme generator', scheme_gen_layout)

        ## read the window
        if scheme_gen_active:
            scheme_ev, scheme_vals = scheme_gen_window.read(timeout = 100)

            ## close the scheme gen window if X or Close is hit
            if scheme_ev == None or scheme_ev == 'Close':
                scheme_gen_active = False
                scheme_gen_window.close()

            if scheme_ev == 'Save':
                if scheme_vals['_TAGGING_SCHEME_NAME_'] == '':
                    window['_OUTSTREAM_'].print('{}: Please choose a valid name for your tagging scheme.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
                else:
                    save_scheme(pairs, scheme_vals, tagging_templates_path, window['_OUTSTREAM_'])

        ## check if files are selected and a primerset is selected
        if event == 'Create tagging scheme':
            if not 'pairs' in locals():
                window['_OUTSTREAM_'].print('{}: Please load files to demultiplex.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
            if values['_PRIMERSET_'] == '':
                window['_OUTSTREAM_'].print('{}: Please select a primerset.'.format(datetime.datetime.now().strftime("%H:%M:%S")))

        ## code to modify the scheme
        if event == 'Modify selected scheme':
            if values['_TAGGING_SCHEME_'] == '':
                window['_OUTSTREAM_'].print('{}: Please select a tagging scheme.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
            else:
                os.startfile(values['_TAGGING_SCHEME_'])

        if event == 'Start demultiplexing':
            if not 'pairs' in locals():
                window['_OUTSTREAM_'].print('{}: Please load files to demultiplex.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
            if values['_PRIMERSET_'] == '':
                window['_OUTSTREAM_'].print('{}: Please select a primerset.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
            if values['_TAGGING_SCHEME_'] == '':
                window['_OUTSTREAM_'].print('{}: Please select a tagging scheme.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
            if values['_OUTPUT_PATH_'] == '':
                window['_OUTSTREAM_'].print('{}: Please select an output folder.'.format(datetime.datetime.now().strftime("%H:%M:%S")))
            else:
                demultiplexing.main(values['_PRIMERSET_'], values['_TAGGING_SCHEME_'], values['_OUTPUT_PATH_'], values['_TAG_REMOVAL_'], window['_OUTSTREAM_'], window)

    window.close()

## run only if called as a toplevel script
if __name__ == "__main__":
    main()
