import pymupdf
import streamlit as st
import os

_DOC_EXTS = [
    'pdf','xps','epub',
    'mobi','fb2','cbz',
    'txt','svg'
]
_IMAGE_EXTS = [
    'jpg','jpeg','png',
    'bmp','gif','tiff',
    'pnm','pgm','pbm',
    'ppm','pam','jxr',
    'jpx','jpg','psd'
]

"""
# Extract text from PDF
"""

if "contents" not in st.session_state:
    st.session_state.contents = ""
if "outfile" not in st.session_state:
    st.session_state.outfile = "output.txt"

def handle_file_upload():
    # Interpret filename and extension
    print(st.session_state.file_up)
    filename, file_extension = os.path.splitext(st.session_state.file_up.name)
    # We handle depending on extension type
    if file_extension.lower()[1:] in _IMAGE_EXTS:
        print("This is an image")
    else:
        print("This is a document")

    # file stored in `st.session_state.file_up`
    #doc = pymupdf.open(st.session_state.file_up)

    # Generate output file
    #out = open(st.session_state.outfile, 'wb')
    # iterate through pages
    #for page in doc:
        # Get plain text in UTF-8
    #    text = page.get_text().encode('utf8')
    #    out_write()
    # output
    #st.session_state.contents = "\n\n".join(content_list)

st.text_input(
    'output file name',
    key='outfile'
)

st.file_uploader(
    label="Upload PDF",
    key="file_up",
    type=_DOC_EXTS+_IMAGE_EXTS,
    on_change=handle_file_upload
)