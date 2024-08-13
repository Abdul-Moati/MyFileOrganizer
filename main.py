"""
3. File Organizer
Description: Develop a tool that helps users organize files on their computer.
Users can select a directory, and the program will automatically categorize files
based on their extensions (e.g., images, documents, videos) into folders.

Challenge: Handling large numbers of files efficiently, dealing with potential file conflicts
and providing options for undoing actions.
"""

# Libraries
import FreeSimpleGUI as fsg

# Aesthetics
background_color = '#FFD580'
vivid_orange = '#E67E22'


# Labels
welcome_label = fsg.Text("Welcome to My Folder Organizer!",
                           font=('Calibri', 30), text_color=vivid_orange, background_color=background_color,
                           justification='center', size=(30, 1))

explanation_label = fsg.Text("One time, I had enough courage to open my Downloads folder after years of neglect.\n"
                             "Well, let's just say it was not that nice. Wait.. that wasn't accurate enough."
                             "\nIT WAS TOTAL CHAOS!!\n\n"
                             "Anyhow, out of sheer boredom, the desire to make my first GUI program,"
                             " and the need to restore some digital order, "
                             "I created this humble project to clean my-and your-digital mess!\n\n"
                             "In short, this project creates a new folder for each selected file extension\n"
                             "and moves all relevant files to that new folder.\n\n"
                             "Enjoy ;)",
                             font=('Helvetica', 10, 'italic'), text_color='black', background_color=background_color,
                             justification='center', size=(75, 11))


directory_label = fsg.Text("Insert the directory of the folder you want to organize",
                           font=('Calibri', 18), text_color='black', background_color=background_color,
                           justification='center', size=(50, 1))

directory_example_label = fsg.Text("Example: 'D:/Data/Personal/Photos/Travel/Europe/Italy/Rome/Colosseum'",
                           font=('Courier New', 10), text_color='red', background_color=background_color)

file_types_label = fsg.Text("Check the types (extensions) of the files you want to group together",
                            font=('Calibri', 16), background_color='black', justification='center', size=(55, 1))

empty_label = fsg.Text("", background_color=background_color)

desired_extension_label = fsg.Text("In case your desired extensions are not among the checkboxes,\n"
                                   "please write them in the whitespace below.\n\n"
                                   "You can write multiple file extensions separated by a blank space.\n"
                                   "Example: .psd .SLDPRT .reg .hex .mlx .torrent", background_color='grey')


# Input Boxes
directory_input_box = fsg.InputText(size=(86, 3), tooltip="Directory", key="DIRECTORY")

desired_extensions_input_box = fsg.InputText(size=(55, 3), tooltip="Extensions", key="EXTENSIONS")


# Check Boxes
video_check_box = fsg.Checkbox(['Video (.mp4)'], default=False, key='.mp4', background_color='grey')
image_check_box = fsg.Checkbox(['Image (.png/.jpg/.jpeg)'], default=False, key='.png .jpg. jpeg', background_color='grey')
audio_check_box = fsg.Checkbox(['Audio (.mp3'], default=False, key='.mp3', background_color='grey')

pdf_check_box = fsg.Checkbox(['PDF (.pdf)'], default=False, key='.pdf', background_color='grey')
text_check_box = fsg.Checkbox(['Text (.txt)'], default=False, key='.txt', background_color='grey')
archive_check_box = fsg.Checkbox(['Archive (.zip/.rar)'], default=False, key='.zip .rar', background_color='grey')

word_check_box = fsg.Checkbox(['Word (.doc/.docx)'], default=False, key='.doc', background_color='grey')
powerpoint_check_box = fsg.Checkbox(['Powerpoint (.ppt/.pptx)'], default=False, key='.ppt', background_color='grey')
Excel_check_box = fsg.Checkbox(['Excel (.xls/.xlsx)'], default=False, key='.xls', background_color='grey')



# Buttons
confirmation_button = fsg.Button("Organize My Folder!", button_color=('black', 'green'), size=(20, 2))



# Columns
clmn = fsg.Column(
    [
    [confirmation_button]
    ]
    ,justification='right', background_color=background_color)



layout = [
    [welcome_label],
    [explanation_label],
    [directory_label],
    [directory_input_box],
    [directory_example_label],
    [empty_label],
    [file_types_label],
    [text_check_box,pdf_check_box,archive_check_box],
    [video_check_box, image_check_box, audio_check_box],
    [word_check_box,powerpoint_check_box,Excel_check_box],
    [desired_extension_label],
    [desired_extensions_input_box],
    [clmn]
    ]


# Main Window
window = fsg.Window('My Folder Organizer', layout, background_color='#FFD580')

true_check_boxes = []

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["DIRECTORY"])
    print(values["EXTENSIONS"])

    for key, value in values.items():
        if value:
            true_check_boxes.append(key)

    print(true_check_boxes)




    if event == fsg.WINDOW_CLOSED:
            break

window.close()
