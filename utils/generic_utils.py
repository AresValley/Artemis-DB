import requests
import hashlib
import re

from bs4 import BeautifulSoup

from utils.constants import *


def _get_source (url):
    response = requests.get(url)
    return response.content


def extract_sig_param(url):
    
    sig_param = {}
    
    source = _get_source(url)
    soup = BeautifulSoup(source, 'lxml')
        
    table_tag = soup.find('table', 'infobox')
    tr_tag = table_tag.find_all('tr')

    cat_tag = soup.find('div', 'mw-normal-catlinks')
    categories = [a.text for a in cat_tag.find_all('a') if 'title' in a.attrs and 'Category:' in a.attrs['title']]

    for row in tr_tag:
        th_tag = row.find('th')
        td_tag = row.find('td')
        spectrum_tag = row.find('img')
        audio_tag = row.find('audio')
        
        if spectrum_tag == None and audio_tag == None:
            if td_tag.text != None:
                sig_param[th_tag.text] = td_tag.text.strip()
            else:
                sig_param[th_tag.text] = None

        elif spectrum_tag != None:
            try:
                src = spectrum_tag['srcset'].split(',')[-1].split()[0]
            except:
                src = spectrum_tag['src']
                
            sig_param['Spectrum'] = Url.SIGID_DOMAIN + src
            
        elif audio_tag != None:
            sig_param['Audio'] = audio_tag['src']
    
    sig_param['Category'] = [cat for cat in categories if cat in Constants.CATEGORIES]
    return sig_param


def format_freq(freq_string):
    freq_list = []
    matches = re.findall(r'(\d+(\.\d+)?)\s*(\w+)', freq_string)

    for freq in matches:
        formatted_freq = int(float(freq[0]) * Constants.UNIT_TO_FACTOR[freq[2]])
        freq_list.append(formatted_freq)

    return freq_list


def format_acf(acf_string):
    if acf_string == '—':
        return []
    
    else:
        acf_list = []
        acf_string = acf_string.split(',')
        for i in acf_string:
            if ':' in i:
                i = i.split(':')
                
                try:
                    acf_description = i[0].strip()
                    acf_value = float(i[1].replace('ms','').strip())
                
                except:
                    acf_value = 0
                    acf_description = ':'.join(i)   
            
            else:
                try:
                    acf_description = 'Main'
                    acf_value = float(i.replace('ms','').strip())
                except:
                    acf_value = 0
                    acf_description = i.strip()

            acf_list.append((acf_description, acf_value))

        return acf_list


def format_text(raw_string):
    """ Used for modulation, mode and location
    """
    if raw_string == '—':
        list_result = []
    else:
        list_result = raw_string.split(',')
    
    list_result = [x.strip() for x in list_result]

    return list_result


def checksum_sha256(data):
    """ Calculate SHA256 hash
    """
    code  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(data, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            code.update(mv[:n])
            
    return code.hexdigest()


def get_extension(url):
    file_name = url.split('/')[-1]
    extension = file_name.split('.')[-1]
    return extension
