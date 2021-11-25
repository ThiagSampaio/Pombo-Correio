import mammoth


def docx_2_html(file):

    result = mammoth.convert_to_html(file)
    return result
