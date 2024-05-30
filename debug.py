from bs4 import BeautifulSoup


def extract_sig_param(source_path):
    sig_param = {}

    with open(source_path) as f:
        source = f.read()

    soup = BeautifulSoup(source, 'lxml')

    table_tag = soup.find('table', 'infobox')
    tr_tag = table_tag.find_all('tr')

    for row in tr_tag:

        th_tag = row.find('th')
        td_tag = row.find('td')
        spectrum_tag = row.find('img')
        audio_tag = row.find('audio')

        if spectrum_tag == None and audio_tag == None:
            if td_tag.text != None:
                sig_param[th_tag.text] = td_tag.text.strip()
            else:
                sig_param[th_tag.string] = None

        elif spectrum_tag != None:
            try:
                src = spectrum_tag['srcset'].split(',')[-1].split()[0]
            except:
                src = spectrum_tag['src']

            sig_param['Spectrum'] = src

        elif audio_tag != None:
            sig_param['Audio'] = audio_tag['src']

extract_sig_param('source.txt')
